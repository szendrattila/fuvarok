"""
taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja
5240; 2016-12-15 23:45:00; 900;2,5; 10,75; 2,45; bankkártya
1215;2016-12-12 07:15:00;240;0,4;5,0;3,0;bankkártya
"""
class Fuvar:
    def __init__(self, sor):
        taxi_id, indulas, idotartam, tavolsag, viteldij, borravalo, fizetes_modja = sor.strip().replace(',','.').split(";")
        self.taxi_id =       int(taxi_id)
        self.indulas =       str(indulas)
        self.idotartam =     int(idotartam)
        self.tavolsag =      float(tavolsag)
        self.viteldij =      float(viteldij)
        self.borravalo =     float(borravalo)
        self.fizetes_modja = str(fizetes_modja)
lista = []
with open("fuvar.txt", encoding="utf-8") as f:
    f.readline()
    for sor in f:
        lista.append(Fuvar(sor))
#3.feladat
print(f"3.feladat: {len(lista)} fuvar")
#4.feladat
hanyfuvar = len([sor.viteldij for sor in lista if sor.taxi_id == 6185])
penz = [sor.viteldij + sor.borravalo for sor in lista if sor.taxi_id == 6185]
teljes = sum(penz)
print(f"4. feladat: {hanyfuvar} alatt: {teljes}$")
#5.feladat
print("5. feladat")
stat = dict()
for sor in lista:
    stat[sor.fizetes_modja] = stat.get(sor.fizetes_modja, 0) + 1
for kulcs, ertek in stat.items():
    print(f"    {kulcs}: {ertek} fuvar ")
#6.feladat
szamlalo = 0
for sor in lista:
    szamlalo = sor.tavolsag + szamlalo
formalt = "{:.2f}".format(szamlalo * 1.6)
print(f"6. feladat: {formalt}km")
#7.feladat
print("7. feladat:")
legnagyobbtar = max(lista, key=lambda x:x.idotartam).idotartam
legnagyobbid = max(lista, key=lambda x:x.idotartam).taxi_id
legnagyobbtav = max(lista, key=lambda x:x.idotartam).tavolsag
legnagyobbdij = max(lista, key=lambda x:x.idotartam).viteldij
print(f"Fuvar hossza:{legnagyobbtar} másodperc\n Taxi azonositó:{legnagyobbid}\n Megtett távolság: {legnagyobbtav:}km\n Viteldij: {legnagyobbdij}$")
#8.feladat
with open("hibak.txt", "w", encoding("utf-8"):
    
          
