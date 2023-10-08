# tsoha-chat
Keskustelusovellus

Kun käynnistät sovelluksen ensimmäisen kerran, keskustelualueet ovat tyhjiä. Rekisteröidy painamalla "Kirjaudu sisään" linkkiä
ja "tästä" linkkiä painamalla pääset rekisteröitymään. Valitse rooliksi ylläpitäjä, jotta pääset luomaan ja poistamaan keskustelualueita.
Keskustelualueita voit poistaa klikkaamalla "Keskustelualueet" linkkiä. (Ylläpitäjänä)
Tämän jälkeen voit luoda keskusteluketjuja ylläpitäjänä tai käyttäjänä. Käyttäjä voi muokata tai poistaa omia viestejään.
Ketjuissa näkyy kyseisen ketjun viestien määrä.
Hakukentästä voi etsiä viestejä niiden sisällön perusteella ja tuloksena näkyy kaikki viestit, lähettäjä, ajankohta ja viestien määrä.

Tarkoituksena olisi vielä:
Muokata sovelluksen ulkoasua, parantaa tietoturvaa ja rajoituksia. Etusivulle ketjujen viimeisimpiä viestien tietoja.
Koodin rakennetta parannella. Poistaa turhia osia koodista.


Sovelluksen nykyinen tilanne:

  * Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen. Rooliksi voi valita käyttäjä tai ylläpitäjä.
  * Käyttäjä näkee sovelluksen etusivulla listan alueista sekä listan ketjuista, joissa linkki kyseisiin alueisiin ja ketjuihin.   
  * Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon.
  * Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
  * Käyttäjä voi muokata lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa viestin.
  * Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
  * Ylläpitäjä voi lisätä ja poistaa keskustelualueita.



Ohjeet sovelluksen käynnistykseen:

  Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

    DATABASE_URL=postgresql+psycopg2://
    SECRET_KEY=c9263473aa2aafd877e412cc0bab808c

  Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r ./requirements.txt

  Määritä vielä tietokannan skeema komennolla:

    $ psql < schema.sql

  Nyt voit käynnistää sovelluksen komennolla:

    $ flask run
