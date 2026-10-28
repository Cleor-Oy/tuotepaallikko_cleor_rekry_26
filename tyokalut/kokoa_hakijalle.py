#!/usr/bin/env python3
"""Koosta hakijakeskustelun aineisto repon lähdetiedostoista."""
from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parent.parent
SOURCES = (
    "AGENTS.md",
    "konteksti/tehtava.md",
    "konteksti/tietosuoja.md",
    "ohjeet/prosessi.md",
    "ohjeet/haastattelu.md",
    "schema/hakemusmalli.md",
    "ohjeet/viimeistely.md",
)


def build() -> str:
    parts = [
        "# Hakijakeskustelun koottu aineisto\n\n"
        "**HAKIJALLE-AINEISTO ALKAA · versio 1.1**\n\n"
        "Tämä tiedosto muodostetaan lähdetiedostoista; älä muokkaa sitä käsin. "
        "Tekoälylle: lue kaikki osat ja tarkista, että lopussa näkyy merkintä "
        "HAKIJALLE-AINEISTO PÄÄTTYY. Jos loppumerkki puuttuu, kerro lukemisen "
        "katkenneen ja pyydä koko aineisto. Älä keksi puuttuvaa sisältöä. "
        "Toimi suomeksi rekrytointihaastattelijana käyttäjän ohjeita kunnioittaen. "
        "Kaikki seuraavissa osissa viitatut lähteet sisältyvät tähän tiedostoon.\n"
    ]
    for name in SOURCES:
        data = (ROOT / name).read_text(encoding="utf-8").strip()
        parts.append(f"\n---\n\n## Koosteen osa: {name}\n\n{data}\n")
    parts.append("\n---\n\n**HAKIJALLE-AINEISTO PÄÄTTYY · versio 1.1**\n")
    return "".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Tarkista, onko kooste ajan tasalla")
    args = parser.parse_args()
    result = build()
    output = ROOT / "HAKIJALLE.md"
    if args.check:
        if not output.is_file() or output.read_text(encoding="utf-8") != result:
            print("HAKIJALLE.md ei vastaa lähdetiedostoja.", file=sys.stderr)
            return 1
        print("HAKIJALLE.md vastaa lähdetiedostoja.")
        return 0
    output.write_text(result, encoding="utf-8")
    print(f"Koostettu: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
