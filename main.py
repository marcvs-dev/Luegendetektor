import time
import sys
import os


def print_langsam(str):                #Jeder einzelne Buichstabe innerhalb des textes mit print_langsam wird mit 0.06 Sekunden Abstand ausgegeben.
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.06)


def print_schneller(str):              #Jeder einzelne Buichstabe innerhalb des textes mit print_schneller wird mit 0.05 Sekunden Abstand ausgegeben.
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.035)


 #---------------------------------------------------------------------------------------------------------       

os.system("cls")

print_langsam("Hallo! Sie sind hier da sie ein Verdächtiger im Mordfall von Ulrike sind.")

input("")  #Man muss Enter drücken damit weiterer text ausgegeben wird.
print("")

print_schneller("""Ich und meine Kollegen werden nun die Geschichte unserer Kenntnisse nacherzählen.
Später werden sie noch ein paar Fragen zu diesem Gewaltverbrechen mit Todesfolge stellen.
Wir sind bereit. Kamera läuft, Mikro läuft und ein Psychologe sowie ihr Anwalt stehen bereit. Nun zum Geschehen.""")

input("")  #Man muss Enter drücken damit weiterer text ausgegeben wird.
print("")

print_schneller("""Am 03.10.2022 wurde die 39-Jährige Ulrike in Suhl grauenhaft Ermordet.
Die 39-Jährige besuchte an diesem Tag ihre beste Freundin. Sie haben ein wenig gefeiert da sie einen Job gefunden hat. 
Also tranken sie ein wenig, schauten gemeinsam Fernseher, kochten und backten. 
Anschließend wollten sie noch um 16:30 Uhr mit dem Hund im Schwarzwald wandern gehen. 
Als Ulrike das Haus mit ihrem Hund um 16:12 Uhr verließ, kam ein Mann oder eine Frau von hinten. 
Mit einem gewöhnlichem Kuchenmesser wurde Ulrike 34mal in den Rücken gestochen. 
Ulrike viel schnell in schockstarre und konnte so nicht schreien. 
Als ihr Hund versuchte den Angreifer zu verjagen brachte es nichts. 
Der Angreifer kennt Hunde und konnte sich so ohne weiteres bewegen.""")

time.sleep(1000)