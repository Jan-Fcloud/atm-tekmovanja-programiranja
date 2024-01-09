"""
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
"""

################################################
# Naslednja rešitev je narejena z vnosom citata.
################################################

import random # uvozimo knjižnico random, katero bomo uporabljali za naključno generiranje.

def zmesaj_crke(citat): # definiramo funkcijo ki jo bomo klicali ter ji bomo podali citat
    besede = citat.split() # razdelimo celoten citat v več besed
    stevec = 0 # definiramo števec, z katerim lahko razberemo v kateri besedi smo

    for beseda in besede: # uporabimo for zanko, da gremo čez vsako besedo posebej
        beseda = list(beseda) # pretvorimo besedo v array, da lahko uporabljamo indexe in zamenjujemo črke

        for i in range(len(beseda)): # uporabimo še eno for zanko, da gremo čez vsako črko v besedi posebej
            index_1 = i # definiramo index_1, ki je enak trenutnemu indexu crke
            index_2 = random.randint(0, len(beseda) - 1) # definiramo index_2, ki je naključno generiran med 0 in dolžino besede - 1

            if beseda[index_1].isalpha() and beseda[index_2].isalpha(): # preverimo če sta obe črki res črki z funkcijo .isalpha()
                temp = beseda[index_1] # definiramo temp, ki začasno drži prvo črko da je ne zgubimo med menjavo

                beseda[index_1] = beseda[index_2] # prvo črko menjamo z drugo
                beseda[index_2] = temp # drugo črko zamenjamo z prvo ki smo jo predčasno shranili v temp
        besede[stevec] = "".join(beseda) # združimo črke nazaj v string

        stevec += 1 # Stevec povecamo za 1 da povemo programu da gremo na naslednjo besedo

    return " ".join(besede) # vrnemo zdruzene besede (besede je array, zato uporabimo join() da jih združimo v string)


def main():
    citat = input("Vnesi citat: ")
    print(zmesaj_crke(citat))

main() # kličemo funkcijo main() da se program zažene