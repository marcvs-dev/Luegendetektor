from csv import excel
import time
import numpy
import pandas as pd
import sys
import os

gewicht = pd.read_excel("dateien/Standartabweichung.xlsx")

abweichung = (gewicht.std()) #Berechnet Standartabweichung

zahlabweichung = abweichung.astype(float)

print(abweichung) 