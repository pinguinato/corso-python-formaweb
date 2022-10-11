import pandas as pd
import matplotlib.pyplot as plt
import requests
url = 'http://www.dati.salute.gov.it/imgs/C_17_dataset_96_0_upFile.csv'

csv=pd.read_csv('C_17_dataset_96_0_upFile.csv', sep=';', encoding='unicode_escape')

print(csv.head()) # ci ritorna le prime 5 righe
csv.dtypes # ci ritorna righe e colonne

# esempio visto alla lezione 3
csv_2014 = csv[csv['Anno']==2014]
# totale dei posti letto, seleziono una colonna soltanto
beds_2014 = csv_2014['Totale posti letto']
beds_2014 = csv_2014.groupby('Denominazione Struttura/Stabilimento')['Totale posti letto'].sum()
print(beds_2014)
print(beds_2014.describe())
# istogramma
histogram = beds_2014.hist(bins=50)
histogram.set_title('Letti per ospedale 2014')
histogram.set_xlabel('numero di letti')
histogram.set_ylabel('numero di oespedali')
plt.show()