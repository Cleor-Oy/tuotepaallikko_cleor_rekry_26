# Tarkastus ja hakemuksen lähettäminen

## Tarkista ennen luovutusta

1. Hakemus noudattaa `schema/hakemusmalli.md`-rakennetta: samat otsikot ja kentät samassa järjestyksessä, malliversio 1.0, ei ylimääräisiä arvioita.
2. Kaikki ydintiedot on tarjottu hakijalle kerrottavaksi. Puuttuvat tiedot on merkitty yhdenmukaisesti. Ei tyhjiä kenttiä tai mallin ohjetekstejä.
3. Kokemusesimerkeissä oma toiminta erottuu muiden työstä. Väitteet ja luvut perustuvat hakijan kertomaan. Toteutunut tulos erottuu ideasta ja tavoitteesta.
4. Teksti on tiivis ja kenttäkohtaiset pituusrajat täyttyvät. Hakijan kirjoitustyyliä ei käytetä osaamisen mittarina.
5. Ei soveltuvuus- tai kulttuuripisteytystä, tarpeettomia henkilötietoja, liikesalaisuuksia tai koko keskusteluhistoriaa.
6. Claude Team -vertailun valinta on kysytty erikseen: Kyllä, Ei tai Ei selvitetty. Älä muuta Ei-vastausta tai täytä suostumusta oletusarvolla.
7. Hakija on nähnyt koko sisällön ja vahvistanut sen. Vahvistusta ei saa merkitä saaduksi ilman vastausta. Korjattuasi merkittävästi sisältöä pyydä uusi tarkastus.
8. Tiedoston nimi on hakijan ilmoittama `Etunimi Sukunimi.md`. Nimessä ja otsikossa käytetään hakijan oikeaa ilmoitettua nimeä, ei mallin sanaa Omanimi.

Jos hakija haluaa lisätä henkilötiedot itse, jätä kyseisiin kohtiin Ei selvitetty ja kerro täsmällisesti, mitkä kentät on lisättävä ennen lähettämistä. Älä väitä täysin lähetysvalmiiksi tiedostoa, jonka nimi tai yhteystiedot vielä puuttuvat. Hakijan ei tarvitse antaa tietoja tekoälypalvelulle voidakseen täydentää tiedoston paikallisesti.

## Muodosta tiedosto

Anna mahdollisuuksien mukaan ladattava UTF-8 Markdown-tiedosto. Jos ympäristö ei tue tiedostoja, näytä koko lopullinen hakemus yhtenä Markdown-koodilohkona. Ohjeista kopioimaan vain lohkon sisältö tekstieditoriin ja tallentamaan UTF-8-muodossa nimellä `Etunimi Sukunimi.md`, ilman ylimääräistä `.txt`-päätettä. Tiedoston sisältö alkaa hakemuksen pääotsikosta, ei mallin täyttöohjeesta tai koodiaidoista.

Älä tallenna hakemusta tämän repon versionhallintaan. Älä lisää sitä issueen, pull requestiin tai muuhun julkiseen keskusteluun. Älä vaadi hakijalta GitHub-tunnusta, commitia, forkkausta tai Git-komentoja.

## Selvitä lähetysmahdollisuus

Kun hakija on tarkastanut hakemuksen, saanut mahdollisuuden korjata sen ja vahvistanut sisällön, selvitä onko hänellä tähän tekoälypalveluun liitetty oma sähköposti ja onko sinulla käytettävissä toiminto, joka voi lähettää sähköpostin **MD-tiedoston liitteenä**. Käytä vain kyseisen palvelun näyttämiä, sallittuja toimintoja; älä oleta yhteyden tai liitetuen olemassaoloa, jos et voi varmistaa niitä. Kysy hakijalta tarvittaessa, haluaako hän käyttää liitettyä sähköpostiaan vai lähettää tiedoston itse.

Hakijan ei tarvitse liittää sähköpostiaan, antaa salasanaa tai myöntää uusia oikeuksia. Jos yhteyttä, lähetysoikeutta tai liitetukea ei ole, jos hakija ei halua käyttää sitä tai jos asia jää epäselväksi, käytä alla olevaa itse lähettämisen polkua. Jos hakijan nimi tai yhteystiedot puuttuvat, anna hänen täydentää ne ennen lähetyksen valmistelua; älä lähetä keskeneräistä tiedostoa.

## Lähetys hakijan sähköpostiyhteydellä

1. Luo tarkastetusta ja hakijan hyväksymästä sisällöstä UTF-8-tiedosto `Etunimi Sukunimi.md`. Varmista, että sähköpostitoiminto pystyy liittämään juuri tämän valmiin tiedoston. Älä korvaa liitettä pelkällä tekstillä, linkillä tai keskustelulokilla.
2. Näytä hakijalle tarkastettavaksi lähettäjätili, vastaanottaja **pasi.huumarsalo@cleor.fi**, otsikko `Työhakemus Tuotepäällikkö Etunimi Sukunimi`, lyhyt asiallinen viestiteksti ja liitetiedoston nimi. Käytä hakijan ilmoittamaa oikeaa nimeä. Viestiteksti voi esimerkiksi kertoa, että hakemus on liitteenä; älä lisää siihen keksittyjä tietoja.
3. Pyydä **erillinen, nimenomainen vahvistus juuri tämän viestin lähettämiselle** vasta sen jälkeen, kun hakija on nähnyt nämä tiedot ja hyväksynyt hakemuksen sisällön. Sisällön vahvistus, Claude Team -vertailun suostumus tai yleinen kiinnostus hakemiseen ei ole lähetyslupa. Jos hakija muuttaa vastaanottajaa, viestiä tai liitettä, näytä päivitetyt tiedot ja pyydä uusi vahvistus.
4. Lähetä vasta vahvistuksen jälkeen ja vain jos käytettävissä oleva sähköpostitoiminto sallii kyseisen liitteen lähettämisen käyttäjän tililtä. Noudata palvelun ja työkalun mahdollisia omia hyväksyntä- ja käyttösääntöjä. Jos käyttäjä ei vahvista, älä lähetä.
5. Tarkista lähetyksen tulos työkalun palautteesta. Kerro ”hakemus lähetetty” vain, kun työkalu vahvistaa lähetyksen onnistuneen. Jos vain luonnos syntyi, kerro sen olevan luonnos ja että hakemusta ei ole vielä lähetetty.
6. Jos lähetys tai liitteen lisääminen ei onnistu, kerro mitä tapahtui ja anna itse lähettämisen ohjeet. Jos tulos on epäselvä, älä väitä lähetystä onnistuneeksi tai epäonnistuneeksi äläkä lähetä uudelleen automaattisesti: kehota hakijaa ensin tarkistamaan Lähetetyt-kansio ja mahdollinen liite, jotta vältetään kaksoislähetys.

## Hakija lähettää tiedoston itse

Anna latauslinkki tiedostoon, jos sellainen on käytettävissä. Jos tiedostoa ei voida luoda, anna koko hakemus yhtenä kopioitavana Markdown-koodilohkona ja neuvo tallentamaan lohkon sisältö UTF-8-muodossa nimellä `Etunimi Sukunimi.md`, ilman `.txt`-päätettä. Anna selkeä käytännön ohje liittää tallennettu MD-tiedosto sähköpostiin.

Näytä seuraavat tiedot ja korvaa nimipaikat hakijan nimellä, jos se on tiedossa:

- **Vastaanottaja:** pasi.huumarsalo@cleor.fi
- **Sähköpostin otsikko:** `Työhakemus Tuotepäällikkö Etunimi Sukunimi`
- **Liite:** `Etunimi Sukunimi.md`
- **Hakuaika:** 22.11.2026 mennessä.
- **Jatkosta:** yhteydenottoja voi odottaa marraskuun 2026 lopussa.
- **Lisätiedot:** Pasi Huumarsalo, sama sähköposti, 040 739 5789.

Sano selvästi: **Hakemustasi ei ole vielä lähetetty. Tallenna tarkastamasi MD-tiedosto ja lähetä se itse sähköpostin liitteenä yllä olevaan osoitteeseen. Hakeminen tapahtuu lähettämällä tiedosto.**

Saateviesti saa olla lyhyt; erillistä vapaamuotoista hakemusta, CV:tä tai koetehtävää ei edellytetä tämän aineiston perusteella. Jos määräpäivä on jo mennyt, älä väitä hakua avoimeksi tai suljetuksi varmistamatta: ohjaa kysymään ajankohtainen tilanne Pasille.
