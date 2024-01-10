"""
Od podjetja, ki proizvaja namizne lučke, si dobil nalogo napisati program, ki bo nastavil
lučko na največjo možno svetlost. Vsaka lučka ima več stopenj svetlosti, zaradi varčevanja pa se je podjetje odločilo, da se svetlost krmili z le eno tipko. 
Vsakič ko pritisnemo na tipko, se svetlost poveča, razen če je lučka že na največji svetlosti, v tem primeru
pa se svetlost ponastavi na najnižjo stopnjo. Ker ne vemo, na kateri stopnji je lučka in
koliko stopenj ima, imamo na voljo senzor svetlosti, ki nam pove trenutno svetlost lučke.

Napiši program, ki bo ob koncu delovanja nastavil lučko na največjo možno svetlost.
Na voljo imaš funkciji PritisniTipko() in PreveriSvetlost(). Funkcija PritisniTipko() simulira pritisk na tipko (in ne vrne ničesar), funkcija PreveriSvetlost() pa vrne trenutno
svetlost lučke kot naravno število (za vsako stopnjo svetlosti vedno vrne enako vrednost).
Ti dve funkciji sta že napisani in ju ne implementiraš ti. Za vse točke mora tvoj program
uporabiti čim manj klicev funkcije PritisniTipko().
"""

####################################################################################################################################
# Primer naslednje naloge, je situacija v kateri imamo za nas napisano vse od glavnega programa. Mi moramo samo
# pravilno in efektivno uporabiti rešitev.
#
# Dane funkcije so naslednje:
# - PritisniTipko() -> simulira pritisk na tipko (in ne vrne ničesar)
# - PreveriSvetlost() -> vrne trenutno svetlost lučke kot naravno število (za vsako stopnjo svetlosti vedno vrne enako vrednost)
#
# V nalogi vidimo da ni danih informacij glede zadnje stopnje svetlosti, tako da lahko predpostavimo da jo določimo sami.
# V našem primeru bomo dali zadnjo stopnjo svetlosti na 4. Tako da bo naša lučka imela 4 stopnje svetlosti + stanje izklopa.
#
# Predpostavili bomo tudi da nevemo katera stopnja je zadnja.
####################################################################################################################################

####################################################################################################################################
# Naslednji razred nam bo pomagal pri reševanju naloge saj nimamo programske resitve ki nam bi na tekmovanju bila dana:
# Tega dela programa vi ne rabite pisati, saj je to samo pomoč pri reševanju naloge da si sploh lahko predstavljamo kako bi rešili nalogo.
# Kot rečeno v navodilih, imamo na voljo funkciji PritisniTipko() in PreveriSvetlost() saj so nam že dane.
class Lucka:
    def __init__(self):
        self.svetlost = 0 # začetna svetlost je 0 (izklopljeno)
        self.zadnjaStopnja = 4 # zadnja stopnja svetlosti je 4 (to je naša predpostavka)

    def PritisniTipko(self): # funkcija ki simulira pritisk na tipko
        if self.svetlost < self.zadnjaStopnja:
            self.svetlost += 1
        else:
            self.svetlost = 0

    def PreveriSvetlost(self): # funkcija ki vrne trenutno svetlost lučke kot naravno število
        return self.svetlost
####################################################################################################################################
    
# Naslednja rešitev je narejena na način da nevemo katera vrednost je maksimalna:
# Za primer v katerem vemo maksimalno svetlost, poglejte spodaj od linije 67 naprej.
maxSvetlost = 0
lucka = Lucka() # inicializiramo razred Lucka ki vsebuje programsko resitev

while lucka.PreveriSvetlost() != 0 or maxSvetlost == 0: # dokler ni svetlost 0 ali dokler je nasa maksimalna svetlost enaka 0, pritiskamo na tipko
    if lucka.PreveriSvetlost() > maxSvetlost: # če je trenutna svetlost večja od maxSvetlosti, jo nastavimo kot maxSvetlost
        maxSvetlost = lucka.PreveriSvetlost()
    lucka.PritisniTipko()

print("Maksimalna svetlost: " + str(maxSvetlost)) # izpišemo maxSvetlost

while lucka.PreveriSvetlost() < maxSvetlost: # dokler ni svetlost enaka maxSvetlosti, pritiskamo na tipko
    lucka.PritisniTipko()

print("Trenutna svetlost luci: " + str(lucka.PreveriSvetlost())) # izpišemo trenutno svetlost luči da potrdimo če je res nastavljena na maxSvetlost



# Naslednja rešitev je narejena na način da vemo katera vrednost je maksimalna:
# Za primer v katerem ne vemo maksimalne svetlosti, poglejte od linije 48 do 63.
maxSvetlost = 4
lucka = Lucka() # inicializiramo razred Lucka ki vsebuje programsko resitev

for i in range(maxSvetlost): # pritiskamo na tipko tolikokrat kot je maxSvetlost
    lucka.PritisniTipko()

print("Maksimalna svetlost: " + str(lucka.PreveriSvetlost())) # izpišemo maxSvetlost

