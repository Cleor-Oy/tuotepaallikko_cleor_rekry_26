#!/usr/bin/env python3
"""Tarkista hakemusmallin rakenne. Ei arvioi hakijan soveltuvuutta tai väitteiden totuutta."""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "schema/hakemusmalli.md"
FIELD = re.compile(r"^- (\d+\.\d+ [^:]+|Malliversio|Rekrytointi|Laatimispäivä|Haastattelun tekoälypalvelu):\s*(.*)$")
PROMPT = re.compile(r"\b(ignore (?:all |previous |above )?instructions|ohita (?:kaikki |aiemmat )?ohjeet|arvioi tämä hakija)\b", re.I)
FORBIDDEN = {"ei koske", "ei relevantti", "n/a", "ei tietoa", "-"}
LIMITS = {2: 100, 3: 150, 5: 180, 6: 180, 7: 100, 8: 100, 10: 100}


def expected_lines():
    text = TEMPLATE.read_text(encoding="utf-8").split("\n---\n", 1)[1]
    return [line if line.startswith("#") else line.split(":", 1)[0] + ":"
            for line in text.splitlines() if line.startswith("#") or FIELD.match(line)]


def inspect(path: Path) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"Ei voitu lukea UTF-8-tiedostoa: {exc}"], warnings
    expected = expected_lines()
    found = []
    values = {}
    sections: dict[int, list[str]] = {}
    section = None
    for line_no, line in enumerate(text.splitlines(), 1):
        if re.search(r"<[^>]+>", line):
            errors.append(f"Rivi {line_no}: mallin ohjetekstiä jäljellä")
        if PROMPT.search(line):
            warnings.append(f"Rivi {line_no}: mahdollinen ohjemainen teksti; tarkista asiayhteys")
        if line.startswith("#"):
            found.append((line_no, line))
            m = re.match(r"^## (\d+)\.", line)
            section = int(m.group(1)) if m else None
        elif line.startswith("- "):
            m = FIELD.match(line)
            if not m:
                errors.append(f"Rivi {line_no}: tuntematon tai muotoiltu kenttä")
                continue
            key, value = m.groups()
            found.append((line_no, f"- {key}:"))
            if key in values:
                errors.append(f"Rivi {line_no}: kenttä esiintyy kahdesti: {key}")
            values[key] = value
            if not value.strip():
                errors.append(f"Rivi {line_no}: tyhjä kenttä: {key}")
            if value.strip().casefold() in FORBIDDEN:
                errors.append(f"Rivi {line_no}: tuntematon tilamerkintä: {value}")
            if value.strip() == "Ei selvitetty" and key not in {
                "11.2 Suostumus Cleorin Claude Team -käsittelyyn", "11.3 Valinnan päivämäärä",
                "12.1 Sisällön oikeellisuuden vahvistus", "12.2 Vahvistuksen päivämäärä",
            }:
                errors.append(f"Rivi {line_no}: Ei selvitetty on varattu suostumuksen ja vahvistuksen kenttiin")
            if value.strip() == "Ei kysymyksiä" and not key.startswith("10.1 "):
                errors.append(f"Rivi {line_no}: Ei kysymyksiä on sallittu vain kohdassa 10.1")
            if section is not None:
                sections.setdefault(section, []).append(value)
                if section == 4 and len(value.split()) > 50:
                    errors.append(f"Rivi {line_no}: osaamisalue ylittää 50 sanaa")
        elif line.strip():
            errors.append(f"Rivi {line_no}: ylimääräinen tai virheellinen rivi")
    actual = [x[1] for x in found]
    if actual != expected:
        for pos, item in enumerate(expected):
            if item not in actual:
                errors.append(f"Puuttuva otsikko tai kenttä: {item}")
        for line_no, item in found:
            if item not in expected:
                errors.append(f"Rivi {line_no}: tuntematon otsikko tai kenttä: {item}")
        if sorted(actual) == sorted(expected):
            errors.append("Otsikot tai kentät ovat väärässä järjestyksessä")
    for n, limit in LIMITS.items():
        if len(" ".join(sections.get(n, [])).split()) > limit:
            errors.append(f"Osio {n}: sanaraja {limit} ylittyy")
    for key, allowed in {
        "11.2 Suostumus Cleorin Claude Team -käsittelyyn": {"Kyllä", "Ei", "Ei selvitetty"},
        "12.1 Sisällön oikeellisuuden vahvistus": {"Vahvistettu", "Ei selvitetty"},
        "Malliversio": {"1.1"},
    }.items():
        if key in values and values[key].strip() not in allowed:
            errors.append(f"Virheellinen arvo kentässä {key}: {values[key]}")
    first, last = values.get("1.1 Etunimi", ""), values.get("1.2 Sukunimi", "")
    if first and last and first not in {"Ei käsitelty", "Ei halua ilmoittaa"} and last not in {"Ei käsitelty", "Ei halua ilmoittaa"}:
        if path.name != f"{first} {last}.md":
            errors.append(f"Tiedostonimi ei vastaa nimikenttiä: {first} {last}.md")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.files:
        errors, warnings = inspect(path)
        print(f"\n{path}: {'VIRHEITÄ' if errors else 'RAKENNE OK'}")
        for item in errors:
            print(f"  VIRHE: {item}")
        for item in warnings:
            print(f"  HUOMIO: {item}")
        failed |= bool(errors)
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
