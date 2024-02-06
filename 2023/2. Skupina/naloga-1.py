"""
Imamo n stolov v vrsti in n oseb; oboji so oštevilčeni od 1 do n (velja n ≤ 1000). Osebe bi se rade druga za drugo posedle na stole. 
O vsaki osebi vemo, na kateri stol bi se najraje usedla (oseba i na stol Si), poznamo pa tudi njihove želje v primeru, da je ta stol že zaseden. 
Če je želeni stol že zaseden, se oseba poskuša usesti na najbližji stol, ki ustreza tem zahtevam. 
Nekatere osebe so se pripravljene premakniti levo od stola, nekatere pa desno od stola. 

Ker bodo tisti, ki se niso uspeli usesti na želeni stol, slabe volje, imamo za vsako osebo i podano tudi število Ri (ki je večje ali enako 0), ki pove, 
koliko mest levo in desno od njenega novega sedišča v trenutku, ko se bo usedla, ne sme biti nikogar, 
da ne bo ta zlovoljna oseba širila negativne energije (oseba, ki se ni mogla usesti na želeni stol, se torej v izbrano smer premika tako daleč, 
dokler ni v njeni okolici dovolj prostih stolov). Tisti, ki ne morejo zasesti nobenega stola po svojih željah, v jezi odkorakajo domov in ne zasedejo nobenega stola.
Napiši program, ki ugotovi, kakšna je končna razporeditev ljudi na stole. Podatke o osebah naj prebere s standardnega vhoda. 
V prvi vrstici dobi število oseb n. Sledi n vrstic, za vsako osebo po ena; v i-ti od teh vrstic so s presledkom ločena števila Si, Ri ter črka L ali D, 
ki predstavlja smer, v katero se želi oseba i premakniti, če je njen želeni stol Si že zaseden.
Tvoj program naj izpiše n s presledkom ločenih števil, kjer i-to i-ti stol. Če na stolu ni nikogar, izpiši 0, sicer pa številko osebe (od njem.

Primer: recimo, da imamo 8 stolov; naslednja tabela kaže, kako bi osebe posedle na prve tri, če bi imele takšne želje, kot je navedeno v levem delu tabele.
število predstavlja 1 do n)


oseba | stol | razmik | smer | Stanje stolov po 
  i   |  Si  |   Ri   |      | prihodu te osebe
------+------+--------+------+------------------
      |    začetno stanje -> |  0 0 0 0 0 0 0 0
  1   |  5       7       L   |  0 0 0 0 1 0 0 0
  2   |  5       3       L   |  2 0 0 0 1 0 0 0
  3   |  5       1       L   |  2 0 3 0 1 0 0 0

"""

# ! Navodila naloge so delno zapisane, saj je naloga kopirana iz .pdf dokumenta ki text narobe interpretira !
# ! Priporočeno je da si preberete navodila v samem .pdf dokumentu tekomvanj 2. skupine leta 2023.          !

##############################################################################################################
# V tej nalogi prikažemo način reševanja naloge in identični izpis končnega rezultata kot je v primeru naloge.

# Naloga je seveda rešljiva brez podprogramov, ampak je z uporabo podprogramov bolj pregledna in razumljiva.
# Glavno razvrščanje oseb je v funkciji main(), kjer se uporabljajo podatki, ki so definirani v nalogi.
# koncni_izpis in listToString pa sta posebej podprograma da lažje razdelimo in je razlaga bolj jasna.
##############################################################################################################

def main():

    vhod_stevilo = 3 # Vhodni podatki, ki so definirani v nalogi. Drugače se naredi z input()
    vhod_stoli = 8   # Vhodni podatki, ki so definirani v nalogi. Drugače se naredi z input()
    vhod_osebe = [   # Vhodni podatki, ki so definirani v nalogi. Drugače se naredi z input()
        [5, 7, "L"],
        [5, 3, "L"],
        [5, 1, "L"]
    ]

    stoli = [0] * vhod_stoli # Naredimo seznam stolov, ki je dolžine vhod_stoli, ter ga napolnimo z ničlami.
    stoli[vhod_osebe[0][0] - 1] = 1 # Nastavimo prvi stol na 1, saj se oseba 1 želi usesti na stol 5 in ni nikogar na nobenem stolu.

    print("Oseba 1 se je usedla na stol " + str(vhod_osebe[0][0]) + ".") # Izpišemo lahko že za prvo osebo saj vedno dobi svoj stol, saj še nobene druge osebe ni.

    for i in range(1, vhod_stevilo, 1): # Naredimo loop ki gre skozi vsako osebo v vhodnih podatkih.
        razmik = 0 # inicializiramo spremenljivko z katero lahko preverjamo razmik med osebami
        ni_osebe = True # inicializiramo spremenljivko z katero preverimo če je sploh kakšna oseba že prisotna.
                        # pride v poštev če v zgornjem delu programa ne dodelimo prve osebe avtomatsko na željen stol
        
        ciljni_stol = vhod_osebe[i][0] - 1 # prvotno je ciljni stol tisti, ki je zaželjen

        if (vhod_osebe[i][2] == "L"): # izvede se če se oseba želi premikati v levo (podobna stvar za desno stran na liniji 75)
            for j in range(vhod_osebe[i][0] - 1, 0, -1): # Prvotno se postavimo na stol kateri je željen ter se premikamo v levo po seznamu stolov
                if (stoli[j] != 0): # če se je enden od stolov zaseden, se razmik resetira in zabeleži da so osebe prisotne
                    ni_osebe = False
                    razmik = 0
                else:
                    if razmik == vhod_osebe[i][1]: # če ke zamik zadosten zahtevam, prekinemo loop
                        break
                    razmik += 1 # v tem primeru že vemo da na trenutnem sedežu ni nikogar, zato razmik povečamo za 1
                    if not ni_osebe: # v primeru da trenutno ni osebe, se avtomatsko zabeleži trenutni stol kot opcija
                        ciljni_stol = j

        else: # vhod_osebe[i][2] == "D"
            for j in range(vhod_osebe[i][0] - 1, vhod_stoli, 1): # pristop je v tem delu zelo podoben, razen da se tukaj pomikamo desno po seznamu
                if (stoli[j] != 0):
                    ni_osebe = False
                    razmik = 0
                else:
                    if razmik == vhod_osebe[i][1]:
                        break
                    razmik += 1
                    if not ni_osebe:
                        ciljni_stol = j

        
        if (ni_osebe or razmik == vhod_osebe[i][1]): # to se izvede v primeru če ni oseb, ali pa če je razmik zadosten
            stoli[ciljni_stol - 1] = i + 1 # zabeleži se kjer se je oseba vsedla na stol
            print("Oseba " + str(i + 1) + " se je usedla na stol " + str(ciljni_stol) + ".") # izpis da se je oseba vsedla
        else:
            print("Oseba " + str(i + 1) + " je odšla domov.") # v primeru da ni bil nobeden stol zadosten kriterijem, oseba odide

        

    print(stoli) # izpis končnega sedežnega reda

    koncni_izpis(stoli, vhod_osebe) # kličemo podprogram za podroben izpis kako se je stopnjevalo.


def koncni_izpis(stoli, vhod_osebe):
    print("\n\nKoncni izpis:\n") # naslednjih 5 printov je statičnih tako da jih lahko že kar izpišemo
    print("oseba | stol | razmik | smer | Stanje stolov po ")
    print("  i   |  Si  |   Ri   |      | prihodu te osebe ")
    print("------+------+--------+------+------------------")
    print("      |    začetno stanje -> |  0 0 0 0 0 0 0 0 ")
    
    printable_stoli = [0] * len(stoli) # naredimo nov seznam katerega bomo sproti spreminjali za pravilen izpis. Dolžina je odvisna od število stolov
    for i in range(1, len(vhod_osebe) + 1, 1): # naredimo loop od 1 do zastavljenega števila oseb
        printable_stoli[stoli.index(i)] = i # poiščemo število v končnem sedežnem redu, ter ga zastavimo v naš nov seznam ter ga takoj izpišemo
                                            # razlog takšnega pristopa je da izpisujemo po vrsti. Primer:
                                            # npr i = 1, v seznamu stoli pošičemo kjer je oseba 1, jo na isto mesto zapišemo v novem seznamu, izpišemo, potem pa naredimo isto z i = 2
        # print(printable_stoli)
        print("  " + str(i) + "   |  " + str(vhod_osebe[i-1][0]) + "       " + str(vhod_osebe[i-1][1]) + "       " + vhod_osebe[i-1][2] + "   | " + str(listToString(printable_stoli)))
    
    print("\n\n")


def listToString(list): # ta podprogram služi da spremenimo zapis seznama
                        # V primeru da tega nimamo, zgleda seznam kot string tako: [2, 0, 3, 0, 1, 0, 0, 0]
                        # Z podprogramom pa potem zgleda tako: 2 0 3 0 1 0 0 0
    str1 = ""
    for ele in list: # vsako število v seznamu spremenimo v string, dodamo presledek ter ponavljamo
        str1 += " " + str(ele)
    return str1

main()