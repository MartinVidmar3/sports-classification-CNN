# 🧠 Klasifikacija Sportova Pomoću Dubokog Učenja

Ovaj projekt je razvijen u sklopu kolegija **Neuronske mreže**. Glavni cilj projekta bio je provesti komparativnu analizu naprednih arhitektura konvolucijskih neuronskih mreža (CNN) na zadatku klasifikacije vrsta sportova koristeći javno dostupan skup slika s platforme Kaggle.

## 🛠️ Korištene Tehnologije i Arhitekture

Projekt je implementiran u jeziku **Python** uz korištenje modernih biblioteka za duboko učenje. U fokusu je bila usporedba triju moćnih obitelji modela:

* **ResNet (Residual Networks):** Korištenje preskočnih veza (*skip connections*) za rješavanje problema nestajućeg gradijenta.
* **DenseNet (Densely Connected Convolutional Networks):** Maksimalan protok informacija kroz izravno povezivanje svih slojeva, čime se potiče ponovna uporaba značajki.
* **EfficientNet:** Arhitektura optimizirana kroz balansirano skaliranje dubine, širine i rezolucije mreže (Compound Scaling).

---

## 📈 Metodologija i Analiza Rezultata

U sklopu tmskog rada, modeli su istrenirani na velikom broju epoha kako bi se detaljno analizirala dinamika učenja, brzina konvergencije i kretanje točnosti (*accuracy*) kroz vrijeme.



### Ključni zaključci:
* Pratili smo i vizualizirali krivulje točnosti i gubitka (*loss*) tijekom procesa treniranja.
* **Rezultati su u potpunosti opravdali teorijska očekivanja:**
    * **EfficientNet** je pokazao iznimnu efikasnost i visoku točnost uz manji broj parametara zahvaljujući pametnom skaliranju.
    * **DenseNet** je zbog guste povezane strukture odlično iskorištavao značajke i postizao stabilnu točnost.
    * **ResNet** je poslužio kao izvrstan i robustan baseline model s predvidljivom i stabilnom konvergencijom.

---

## 👥 Timski rad i Doprinos

Projekt je realiziran kao timski rad unutar kojeg smo uspješno podijelili faze predobrade slika, augmentacije podataka, postavljanja cjevovoda za treniranje (*training pipeline*) te evaluacije i vizualizacije konačnih metrika.