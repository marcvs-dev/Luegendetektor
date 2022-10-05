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
Die 39-Jährige besuchte an diesem Tag ihre beste Freundin. Sie haben ein bisschen gefeiert da sie einen Job gefunden hat. 
Also tranken sie ein wenig, schauten gemeinsam Fernseher, kochten und backten. 
Anschließend wollten sie noch um 16:30 Uhr mit dem Hund spazieren gehen. 
Als Ulrike das Haus mit ihrem Hund um 16:12 Uhr verließ, kam der Täter von hinten. 
Mit einem gewöhnlichem Kuchenmesser wurde Ulrike 6mal brutal in den Rücken gestochen. 
Ulrike viel schnell in schockstarre und konnte daher nicht schreien. 
Der Hund versuchte den Angreifer zu verjagen, doch leider vergeblich.""")

input("")  #Man muss Enter drücken damit weiterer text ausgegeben wird.
print("")

print_schneller("""Ulrikes Freundin dachte sich nichts vom bellenden Hund. Sie zog sich schon passend zum Wandern an. 
Als ihre Freundin nach 5 Minuten immer noch nicht zurück war wurde sie misstrauisch. 
Sie öffnete die Türe und sah ein riesen Blutfleck auf dem Boden. Ulrikes Hund Bello lag auf dem Blutfleck und rührte sich nicht. 
Die Freundin geriet in Panik und schrie nach ihrer Freundin. Niemand antwortete. 
Sie rann zurück ins Haus und holte ihr Handy um die Polizei zu rufen. Um 16:21 Uhr klingelte es dann bei der wache. 
Sofort wurden Spurensicherung und Kommissare sowohl Psychologe losgeschickt um den Fundort zu begutachten. 
Sie hatten keine Spur. Die suche war vergeblich. 
2 Wochen später am 17.10.2022 wurde ihre Leiche halb verscharrt an einem Waldrand gefunden.""")

time.sleep(1000)