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


import xlwt
import xlrd

class Excel(object):
    def __init__(self):
        self.workbook = xlwt.Workbook(encoding = 'ascii')
        self.worksheet = self.workbook.add_sheet('Feuille1')
        self.worksheet.write(0,0 , "Rome v2 ") 
        self.worksheet.write(0,1 , "Intitule V2")
        self.worksheet.write(0,2, "Nom job")
        self.worksheet.write(0,3, "Nom entreprise")
        self.worksheet.write(0,4, "Addresse")
        self.worksheet.write(0,5, "Ville")
        self.worksheet.write(0,6, "mode de contact")

        self.worksheet.write(0,8, "Rome V3")
        self.worksheet.write(0,9, "Intitule V3")
        self.worksheet.write(0,10, "Nom job")
        self.worksheet.write(0,11, "Nom entreprise")
        self.worksheet.write(0,12, "Addresse")
        self.worksheet.write(0,13, "Ville")
        self.worksheet.write(0,14, "mode de contact")
        self.workbook.save('resultat.xls')
    
    def lire(self):
        data = xlrd.open_workbook('liste.xlsx')
        feuille = data.sheet_by_name('Feuil1')
        idv2= []
        idv3 = []
        for i in range(1,feuille.nrows):
            row = feuille.row_values(i)
            v2id = row[ 0 ]
            v3id = row[ 3 ]
            temoinv2 = True
            temoinv3 = True
            for j in range(len(idv2)):
                if idv2[j][0] == v2id:
                    temoinv2 = False
                    break
            if temoinv2:
                idv2.append([row[ 0 ],row[ 1 ] ])

            for j in range(len(idv3)):
                if idv3[j][0] == v3id:
                    temoinv3 = False
                    break
            if temoinv3:
                idv3.append([row[3],row[ 4]])       
        return idv2,idv3
    
    def EcrireV3(self,indice,id,companies):
        if len(companies)> 0:
            for i in range(len(companies)):
                self.worksheet.write(indice,8, id[0])
                self.worksheet.write(indice,9, id[1])
                self.worksheet.write(indice,10,companies[i]["naf_text"] )
                self.worksheet.write(indice,11, companies[i]["name"])
                self.worksheet.write(indice,12, companies[i]["address"])
                self.worksheet.write(indice,13, companies[i]["city"])
                self.worksheet.write(indice,14, companies[i]["contact_mode"])
                indice = indice + 1
            self.workbook.save('resultat.xls')
        return indice 

    def EcrireV2(self,indice,id,companies):
        if len(companies)> 0:
            for i in range(len(companies)):
                    self.worksheet.write(indice,0, id[0])
                    self.worksheet.write(indice,1, id[1])
                    self.worksheet.write(indice,2,companies[i]["naf_text"] )
                    self.worksheet.write(indice,3, companies[i]["name"])
                    self.worksheet.write(indice,4, companies[i]["address"])
                    self.worksheet.write(indice,5, companies[i]["city"])
                    self.worksheet.write(indice,6, companies[i]["contact_mode"])
                    indice = indice + 1
            self.workbook.save('resultat.xls')
        return indice 
