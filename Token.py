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

import requests
import json 

class Token(object):
    def __init__(self):
        self.data = {'realm': '/partenaire',"grant_type": "client_credentials","client_id": "PAR_myapi_ce686dc023606cd710b4977a5844005f0bdf8d4e69e4be45fd62e81d24d8190d","client_secret": "c6f1e811035bcb9ad24e90b0753055c092883124cd81341ec16cf543285749ca","scope" : "application_PAR_myapi_ce686dc023606cd710b4977a5844005f0bdf8d4e69e4be45fd62e81d24d8190d api_labonneboitev1 api_eterritoirev1" } 

    def getToken(self):
        response = requests.post('https://entreprise.pole-emploi.fr/connexion/oauth2/access_token', data=self.data,headers={"Content-Type": "application/x-www-form-urlencoded"})
        json_response = json.loads(response.content)
        return json_response['access_token']
