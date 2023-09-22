# tsoha-chat
Keskustelusovellus


Sovelluksen nykyinen tilanne:

  * Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
  * Rekisteröinnin aikana käyttäjä voi valita roolin: käyttäjä tai ylläpitäjä. (valinnalla ei ole vielä toiminnallisuutta)
  * Käyttäjä näkee sovelluksen etusivulla listan lähetetyistä viesteistä ja lähetetyn viestin ajankohdan.
  * Käyttäjä voi luoda viestin, jolla on otsikko.
  * Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.


Lopullisessa sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

Sovelluksen ominaisuuksia:

  * Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
  * Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
  * Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
  * Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
  * Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa ketjun tai viestin.
  * Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
  * Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
  * Ylläpitäjä voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle.

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
