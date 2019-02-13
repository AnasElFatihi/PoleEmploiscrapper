
#!/usr/bin/env python3

__author__ = "Anas EL FATIHI"
__copyright__ = "Copyright 2019"
__credits__ = ["Anas EL FATIHI"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "ANAS EL FATIHI"
__email__ = "anaselfatihi1@gmail.com"
__email__ = "contact@emis-agency.com"
__status__ = "Production"

from Recherche import *
from Excel import *
import time

class Programme(object):

    def __init__(self):
        self.recherche = Recherche()
        self.fichier = Excel()
        self.idinse = self.recherche.getCommune()
        
    def mainloop(self):
        idv2,idv3 = self.fichier.lire()

        indicev3 = 1
        for i in range(len(idv3)):
            #time pour token 
            start_time = time.time()
            a = str(idv3[i][0]).split('.')[0]
            for j in range(len(self.idinse)):
                companies = self.recherche.getRecherche(self.idinse[j][0],a)
                indicev3 = self.fichier.EcrireV3(indicev3,idv3[i],companies)
                end_time = time.time()
                if( end_time - start_time >= 1000):   
                    self.recherche.setToken()

        self.recherche.setToken()

        indicev2 = 1
        for i in range(len(idv2)):
            #time pour token 
            start_time = time.time()
            a = str(idv2[i][0]).split('.')[0]
            for j in range(len(self.idinse)):
                companies = self.recherche.getRecherche(self.idinse[j][0],a)
                indicev2 = self.fichier.EcrireV2(indicev2,idv2[i],companies)
                end_time = time.time()
                if( end_time - start_time >= 1000):
                    self.recherche.setToken()
