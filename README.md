# tsoha-chat
/ ZohaChat

Kun käynnistät sovelluksen ensimmäisen kerran, keskustelualueet ovat tyhjiä. Rekisteröidy painamalla "Kirjaudu sisään" linkkiä
ja "Luo uusi tunnus" linkkiä painamalla pääset rekisteröitymään. Valitse rooliksi ylläpitäjä, jotta pääset luomaan ja poistamaan keskustelualueita.
Keskustelualueita voit poistaa klikkaamalla "Keskustelualueet" linkkiä. (Ylläpitäjänä)
Tämän jälkeen voit luoda keskusteluketjuja ylläpitäjänä tai käyttäjänä. Käyttäjä voi muokata tai poistaa omia viestejään.
Ketjuissa näkyy kyseisen ketjun viestien määrä.
Hakukentästä voi etsiä viestejä niiden sisällön perusteella ja tuloksena näkyy kaikki viestit, lähettäjä, ajankohta ja viestien määrä.
Ulkoasua on paranneltu viimeistä palautusta varten ja siihen on lisätty logo, joka näytti paremmalta kun sovelluksen nimen muutti ZohaChatiksi.
Varmuuden vuoksi en muuttanut sitä gittiin, jotta palautuksen kanssa ei tulisi ongelmia. Ulkoasussa on käytetty bootstrappia hyödyksi, jonka
takia sovelluksen käyttäminen vaatii nettiyhteyttä vaikka sitä käyttäisikin paikallisesti. Tietoturvaa parantelin vielä CSRF-haavoittuvuuden osalta.
Ajan loppumisen takia ajattelin, että tärkeintä olisi estää haavoittuvuus rekisteröinnin ja kirjautumisen osalta, muuten olisin lisännyt sen jokaiseen
lomakkeeseen. Lisäsin sovellukseen mahdollisuuden antaa palautetta. Vain ylläpitäjä pystyy näkemään palautteet. Navigointia sovelluksessa on
paranneltu niin, että jokaiselta sivulla on "Etusivulle", "Takaisin", "Kirjaudu sisään/ulos", "Keskustelualueet" ja "Anna palautetta".
Ylläpitäjällä on vielä "Luo uusi keskustelualue" painike.


Sovelluksen lopullinen tilanne:

  * Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen. Rooliksi voi valita käyttäjä tai ylläpitäjä.
  * Käyttäjä näkee sovelluksen etusivulla listan alueista sekä listan ketjuista, joissa linkki kyseisiin alueisiin ja ketjuihin.   
  * Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon.
  * Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
  * Käyttäjä voi muokata lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa viestin.
  * Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
  * Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
  * Käyttäjä voi antaa palautetta. Ylläpitäjä näkee samalta sivulta listan palautteista.



Ohjeet sovelluksen käynnistykseen:

  Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

    DATABASE_URL=<tietokannan-paikallinen-osoite>
    SECRET_KEY=<salainen-avain>

  Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r ./requirements.txt

  Määritä vielä tietokannan skeema komennolla:

    $ psql < schema.sql

  Nyt voit käynnistää sovelluksen komennolla:

    $ flask run
