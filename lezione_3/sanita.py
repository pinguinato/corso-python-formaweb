import pandas as pd 
import matplotlib.pyplot as plt
import requests
url = 'http://www.dati.salute.gov.it/imgs/C_17_dataset_96_0_upFile.csv'
nuova_apertura = 0
if nuova_apertura:
    r = requests.get(url, allow_redirects=True)
    open('C_17_dataset_96_0_upFile.csv','wb').write(r.content)
csv=pd.read_csv('C_17_dataset_96_0_upFile.csv', sep=';', encoding='unicode_escape')
# metodi di csv usati come esempio
print(csv.head())
print(csv.dtypes)
# filtrare i dati
csv_2014 = csv[csv['Anno']==2014]
print(csv_2014)
# totale dei posti letto, seleziono una colonna soltanto
beds_2014 = csv_2014['Totale posti letto']
beds_2014 = csv_2014.groupby('Denominazione Struttura/Stabilimento')['Totale posti letto'].sum()
print(beds_2014)
# describe() è un metodo delle series e dei dataframes che mi da per le colonne di tipo quantitativo tutti i momenti importanti(media, deviazione, minimo, massimo ecc...)
print(beds_2014.describe())
# facciamo un istogramma di questa distribuzione
histogram = beds_2014.hist(bins=50)
histogram.set_title('Letti per ospedale 2014')
histogram.set_xlabel('numero di letti')
histogram.set_ylabel('numero di oespedali')
#plt.show()
print(type(beds_2014))
print("Pandas Version ==> ", pd.__version__)