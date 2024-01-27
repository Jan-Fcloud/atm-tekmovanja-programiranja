/*
Mojca in Peter sta urednika šolskega časopisa. Kot vsak zaupanja vreden časopis mora
tudi šolski časopis imeti rubriko z ugankami. Po pregledu ostalih časopisov sta se Mojca
in Peter odločila, da bosta v šolskem časopisu dijakom v reševanje ponudila „zmešane
citate“. Pri tej vrsti ugank je podan stavek, kjer so črke v posameznih besedah premešane, tako da nimajo nobenega smisla, naloga reševalca pa je, da ugotovi pravilen vrstni
red črk v besedah, ki mu dajo smiseln citat.

Ker se Mojca in Peter ukvarjata z urejanjem šolskega časopisa, ne pa s programiranjem, sta se obrnila nate, ki obiskuješ programerski krožek. Prosita te, da jima napišeš
program, ki bo iz citatov generiral uganke. Tvoj program kot vhod prebere citat (lahko
ga prebere s standardnega vhoda ali iz datoteke vhod.txt, karkoli ti je lažje), izpiše pa
naj „zmešani citat“, v katerem so črke vsake besede naključno premešane, ostali znaki
citata (presledki in ločila) pa ostanejo nespremenjeni. Predpostavi, da je citat dolg največ 100 znakov, da leži v celoti v eni vrstici in da je posamezna beseda sestavljena le iz
črk angleške abecede.
Predpostavi, da je za generiranje naključnih števil na voljo funkcija Random(n), ki
vrne naključno celo število od 0 do n − 1 (pri čemer so vsa števila enako verjetna).

Nekaj primerov:
vhod: Danes je lep, topel dan.
možen izhod: nDsae ej lpe, peotl dan.
vhod: Pes, ki laja, ne grize.
možen izhod: sPe, ik jaal, ne zireg.
vhod: cDdDc cddcdc CCD... cdcdd ddDc? ccddc
možen izhod: cDcdD ddcccd DCC... dddcc Dcdd? cdccd
*/

#include <iostream>

using namespace std; // da ne pišemo std::cout in std::cin

int main()
{
    string citat; // definiramo string v katerega vnesemo citat
    getline(cin, citat); // vnos citata

    int zacetek = 0; // začetek bo vedno na 0 saj je to prvo mesto prvega znaka v citatu
    int konec = 0; // konec je določen na 0 da se inicializira, drugace bi lahko bilo karkoli saj se spremeni v zanki

    for (int i = 0; i < citat.length(); i++) // zanka ki se izvede tolikokrat kot je dolg citat
    {
        if (citat[i] == ' ' || citat[i] == ',' || citat[i] == '.' || citat[i] == '!' || citat[i] == '?') // z tem if-om preverimo kdaj se konča beseda in zabeležimo kje je konec besede v spremnljivko "konec"
        {
            konec = i; // zabeležimo konec besede
            for (int j = zacetek; j < konec; j++) // zanka ki se izvede tolikokrat kot je dolga beseda
            {
                int nakljucno = rand() % (konec - zacetek) + zacetek; // naključno število ki določa naključno pozicijo med zacetkom in koncem besede
                char temp = citat[j]; // začasna spremenljivka ki hrani znak na poziciji j
                citat[j] = citat[nakljucno]; // na pozicijo j zapišemo naključno črko iz besede na poziciji ki je bila prej naključno določena
                citat[nakljucno] = temp; // na pozicijo naključno zapišemo črko ki je bila prej na poziciji j in je bila shranjena v temp
            }
            zacetek = konec + 1; // zacetek besede je enak koncu besede + 1 saj je konec besede presledek ali drug znak
        }
    }

    cout << citat << endl; // izpis razmetanega citata

    return 0;
}