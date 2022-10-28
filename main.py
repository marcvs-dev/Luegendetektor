from csv import excel
import time
import numpy
import pandas as pd
import numpy as np
import sys
import os

#---------------------------------------------------------------------------------------------------------
#Excel

excel_datei = pd.read_excel("dateien/Fragen.xlsx")  #Excel

#print(excel_datei) #Ganze Datei ausgeben
#print(
#  excel_datei.iloc[1, 2]
#)  #Zeile 3 Spalte 2 -- Es fängt bei 0 an zu zählen! In Excel muss alles eins runter, damit es funktioniert!

#---------------------------------------------------------------------------------------------------------
#Textgeschwindigkeit


def print_langsam(
  str
):  #Jeder einzelne Buichstabe innerhalb des textes mit print_langsam wird mit 0.06 Sekunden Abstand ausgegeben.
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.06)


def print_schneller(
  str
):  #Jeder einzelne Buichstabe innerhalb des textes mit print_schneller wird mit 0.05 Sekunden Abstand ausgegeben.
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.055)


#---------------------------------------------------------------------------------------------------------
#Standartabweichung




list = [1,3,3,3,3,1,2,1,2,2,2,1,3,2,3,1,2,1,0,1,1,1,0,1,1,3,1,1,0,1,1,2,1,1,2,1,2,1,3,1,1,1,0,1,1,3,2,1,1,1,2,0,1,1,0,2,1,1,1,2,2,0,1,3,2,2,1,1,2,2,0,1,1,0,1,1,3,1,1,3,1,1,3,1,0,2,3,1,1,1,1,3,0,1,2,1,1,0,1,1,3]


print("List : " + str(list))



st_dev = np.std(list)
print(st_dev)








#---------------------------------------------------------------------------------------------------------
# Programm an sich (Text)



#---------------------------------------------------------------------------------------------------------
#Fragen
input("")#Man muss Enter drücken damit weiterer text ausgegeben wird.

print(
  excel_datei.iloc[0, 2] #Fängt immer bei 0 an zu Zählen!!
)  




#test marc 