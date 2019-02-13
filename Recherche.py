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


from Token import *



class Recherche(object):
    def __init__(self):
        self.token = Token().getToken()
    def setToken(self):
        self.token = Token().getToken()
    def getRecherche(self,commune,rome):
        
        response = requests.get('https://api.emploi-store.fr/partenaire/labonneboite/v1/company/?commune_id='+commune+'&rome_codes='+str(rome),headers={"Authorization": "Bearer " + str(self.token)})
        try:
            json_response = json.loads(response.content)
            liste = list(json_response)
            return  liste[0]["companies"]
        except :
            return []
        
    def getCommune(self):
        response = requests.get('https://api.emploi-store.fr/partenaire/eterritoire/v1/cadre-de-vie.php',headers={"Authorization": "Bearer " + str(self.token)})
        json_response = json.loads(response.content)
        idinsee =[]
        for i in range(0,len(json_response) ):
            idinsee.append([json_response[i]["idinsee"],json_response[i]["nom"]]) #,json_response[i]["gps"][0],json_response[i]["gps"][0]]
        return idinsee
