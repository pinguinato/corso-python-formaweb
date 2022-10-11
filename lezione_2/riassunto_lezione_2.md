# Lezione 2

## Appunti

Modifica dell'orario: lunedì 30/11 si prova dalle 18.15 alle 21.15

### Liste in Python

Rappresentano dei dati che hanno più di una dimensione.

Es. il gioco della battaglia navale

Una lista a differenza del dizionario contiene un ordine. Quello che importa è l'ordine.

        elenco = [1,2,3,4,5,6,7]

#### append()

Inserisce elemnti in una lista, mette in coda

Es. 

        elenco.append(12)

L'invocazione di questo metodo è in place, ma non è sempre così per tutti!

**Importante**

Pandas è un pacchetto di modifica di tabelle **dataframes**, non è permessa l'operazione in place, si invoca un metodo su un dataframe,
ma non essendo un metodo in place, non funziona. Quindi attenzione.

Tutte le operazioni il cui risultato deve essere assegnato sono operazioni in place. Sono ad esempio le operazioni che devono ritornare un oggetto 
differente. I metodi ad esempio se applicati su una stringa e non la salvano non sono metodi in place.

### Numpy

Libro di Gros prendere visione del capitolo 4 e 5
Libro di McKinney capitolo 4

Ricostruire con un notebook: http://www.fis.unical.it/astroplasmi/primavera/dottorato/Librerie_numpy_matplotlib.html

Esercizi: https://github.com/rougier/numpy-tutorial

Array: è un tipo di dato che fa parte di Numpy

Numpy implementa il calcolo matriciale, vettoriale

        pip install numpy

Importarlo negli scripts:

        import numpy as np

#### Problema versione 3.9.0 e Numpy

https://stackoverflow.com/questions/64654805/how-do-you-fix-runtimeerror-package-fails-to-pass-a-sanity-check-for-numpy-an

        pip uninstall numpy

        pip install numpy==1.19.3

Es. vettore ad una dimensione di 100 elementi

        In [1]: import numpy as np

        In [2]: vett = np.random.random_sample(100)

        In [3]: print(vett)

Es. vettore multidimensionale

### Spazi Lineari

Sono la creazione di elementi di numeri in un vettore che sono equamente spaziati (linspace)

**Importante**

Non tutte le liste si possono trasformare in array, vedasi le liste composte da elementi diversi,
gli array numpy hanno soltanto numeri.

**N.B.**

CSV = comma seprated file, perché nell'origine usavano la virgola come separatore

## Matplotlib

Replica in maniera fedele le funzionalità di plottaggio di MatLab. L'utilizzo è facile per chi arriva da MatLab.

## Metodo Monte Carlo

Quando si vuole determinare una certa quantità senza avere una legge che la spiega, si deve usare un generatore di numeri casuali.

Random è un generatore "uniforme", vuol dire che non ci sono delle classi più probabili di altre. Le classi sono tutte equiprobabili.

## Vettori

Numpy aggiunge al vettore tutte quelle operazioni che effettua la matematica sul vettore e non soltanto vede il vettore come il classico vettore informatico.

Per verificare le potenzialità dei vettori numpy dobbiamo usare il metodo **array()**

La somma tra vettori è definita soltanto per vettori della stessa lunghezza

La dimensione interna delle matrici deve essere uguale altrimenti non si può fare, così come la moltiplicazione tra vettori.

Matrice identità si chiama così perché moltiplicata sia a destra che a sinistra dà sempre uno, elemento neutro, il risultato della moltiplicazione è sempre la matrice stessa.

Vertical Stack operazione simile all'append, se non hanno lo stesso numero di colonne il vertical stack non lo posso fare.

Horizontal Stack per farlo devo avere lo stesso numero di righe


