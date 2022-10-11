from csv import excel

import time
import pandas as pd
import sys
import os

#---------------------------------------------------------------------------------------------------------
#Excel

excel_datei = pd.read_excel("dateien/Fragen.xlsx")  #Excel

#print(excel_datei) #Ganze Datei ausgeben
#print(
 # excel_datei.iloc[1, 2]
#)  #Zeile 3 Spalte 2 -- Es fängt bei 0 an zu zählen! In Excel muss alles eins runter, damit es funktioniert!

#---------------------------------------------------------------------------------------------------------
#Text


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
# Programm an sich
#os.system("cls")



#------------------------------------------------------------
#Fragen
input("")#Man muss Enter drücken damit weiterer text ausgegeben wird.

print(
  excel_datei.iloc[1, 3]
)  

input("")#Man muss Enter drücken damit weiterer text ausgegeben wird.



input("")#Man muss Enter drücken damit weiterer text ausgegeben wird.


