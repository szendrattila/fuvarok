"""
taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja
5240; 2016-12-15 23:45:00; 900;2,5; 10,75; 2,45; bankkártya
1215;2016-12-12 07:15:00;240;0,4;5,0;3,0;bankkártya
"""
class Fuvar:
    def __init__(self, sor):
        taxi_id, indulas, idotartam, tavolsag, viteldij, borravalo, fizetes_modja = sor.strip().split(";")
        self.taxi_id =       int(taxi_id)
        self.indulas =       indulas
        self.tavolsag =      tavolsag
        self.viteldij =      viteldij
        self.borravalo =     borravalo
        self.fizetes_modja = fizetes_modja
        self.kor =           borravalo[:2]
        self.egesz =         viteldij[:2]
        self.tort =          viteldij[4:6]
lista = []
with open("fuvar.txt", encoding="utf-8") as f:
    f.readline()
    for sor in f:
        lista.append(Fuvar(sor))
#3.feladat
print(f"3.feladat: {len(lista)} fuvar")
#4.feladat
hanyfuvar = len([sor.kor for sor in lista if sor.taxi_id == 6185])
penz = [sor.egesz + sor.tort for sor in lista if sor.taxi_id == 6185]



