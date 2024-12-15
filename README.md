A Palack osztály reprezentálja az általános palackokat az alkalmazásunkban.
A palackokról az alábbi adatokat tároljuk:

- a benne lévő ital ( ital néven)
- maximális űrtartalom milliliterben ( max_urtartalom néven)
- jelenleg benne lévő ital mennyisége milliliterben ( _jelenlegi_urtartalom néven)

Készíts inicializáló függvényt, ami a fenti sorrendben várja az adatokat. A jelenlegi
űrtartalom legyen opcionális, ha nem adjuk meg, akkor 1 legyen az értéke. A függvény a
paraméterek alapján állítsa be az adattagokat.

Készíts propertyt a _jelenlegi_urtartalom adattaghoz, jelenlegi_urtartalom néven. A
getter adja vissza az adattag értékét, a setter pedig az alábbiak szerint működjön:
amennyiben a beállítani kívánt űrtartalom több, mint a palack űrtartalma, úgy a
_jelenlegi_urtartalom értéket a palack maximális űrtartalmára állítsa be.
minden más esetben állítsa be a jelenlegi űrtartalmat a paraméterből érkezőre.
amennyiben 0-ra állítjuk be a jelenleg benne lévő ital mennyiségét, úgy az ital adattag
értékét állítsa be a függvény None -ra.

Készítsd el a suly függvényt, ami nem vár paramétert. A függvény térjen vissza a palack súlyával.
A palack súlya: maximális űrtartalom/35 + jelenleg benne lévő ital súlya (ami
megegyezik az űrtartalommal).

Készítsd el a szöveggé alakító függvényt, ami térjen vissza az alábbi formátumú szöveggel:
"Palack, benne levo ital: {ital neve}, jelenleg {jelenlegi űrtartalom} ml van
benne, maximum {max űrtartalom} ml fer bele."

Készítsd el az egyenlőségvizsgáló függvényt is. Két palack akkor egyenlő, ha mindegyik adattaguk
megegyezik.

Készítsd el a += operátort megvalósító függvényt is ( __iadd__ ). Ezzel egy palack tartalmát
lehessen hozzáadni az aktuális palackhoz. Ez a függvény a következőképp működjön:
A jelenlegi űrtartalomhoz adja hozzá a másik palackban található ital jelenlegi űrtartalmát.
Természetesen ne engedje, hogy többet töltsünk bele, mint amennyi belefér az adott
palackba (ehhez használd a már elkészített property függvényt).
Amennyiben a két ital megegyezik (egy narancsléhez narancslevelt adunk), akkor az
operátor ne csináljon semmit az ital adattaggal.
Amennyiben a két ital nem egyezik meg, az elkészült finomság neve legyen keverek ,
abban az esetben, ha mindkét palackban volt valamilyen ital. Amennyiben a jelenlegi palack
üres volt, a másik palackban lévő ital neve kerüljön az ital adattagba. Feltehetjük, hogy
üres palackból sosem szeretnénk beleönteni a saját palackunkba (tehát a paraméterben lévő
palack ital adattag sosem None)

Készítsd el a VisszavalthatoPalack osztályt, ami egy speciális palackfajta.
A visszaváltható palackokról az alábbi adatot tároljuk a palack adatain felül:
palackdíj Forintban ( palackdij néven)

Készíts inicializáló függvényt, ami az ősosztály inicializálásához szükséges paraméterek után
várja a palackdíjat. A palackdíj szintén opcionális, ha nem adjuk meg, akkor legyen 25 Ft. A
függvény állítsa be az adattagokat (az ősosztály megfelelő metódusának meghívásával, valamint a
palackdíj beállításával).

Készítsd el a szöveggé alakító függvényt, ami használja fel a Palack azonos függvényét, azonban
írja be elé, hogy "Visszavalthato", a megfelelő formátum tehát:

"VisszavalthatoPalack, benne levo ital: {ital neve}, jelenleg {jelenlegi
űrtartalom} ml van benne, maximum {max űrtartalom} ml fer bele."

Készítsd el a Rekesz osztályt.
A rekeszekről az alábbi adatokat tároljuk:
- maximális teherbírás ( max_teherbiras néven)
- a tárolt palackokat ( palackok néven)

Készíts inicializáló függvényt, ami csak a maximális teherbírást várja, a palackok adattagot
pedig egy üres listával inicializálja.

Készítsd el a suly nevű függvényt, ami nem vár paramétert. A függvény térjen vissza a rekeszben
tárolt palackok összsúlyával. Amennyiben nincs benne palack, térjen vissza 0-val.

Készítsd el a uj_palack nevű függvényt, ami egy palackot vár paraméterként. A függvény
számolja ki, hogy ha beletennénk a paraméterben érkező palackot a rekeszbe, akkor azt elbírná-e
a rekesz. Amennyiben nem bírná el, ne csináljunk semmit; ellenkező esetben pedig tegyük be a
palackok közé a paraméterben érkező palackot.

Készítsd el a osszes_penz nevű függvényt, ami nem vár paramétert. A függvény számolja ki, hogy
mennyi pénzt kapunk, ha visszaváltjuk a rekeszben lévő összes palackot (tehát adjuk össze a
palackdíjakat). Ügyeljünk rá, hogy a sima Palack példányoknak nincs palackdij adattagjuk!
