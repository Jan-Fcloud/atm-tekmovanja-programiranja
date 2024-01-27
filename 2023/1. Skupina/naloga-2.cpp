/*
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
*/

#include <iostream>

using namespace std; // da ne pišemo std::cout in std::cin

// Da se ne obadamo z zaporednjem funkcij, jih najprej inicializiramo (deklariramo).
// Funkcije pa lahko pisemo pod main funkcijo brez da nam bo program javljal napake.
int ostanekPlus(float dec);
string izpis(int velikost);

int main(){
    int velikost;

    cout << "Vnesi velikost datoteke v bajtih: ";
    cin >> velikost;

    cout << endl << izpis(velikost) << endl;


    return 0;
}

string izpis(int input){
    int ostanek = 0;
    int velikost = (float)input;

    if (velikost < 10000){
        return to_string(velikost) + " B"; // vsak return uporablja funkcijo to_string(), da pretvori dobljeno stevilo v string ki ga lahko potem združimo z predpono, ter you izpišemo.
    }else{
        ostanek = ostanekPlus(velikost % 1024); // ostanek nam bo v nalogi pomagal zaokrozevat število navzgor, če je ostanek večji od 0.
        velikost /= 1024; // delimo velikost z 1024, da dobimo pravilno vrednost v naslednji predponi, ter ponavbljamo za vsak visji nivo.

        if (velikost < 10000){ // vedno preverjamo ce je stevilo 4 številsko. V primeru da ni, gremo na naslednji nivo.
            return to_string(velikost + ostanek) + " KB";
        }else{
            ostanek = ostanekPlus(velikost % 1024); // klicemo funkcijo ki nam vrne 1 ali 0, odvisno od tega če je ostanek večji od 0.
            velikost /= 1024;

            ///////////////////////////////////////////////////////////////////
            // Vsi zgornji komentarji se nato ponavljajo za vsak nivo predpone.
            ///////////////////////////////////////////////////////////////////

            if (velikost < 10000){
                return to_string(velikost + ostanek) + " MB";
            }else{
                ostanek = ostanekPlus(velikost % 1024);
                velikost /= 1024;

                if (velikost < 10000){
                    return to_string(velikost + ostanek) + " GB";
                }else{
                    ostanek = ostanekPlus(velikost % 1024);
                    velikost /= 1024;

                    if (velikost < 10000){
                        return to_string(velikost + ostanek) + " TB";
                    }else{
                        ostanek = ostanekPlus(velikost % 1024);
                        velikost /= 1024;

                        if (velikost < 10000){
                            return to_string(velikost + ostanek) + " PB";
                        }else{
                            return to_string(velikost + ostanek) + " EB";
                        }
                    }
                }
            }
        }
    }
}

// Uporaba naslednjega podprograma je da se odločimo če bomo pripisali rezultatu 1 ali ne.
// V navodilih naloge je napisano naslednje:

// Če število bajtov ni mnogokratnik vrednosti predpone (in bi pri deljenju ostale decimalke), 
// zaokrožimo število navzgor, npr. 234,03 KB izpišemo kot 235 KB, 234,00 KB pa kot 234 KB.

// Glede tega sklepamo da je pravilno da zaokrožimo navzgor, če je ostanek večji od 0.
// Vrnjen rezultat je seštet k izpisu velikosti v glavnem podprogramu.
int ostanekPlus(float dec){
    if (dec > 0){ // Če je ostanek večji od 0, vrnemo 1, drugače 0.
        return 1;
    }
    else{
        return 0;
    }
}