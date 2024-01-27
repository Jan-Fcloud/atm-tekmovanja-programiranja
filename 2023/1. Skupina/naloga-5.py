"""
Na eni od imenitnejših srednjih šol v Ljubljani so se odločili, da bi v telovadnico želeli postaviti velik zaslon, 
na katerem bi predvajali reklame in druga sporočila, podobno kot vidimo pri športnih tekmovanjih. 
Ker nimajo denarja za nakup novih, so iz računalniške učilnice nabrali stare, še delujoče računalniške zaslone in jim dodali poceni računalnike, 
ki krmilijo zaslon in se pogovarjajo z nadzornim računalnikom. Zaslone so pritrdili ob rob telovadnice, pokonci, drugega zraven drugega. 
Nadzorni računalnik bo celotno sliko „razrezal“ in dele pošiljal na ustrezni zaslon. 

Primer:
----------- ----------- ----------- ----------- -----------
|         | |         | |         | |         | |         |
|         | |         | |         | |         | |         |
|         | |         | |         | |         | |         |
|         | |         | |         | |         | |         |
|         | |         | |         | |         | |         |
|         | |         | |         | |         | |         |
----------- ----------- ----------- ----------- -----------
Zaslon 140   Zaslon 378   Zaslon 52   Zaslon 6   Zaslon 839

Seveda za ta podvig potrebujejo računalniški krožek. Tam so napisali program, 
i na po- sameznem zaslonu ugotovi oba sosednja zaslona in to sporoči nadzornemu računalniku. 
Te podatke dobiš kot zaporedje trojic števil, kjer drugo število pove številko zaslona, 
ki sporoča to trojico, prvo število je številka njegovega levega soseda (ali −1, če levega so- seda sploh ni), 
tretje število pa je številka njegovega desnega soseda (ali −1, če desnega soseda sploh ni). 
Te trojice so navedene v nekem naključnem vrstnem redu, kot kaže naslednji primer za zgornjo sliko:

378 52  6
6   839 -1
52  6   839
-1  140 378
140 378 52

Napiši program, ki iz teh podatkov ugotovi vrstni red zaslonov. Številke zaslonov so naravna števila z območja od 1 do 1000, 
vendar ne nujno točno od 1 do števila zaslonov (kar vidimo tudi na gornjem primeru). 
Podatke lahko tvoj program bere s standardnega vhoda ali pa iz datoteke vhod.txt (karkoli ti je lažje). 
(Pozor: čeprav je v primeru zgoraj pet zaslonov, naj tvoja rešitev deluje tudi za primere z več ali manj kot petimi zasloni.)
Mogoče je tudi, da v vhodnih podatkih manjka vrstica za kakšen zaslon; v tem primeru naj tvoj program izpiše sporočilo o napaki.
"""

#######################################################################################################################################
# V naslednji rešitvi uporabimo slovarje, ter sklepamo da je vnos podatkov pravilen brez napak, oz. brez manjkajočih podatkov/zaslonov.
# Sledeča rešitev uporablja samo eno funkcijo, ki je definirana na vrhu, ter se kliče v for zanki.
#
# Vhod je v našem primeru vnaprej definiran, vendar bi lahko uporabili tudi funkcijo input(), ki bi nam omogočila vnos podatkov.
# Določeno je v naprej, da se pokaže pravilna rešitev z podatki podani v primeru naloge.
#
# Na koncu programa se tudi pojavi nov "expression", ki je ** (double asterisk). Uporaba dovjnih zvezdic je več za več namenov.
# V našem primeru ko se uporablja z slovarji, nam "razpakira" slovar, ter nam omogoči da združimo dva slovarja v enega.
# Zato lahko tudi preskočimo pisanje loopa, ki bi nam to drugače združil.
#######################################################################################################################################


def naslednjiZaslon(slovar, trenutniZaslon): # Definiramo funkcijo, kateri podamo slovar vseh zaslonov, ter trenutni zaslon z katerim delamo v glavnem programu.
    
    for i in slovar: # Za vsak zaslon v slovarju preverimo če je trenutni zaslon enak levemu zaslonu, če je, vrnemo trenutni zaslon saj nam to pove da delamo z naslednjim.
                     # Npr: trenutni zaslon je 378. Z loopom najdemo v slovarju zaslon 378 ki je definiran kot levi zaslon zaslona 52
                     # V slovarju zgleda tako:
                     # Trenutni zaslon ->   378: { "levo": 140, "desno": 52 }
                     # Naslednji zaslon ->  52:  { "levo": 378, "desno": 6 }
        
        if (slovar[i]["levo"] == trenutniZaslon): # Z if stavkom preverimo zgornji opisani postopek.
            return {i: slovar[i]} # Vrnemo slovar z naslednjim zaslonom, ki ga bomo dodali v seznam razvrstitev.
        

def main():
    vhod = [ # Vhodni podatki, ki so definirani v nalogi.
        [378, 52, 6],
        [6, 839, -1],
        [52, 6, 839],
        [-1, 140, 378],
        [140, 378, 52]
    ]

    # Izpis vhodnih podatkov:
    # (Ni del naloge, ampak je za nas uporabno za preverjanje pravilnosti vhodnih podatkov)
    print("Vhodni podatki:")
    for i in vhod:
        print(i)

    slovar = {} # definiramo prazen slovar, ki bo vseboval vse zaslone, ter njihove leve in desne sosede.

    for i in vhod: # Za vsako vrstico v vhodnih podatkih, dodamo v slovar zaslon, ter njegove leve in desne sosede.
                   # To je potrebno saj imamo vse podatke trenutno v arrayu.
        slovar[i[1]] = { 
            "levo": i[0],
            "desno": i[2]
        } # Podatki so najprej v taksni obliki: [378, 52, 6]. Z zgornjim loopom jih spremenimo v slovar, ki zgleda tako: 52: { "levo": 378, "desno": 6 }
          # Dobro je ponovit da se array zažne z indexom 0, kar pomeni da prva vrednost v array na 0. mestu je 378, druga na 1. mestu 52, tretja pa na 2. mestu, ki je 6.
          # če je i = [378, 52, 6]:
          # i[0] -> 378
          # i[1] -> 52
          # i[2] -> 6

    # Izpis trenutnega slovarja ki še ni razvrščen (samo za preglednost) ter definiramo prvi zaslon:
    print("\nSlovar:")
    for i in slovar:
        print(i, slovar[i])

        if (slovar[i]["levo"] == -1): # Poiscemo prvi zaslon:
            prvi = {i: slovar[i]}
        # Zlahka najdemo prvi zaslon, saj vemo da če je sosed definiran kot -1, pomeni da ne obstaja. Zato poišemo zaslon od kerega je levi sosed -1.

    razvrstitev = {} # Definiramo slovar, ki bo vseboval razvrstitev zaslonov.
    razvrstitev = prvi # V slovar dodamo prvi zaslon ki smo ga prej našli.

    while len(razvrstitev) != len(slovar): # Loop se nam izvaja tako dolgo dokler se dolžina/velikost razvrščenega slovarja ne ujema z originalnim.
        for i in razvrstitev: # Zanka gre skozi slovar keremu trenutno dodajamo razvrscene vrednosti
            naslednjiReturn = naslednjiZaslon(slovar, i) # Shranimo vrnjeno vrednost od klicane funkcije ki ji podamo celoten nerazvrščen slovar in najnovejši dodan zaslon iz razvrščenega (razlaga funkcije je zgoraj)
            razvrstitev = {**razvrstitev, **naslednjiReturn} # razvrščen slovar združimo z naslednjim tako da oba razpakiramo.

            
    print("\nRazvrstitev:") # Izpišemo razvrščene zaslone da potrdimo če je prav.
    for i in razvrstitev:
        print(i)


main() # Klic main() da začnemo program