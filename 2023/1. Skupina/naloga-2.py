"""

Velikost datotek ali pomnilnika običajno merimo v bajtih (B), pri zapisu večjih vrednosti
pa si naredimo število preglednejše oz. lažje razumljivo tako, da uporabimo multiplikativne predpone K (kilo-), M (mega-), G (giga-) itd. Tako predstavlja en kilobajt 1024
bajtov (1 KB = 1024 B), megabajt je 1024 kilobajtov (1 MB = 1024 KB) in tako naprej, vsaka naslednja predpona (kot jih določa in poimenuje npr. industrijski standard
jedec) je za faktor 1024 večja od prejšnje. Te predpone po vrsti so: K, M, G, T, P (za
naš namen se ustavimo pri P, čeprav obstajajo tudi višje).

Napiši podprogram (oz. funkcijo), ki bo dobil kot argument velikost neke datoteke
v bajtih kot nenegativno celo število, potem pa izpisal to vrednost, po potrebi okrajšano
z uporabo najnižje možne predpone tako, da število števk zapisa ne bo večje kot štiri.
Če je število tako veliko, da zanj uporabimo najvišjo predpono, potem za tak primer
omejitev na štiri števke ne velja.

Če ti je lažje, lahko namesto podprograma napišeš program, ki naj prebere število
iz vhodne datoteke ali s standardnega vhoda.
Izpišemo vedno le celi del (brez morebitnih decimalk), temu naj sledi črka B (= bajt),
pred katero naj po potrebi stoji črka predpone.

Če število bajtov ni mnogokratnik vrednosti predpone (in bi pri deljenju ostale decimalke), zaokrožimo število navzgor, npr. 234,03 KB izpišemo kot 235 KB, 234,00 KB
pa kot 234 KB.
Za potrebe te naloge lahko predpostaviš, da imajo številski podatkovni tipi tvojega
programskega jezika neomejen obseg in natančnost.

Primeri:

| podatek   | izpis    |
| 0         | 0 B      |
| 5678      | 5678 B   |
| 2097152   | 2048 KB  |
| 2097153   | 2049 KB  |
| 12897500  | 13 MB    |
| 128975000 | 124 MB   |

"""