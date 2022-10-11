# Lezione 1

## Informazione e dato

**Dato**

Ogni informazione mediante opportuni simboli dell'alfabeto. Il dato è la rappresentazione dell'informazione

**Informazione**

Un fatto, un concetto che posso comunicare, interpretare o elaborare attraverso strumenti automatici. L'informazione è 
l'insieme di un dato più un descrittore, cioè il descrittore è ciò che qualifica il dato. Esempio: peso 30 kg, dove kg è il descrittore e 30 il dato.

## Analisis dei dati che cosa è

L'analisi dei dati compie **5 azioni sui dati**, di fatto è una **pipeline** composta da queste cinque operazioni sui dati:
- Obtain (acquisizione)
- Scrub/Clean (pulizia)
- Explore/Visualize (trasformazione)
- Model (modellazione)
- Interpret (interpretazione)

Comporta 3 tipologie di differenti analisi:
- analisi diagnostica (perché è successa una certa cosa)
- analisis predittiva (cosa succederà verosimilmente)
- analisis prescrittiva (quali azioni intraprendere)

Per fare tutto ciò si serve di tantissimi strumenti che operano con i dati:
- le basi di dati (relazionali e non)
- l'analisi dei testi (sentiment analisys)
- data mining
- analisi di reti complesse
- statistica
- rappresentazioni dei dati
- analisi prescrittiva
- ecc...

## Python

Pubblicato nel 1991, ideato da Guido Von Rossum.

Python 2 (2000), sarà dismesso quest'anno (2020)

Python 3 (2008)

Garbage collection e supporto unicode

Versione di riferimento del corso la **3.8.2**, la versione 3.9 ha problemi con Numpy.

Ci sono 2 scuole di pensiero:
- installazione di python tramite python.org (prevede installatore di pacchetti PIP)
- installazione tramite anaconda (prevede installatore di pacchetti CONDA)

Python3 non è retrocompatibile con Python2

Python ha la sua massima potenza grazie all'uso di differenti pacchetti, che ne estendono e amplificano le possibilità.

**Vantaggi Python**

- linguaggio general purpose molto diffuso
- molto espressivo
- facillità di scrittura dei programmi
- facilità nel leggere i dati
- gestione a pacchetti
- rapidità di prototipazione e scalabilità
- visualizzazione grafica

**Importante**

- per installare su Windows 10 scaricare il pacchetto di installazione da https://www.python.org
- andare sul terminale e digitare **python**, se non succede niente vuol dire che dobbiamo settare le varibili di ambiente
- per abilitare il funzionamento dell'installer **pip** far puntare la cartella /scripts nelle variabili di ambiente

## Jupiter Lab

è un ambiente interattivo che serve a creare i **notebboks** Jupyter, in Jupyter si ragione a notebook (quaderni).

        pip install jupyterlab (installazione jupyter)

        jupyter lab (esecuzione dell'ambiente di sviluppo)

I file di Jupyter hanno estensione **.ipynb**

### Casting

Quando un tipo di dato viene trasformato in un altro tipo di dato, Python va molto forte sul casting implicito.

Esempio:

        math.log(math.pi + 1)

### Da evitare assolutamente

        from math import *

Si rischia di andare a sovrascrivere delle funzioni, poi tanto vale importare tutto l'intero pacchetto **math**, lo si può fare direttamente usando la direttiva **import**

        import math

Import selettivo:

        from math import pi

## Altre note su Python

- linguaggio ad alto livello
- è interpretato
- nessuna dichiarazione esplicita del tipo, le variabili non vanno dichiarate prima di essere usate
- procedurale, ad oggetti e funzionale
- indentazione

