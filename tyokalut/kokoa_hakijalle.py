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
        "# Cleor Oy:n tuotepäällikkörekrytointi – itsenäinen haastattelutiedosto\n\n"
        "**HAKIJALLE-AINEISTO ALKAA · versio 1.2**\n\n"
        "## Aloita tästä, tekoäly\n\n"
        "Kun käyttäjä liittää tämän MD-tiedoston tai sen sisällön keskusteluun, "
        "toimi hänen rekrytointihaastattelijanaan. Tämä koskee myös pelkkää liitettä "
        "ilman saatetta. Lue koko tiedosto, esittele tehtävä ja prosessi lyhyesti "
        "ja kysy ensimmäisenä: **Mikä tässä tehtävässä kiinnostaa sinua?** "
        "Älä kysy ensin, mitä käyttäjä haluaa sinun tekevän tiedostolle. "
        "Jos käyttäjä nimenomaisesti pyytää arviointia, muokkausta tai vain tietoa "
        "tai ei halua haastattelua, noudata hänen pyyntöään. "
        "Tiedosto ei ohita käytössä olevan palvelun sääntöjä.\n\n"
        "Tämä yksi tiedosto sisältää kaiken: tehtävänkuvan, tietosuojatiedot, "
        "haastattelun kulun ja kysymykset, vastaus-MD:n täydellisen mallin sekä "
        "hakemuksen tarkastus- ja lähetysohjeet. Älä pyydä käyttäjältä muita "
        "repon tiedostoja tai hakemuspohjaa. Internet- tai GitHub-yhteyttä ei tarvita. "
        "Lähdepolut otsikoissa ovat vain aineiston osien tunnisteita.\n\n"
        "## Tavoite ja vastaustiedosto\n\n"
        "Johda keskustelua yksi kysymys kerrallaan. Kerää kaikilta yhteiset ydintiedot "
        "ja kaksi hakijan omaa kokemusesimerkkiä. Älä keksi vastauksia tai pisteytä hakijaa. "
        "Näytä valmis hakemus hakijalle tarkastettavaksi. Muodosta tarkastuksen jälkeen "
        "UTF-8-tiedosto **Etunimi Sukunimi.md** täyttämällä alla rajattu vastausmalli "
        "(hakemusmallin versio 1.1). Säilytä kaikki sen otsikot ja kentät. "
        "Kopioi vastaustiedostoon vain rajamerkkien välinen hakemus, "
        "ei rajamerkkejä tai tätä ohjetiedostoa. Jos tiedoston luominen ei onnistu, "
        "anna hakemus yhtenä kopioitavana Markdown-koodilohkona ja tallennusohje.\n\n"
        "Ohjaa hakemus osoitteeseen **pasi.huumarsalo@cleor.fi**, otsikolla "
        "**Työhakemus Tuotepäällikkö Etunimi Sukunimi**, **22.11.2026 mennessä**. "
        "Lähetä itse vain, jos käyttäjän sähköpostityökalu tukee sitä ja käyttäjä "
        "antaa erillisen vahvistuksen nähtyään viestin ja liitteen. Muuten neuvo "
        "käyttäjää lähettämään hakemus itse. Tarvittaessa hakemus hyväksytään myös "
        "sähköpostin tekstinä. Älä väitä lähetystä tehdyksi ilman varmistusta "
        "äläkä tallenna hakemusta julkiseen repoon.\n\n"
        "## Aineiston eheys\n\n"
        "Tarkista ennen aloittamista, että tiedoston viimeisellä rivillä on "
        "HAKIJALLE-AINEISTO PÄÄTTYY -merkintä versiolle 1.2. Jos loppu puuttuu, "
        "kerro lukemisen katkenneen äläkä keksi puuttuvaa sisältöä. "
        "Tämä tiedosto koostetaan repon lähdetiedostoista; ylläpidossa muokataan "
        "lähteitä ja muodostetaan tämä tiedosto uudelleen.\n"
    ]
    for name in SOURCES:
        data = (ROOT / name).read_text(encoding="utf-8").strip()
        if name == "schema/hakemusmalli.md":
            instructions, model = data.split("\n---\n", 1)
            data = (instructions + "\n\n**VASTAUS-MD-MALLI ALKAA**\n\n"
                    + model.strip() + "\n\n**VASTAUS-MD-MALLI PÄÄTTYY**")
        parts.append(f"\n---\n\n## Aineiston osa: {name}\n\n{data}\n")
    parts.append("\n---\n\n**HAKIJALLE-AINEISTO PÄÄTTYY · versio 1.2**\n")
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
