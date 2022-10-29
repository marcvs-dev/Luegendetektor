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
print_schneller("For each letter should be a keyboard sound.")

#---------------------------------------------------------------------------------------------------------
#Standartabweichung




list = [1,3,3,3,3,1,2,1,2,2,2,1,3,2,3,1,2,1,0,1,1,1,0,1,1,3,1,1,0,1,1,2,1,1,2,1,2,1,3,1,1,1,0,1,1,3,2,1,1,1,2,0,1,1,0,2,1,1,1,2,2,0,1,3,2,2,1,1,2,2,0,1,1,0,1,1,3,1,1,3,1,1,3,1,0,2,3,1,1,1,1,3,0,1,2,1,1,0,1,1,3]


print("List : " + str(list))



st_dev = np.std(list)
print(st_dev)








#---------------------------------------------------------------------------------------------------------
# Programm an sich (Text)
os.system("cls") #Leert die Konsole

print_langsam("Hallo! Sie sind hier da sie ein Verdächtiger im Mordfall von Ulrike sind.")

input("")

print_schneller("""Ich und meine Kollegen werden nun die Geschichte unserer Kenntnisse nacherzählen.
Später werden sie noch ein paar Fragen zu diesem Gewaltverbrechen mit Todesfolge stellen.
Wir sind bereit.
Kamera läuft, Mikro läuft und ein Psychologe sowie ihr Anwalt stehen bereit.
Nun zum Geschehen.
""")

input("")

print_schneller("""Am 03.10.2022 wurde die 39-Jährige Ulrike in Suhl grauenhaft Ermordet.
Die 39-Jährige besuchte an diesem Tag ihre beste Freundin in Suhl. Ein rotes Haus mit der Hausnummer 16.
Sie haben ein wenig gefeiert da sie einen Job gefunden hat.
Also tranken sie ein wenig, schauten gemeinsam Fernseher, kochten und backten.
Anschließend wollten sie noch um 16:30 Uhr mit dem Hund im Schwarzwald wandern gehen.
""")

input("")

print_schneller("""Als Ulrike das Haus mit ihrem Hund um 16:12 Uhr verließ, kam ein Mann oder eine Frau von hinten.
Mit einem gewöhnlichem Kuchenmesser wurde Ulrike 6 mal in den Rücken gestochen.
Ulrike viel schnell in schockstarre und konnte so nicht schreien.
Als ihr Hund versuchte den Angreifer zu verjagen brachte es nichts.
Der Angreifer kennt Hunde und konnte sich so ohne weiteres bewegen.
Ulrikes Freundin dachte sich nichts vom bellenden Hund.
Sie zog sich schon passend zum Wandern an.
Als ihre Freundin nach 5 Minuten immer noch nicht zurück war wurde sie misstrauisch.
Sie öffnete die Türe und sah ein riesen Blutfleck auf dem Boden.
Ulrikes Hund Bello lag auf dem Blutfleck und rührte sich nicht.
Die Freundin geriet in Panik und schrie nach ihrer Freundin.
""")

input("")

print_schneller("""Niemand Antwortete.
Sie rann zurück ins Haus um ihr Handy zu holen um die Polizei zu rufen.
Um 16:21 Uhr klingelte es bei der wache.
Sofort wurden Spurensicherung und Kommissare sowohl ein Psychologe losgeschickt um den Fundort zu begutachten.
Sie hatten keine Spur.
Es gab keine Zeugen oder Ähnliches.
Nur ein anderer Hundebesitzer hörte das bellen.
Die suche war vergeblich.
2 Wochen später am 17.10.2022 wurde ihre Leiche halb verscharrt an einem Waldrand gefunden.
Es war ein Jäger welcher sofort die Polizei rief.
Die Spurensicherung konnte wichtige Dinge Feststellen.
""")

input("")

print_schneller("""Das Opfer verstarb erst am 05.10.2022 an Verblutung.
Es scheint als hätte der Täter versucht sie am Leben zu erhalten jedoch erfolglos.
Spuren deuteten auch auf einen Psychopathen hin.
Das Opfer wurde noch vor dem Tod misshandelt.
Vermutlich war dies das Ziel des Täters, die noch Junge frau zu ermorden.
Die Ärztlichen Mittel wurden laut Spurensicherung versucht zu entfernen jedoch Erfolglos.
Es deutet alles auf eine neue Art von Verband hin.
Der Täter ist vermutlich ein Arzt oder Helfer.
Er wusste wie er das Opfer zu behandeln hatte um sie später noch während Bewusstsein Vergewaltigen zu können.
Es könnte ein Liebhaber gewesen sein oder ein enger Freund welcher mehr wollte als nur Freunde sein.
Noch ist nichts sicher… unwahrscheinlich ist jedoch, dass es ein Fremder war.
Der Hund hätte sonst auch anders reagiert.
""")

input("")

print_schneller("""Beweise:
-Das Messer ist sehr neu.
-Entweder für die tat gekauft oder für den Hausgebrauch.
-Vielleicht ein Bäcker.
-Der Täter musste sehr Blutig gewesen sein.
-Das Opfer wurde laut Spurensicherung in einem VW Transporter.
-Der wagen hat vermutlich Äußere Schäden am Lack.
-Das Opfer verkratzte das Auto laut spuren unter den Fingernägeln.
-Vielleich besteht eine Delle im Hintern Teil des dunkel blauen Transporters.
-Grüne Fasern gefunden.
-Krankenhaus/Krankenwagen Verband benutzt. (Auch Bundeswehr)
""")


#---------------------------------------------------------------------------------------------------------
#Fragen
input("")#Man muss Enter drücken damit weiterer text ausgegeben wird.

print(
  excel_datei.iloc[0, 2] #Fängt immer bei 0 an zu Zählen!!
)  