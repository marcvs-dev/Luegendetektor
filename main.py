import os
import sys
import time
from csv import excel
import numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def title():
  print("""
██╗     ██╗   ██╗███████╗ ██████╗ ███████╗███╗   ██╗██████╗ ███████╗████████╗███████╗██╗  ██╗████████╗ ██████╗ ██████╗ 
██║     ██║   ██║██╔════╝██╔════╝ ██╔════╝████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║ ██╔╝╚══██╔══╝██╔═══██╗██╔══██╗
██║     ██║   ██║█████╗  ██║  ███╗█████╗  ██╔██╗ ██║██║  ██║█████╗     ██║   █████╗  █████╔╝    ██║   ██║   ██║██████╔╝
██║     ██║   ██║██╔══╝  ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝     ██║   ██╔══╝  ██╔═██╗    ██║   ██║   ██║██╔══██╗
███████╗╚██████╔╝███████╗╚██████╔╝███████╗██║ ╚████║██████╔╝███████╗   ██║   ███████╗██║  ██╗   ██║   ╚██████╔╝██║  ██║
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
von Peter, Marc und Alex

  """)










#---------------------------------------------------------------------------------------------------------
#Excel

excel_datei = pd.read_excel("dateien/Fragen.xlsx")  #Excel

def excel():
  print(excel_datei) #Ganze Datei ausgeben
  print(
    excel_datei.iloc[1, 2]
  )  #Zeile 3 Spalte 2 -- Es fängt bei 0 an zu zählen! In Excel muss alles eins runter, damit es funktioniert! 


#---------------------------------------------------------------------------------------------------------
#Textgeschwindigkeit

def print_schneller(
  str
):  #Jeder einzelne Buichstabe innerhalb des textes mit print_schneller wird mit 0.05 Sekunden Abstand ausgegeben.
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.055)
#---------------------------------------------------------------------------------------------------------
#Standartabweichung

def std():



  liste = excel_datei.iloc[:, 9]
  #print("List : " + str(list))

  st_dev_minus_plus = np.std(liste)
  st_dev = (abs(st_dev_minus_plus))

  print("")
  print("----------------------------------------------------------------")
  print("Die Standartabweichung der Gewichtung ist", st_dev)
  print("----------------------------------------------------------------")
  print("")

  if st_dev >= 3:
    print("Die Wahrscheinlichkeit, dass sie die Wahrheit sagen liegt bei 0,2%. Du lügst!")
  elif st_dev >= 2 and st_dev < 3:
    print("Die Wahrscheinlichkeit, dass sie die Wahrheit sagen liegt bei 4,2%. Du lügst!")
  elif st_dev >= 1 and st_dev < 2:
    print("Die Wahrscheinlichkeit, dass sie die Wahrheit sagen liegt bei 27,2%. Du lügst!")
  elif st_dev >= 0 and st_dev < 1:
    print("Die Wahrscheinlichkeit, dass sie die Wahrheit sagen liegt bei 68,2%. Du lügst!")
  elif st_dev == 0:
    print("Wir glauben dir, die Wahrscheinlichkeit, dass du die Wahrheit sagst ist sehr hoch")
  else:
    print("Es ist ein Fehler unterlaufen!")


  
def diagramm():
  data = pd.read_excel("dateien/fragen.xlsx")

  y = data["Herzschlag"][:101]
  x = []

  for a in range(1, 102):
    x.append(a)
 
  plt.plot(x, y)

  plt.show()
    
  
#---------------------------------------------------------------------------------------------------------
# Programm an sich (Text)
def text():
  print("")
  print("----------------------------------------------------------------")
  print("")

  print_schneller("Hallo! Sie sind hier da sie ein Verdächtiger im Mordfall von Ulrike sind.")

  print("""
  """)

  print_schneller("""Ich und meine Kollegen werden nun die Geschichte unserer Kenntnisse nacherzählen.
Später werden sie noch ein paar Fragen zu diesem Gewaltverbrechen mit Todesfolge stellen.
Wir sind bereit.
Kamera läuft, Mikro läuft und ein Psychologe sowie ihr Anwalt stehen bereit.
Nun zum Geschehen.
  """)

  print("""
  """)

  print_schneller("""Am 03.10.2022 wurde die 39-Jährige Ulrike in Suhl grauenhaft Ermordet.
Die 39-Jährige besuchte an diesem Tag ihre beste Freundin in Suhl. Ein rotes Haus mit der Hausnummer 16.
Sie haben ein wenig gefeiert da sie einen Job gefunden hat.
Also tranken sie ein wenig, schauten gemeinsam Fernseher, kochten und backten.
Anschließend wollten sie noch um 16:30 Uhr mit dem Hund im Schwarzwald wandern gehen.
  """)

  print("""
  """)

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

  print("""
  """)

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

  print("""
  """)

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

  print("""
  """)

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
def fragen():
  print("""
  """)
  print("""
  """)
  print("""
███████╗██████╗  █████╗  ██████╗ ███████╗███╗   ██╗
██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔════╝████╗  ██║
█████╗  ██████╔╝███████║██║  ███╗█████╗  ██╔██╗ ██║
██╔══╝  ██╔══██╗██╔══██║██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║██║  ██║╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                   
""")
  print("Kommen wir nun zu den Fragen.")
  print("----------------------------------------------------------------")
  print("Frage:", excel_datei.iloc[	0,2	], "\nAntwort:", excel_datei.iloc[	0,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	1,2	], "\nAntwort:", excel_datei.iloc[	1,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	2,2	], "\nAntwort:", excel_datei.iloc[	2,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	3,2	], "\nAntwort:", excel_datei.iloc[	3,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	4,2	], "\nAntwort:", excel_datei.iloc[	4,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	5,2	], "\nAntwort:", excel_datei.iloc[	5,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	6,2	], "\nAntwort:", excel_datei.iloc[	6,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	7,2	], "\nAntwort:", excel_datei.iloc[	7,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	8,2	], "\nAntwort:", excel_datei.iloc[	8,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	9,2	], "\nAntwort:", excel_datei.iloc[	9,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	10,2	], "\nAntwort:", excel_datei.iloc[	10,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	11,2	], "\nAntwort:", excel_datei.iloc[	11,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	12,2	], "\nAntwort:", excel_datei.iloc[	12,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	13,2	], "\nAntwort:", excel_datei.iloc[	13,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	14,2	], "\nAntwort:", excel_datei.iloc[	14,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	15,2	], "\nAntwort:", excel_datei.iloc[	15,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	16,2	], "\nAntwort:", excel_datei.iloc[	16,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	17,2	], "\nAntwort:", excel_datei.iloc[	17,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	18,2	], "\nAntwort:", excel_datei.iloc[	18,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	19,2	], "\nAntwort:", excel_datei.iloc[	19,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	20,2	], "\nAntwort:", excel_datei.iloc[	20,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	21,2	], "\nAntwort:", excel_datei.iloc[	21,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	22,2	], "\nAntwort:", excel_datei.iloc[	22,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	23,2	], "\nAntwort:", excel_datei.iloc[	23,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	24,2	], "\nAntwort:", excel_datei.iloc[	24,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	25,2	], "\nAntwort:", excel_datei.iloc[	25,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	26,2	], "\nAntwort:", excel_datei.iloc[	26,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	27,2	], "\nAntwort:", excel_datei.iloc[	27,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	28,2	], "\nAntwort:", excel_datei.iloc[	28,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	29,2	], "\nAntwort:", excel_datei.iloc[	29,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	30,2	], "\nAntwort:", excel_datei.iloc[	30,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	31,2	], "\nAntwort:", excel_datei.iloc[	31,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	32,2	], "\nAntwort:", excel_datei.iloc[	32,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	33,2	], "\nAntwort:", excel_datei.iloc[	33,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	34,2	], "\nAntwort:", excel_datei.iloc[	34,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	35,2	], "\nAntwort:", excel_datei.iloc[	35,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	36,2	], "\nAntwort:", excel_datei.iloc[	36,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	37,2	], "\nAntwort:", excel_datei.iloc[	37,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	38,2	], "\nAntwort:", excel_datei.iloc[	38,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	39,2	], "\nAntwort:", excel_datei.iloc[	39,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	40,2	], "\nAntwort:", excel_datei.iloc[	40,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	41,2	], "\nAntwort:", excel_datei.iloc[	41,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	42,2	], "\nAntwort:", excel_datei.iloc[	42,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	43,2	], "\nAntwort:", excel_datei.iloc[	43,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	44,2	], "\nAntwort:", excel_datei.iloc[	44,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	45,2	], "\nAntwort:", excel_datei.iloc[	45,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	46,2	], "\nAntwort:", excel_datei.iloc[	46,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	47,2	], "\nAntwort:", excel_datei.iloc[	47,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	48,2	], "\nAntwort:", excel_datei.iloc[	48,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	49,2	], "\nAntwort:", excel_datei.iloc[	49,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	50,2	], "\nAntwort:", excel_datei.iloc[	50,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	51,2	], "\nAntwort:", excel_datei.iloc[	51,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	52,2	], "\nAntwort:", excel_datei.iloc[	52,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	53,2	], "\nAntwort:", excel_datei.iloc[	53,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	54,2	], "\nAntwort:", excel_datei.iloc[	54,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	55,2	], "\nAntwort:", excel_datei.iloc[	55,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	56,2	], "\nAntwort:", excel_datei.iloc[	56,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	57,2	], "\nAntwort:", excel_datei.iloc[	57,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	58,2	], "\nAntwort:", excel_datei.iloc[	58,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	59,2	], "\nAntwort:", excel_datei.iloc[	59,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	60,2	], "\nAntwort:", excel_datei.iloc[	60,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	61,2	], "\nAntwort:", excel_datei.iloc[	61,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	62,2	], "\nAntwort:", excel_datei.iloc[	62,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	63,2	], "\nAntwort:", excel_datei.iloc[	63,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	64,2	], "\nAntwort:", excel_datei.iloc[	64,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	65,2	], "\nAntwort:", excel_datei.iloc[	65,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	66,2	], "\nAntwort:", excel_datei.iloc[	66,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	67,2	], "\nAntwort:", excel_datei.iloc[	67,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	68,2	], "\nAntwort:", excel_datei.iloc[	68,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	69,2	], "\nAntwort:", excel_datei.iloc[	69,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	70,2	], "\nAntwort:", excel_datei.iloc[	70,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	71,2	], "\nAntwort:", excel_datei.iloc[	71,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	72,2	], "\nAntwort:", excel_datei.iloc[	72,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	73,2	], "\nAntwort:", excel_datei.iloc[	73,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	74,2	], "\nAntwort:", excel_datei.iloc[	74,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	75,2	], "\nAntwort:", excel_datei.iloc[	75,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	76,2	], "\nAntwort:", excel_datei.iloc[	76,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	77,2	], "\nAntwort:", excel_datei.iloc[	77,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	78,2	], "\nAntwort:", excel_datei.iloc[	78,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	79,2	], "\nAntwort:", excel_datei.iloc[	79,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	80,2	], "\nAntwort:", excel_datei.iloc[	80,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	81,2	], "\nAntwort:", excel_datei.iloc[	81,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	82,2	], "\nAntwort:", excel_datei.iloc[	82,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	83,2	], "\nAntwort:", excel_datei.iloc[	83,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	84,2	], "\nAntwort:", excel_datei.iloc[	84,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	85,2	], "\nAntwort:", excel_datei.iloc[	85,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	86,2	], "\nAntwort:", excel_datei.iloc[	86,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	87,2	], "\nAntwort:", excel_datei.iloc[	87,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	88,2	], "\nAntwort:", excel_datei.iloc[	88,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	89,2	], "\nAntwort:", excel_datei.iloc[	89,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	90,2	], "\nAntwort:", excel_datei.iloc[	90,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	91,2	], "\nAntwort:", excel_datei.iloc[	91,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	92,2	], "\nAntwort:", excel_datei.iloc[	92,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	93,2	], "\nAntwort:", excel_datei.iloc[	93,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	94,2	], "\nAntwort:", excel_datei.iloc[	94,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	95,2	], "\nAntwort:", excel_datei.iloc[	95,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	96,2	], "\nAntwort:", excel_datei.iloc[	96,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	97,2	], "\nAntwort:", excel_datei.iloc[	97,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	98,2	], "\nAntwort:", excel_datei.iloc[	98,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)
  print("Frage:", excel_datei.iloc[	99,2	], "\nAntwort:", excel_datei.iloc[	99,6	])
  print("----------------------------------------------------------------")
  time.sleep(3)


os.system("cls")

title()

def Ende():
  print("""
  """)
  print("Danke für dein Interesse an unserem Mordfall!")


text_yn = input("Willst du den Text lesen, oder kennst du ihn schon? Ja/Nein: ")
fragen_yn = input("Willst du die Fragen lesen, oder kennst du diese? Ja/Nein: ")
diagramm_yn = input("Willst du ein Diagramm zu dem Herzschlag sehen? Ja/Nein: ")

if text_yn == "Ja":
  text()
if fragen_yn == "Ja":
    fragen()
if diagramm_yn == "Ja":
 diagramm()

Ende()




