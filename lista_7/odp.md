### Ćwiczenie 45 - Koncentracja odległości
* **Co obserwujesz?**
  Wartość *R(d)* szybko dąży do zera wraz ze wzrostem liczby wymiarów *d*. Oznacza to, że w przestrzeniach wysokowymiarowych odległość do najbliższego i najdalszego sąsiada staje się do siebie zbliżona (następuje zjawisko koncentracji odległości).
* **Jaka jest konsekwencja dla metody KNN?**
  Jest to przejaw "przekleństwa wymiarowości". W przestrzeniach o wielu wymiarach wszystkie punkty są od siebie "prawie tak samo odległe". Pojęcie najbliższego sąsiada traci swoje właściwości dyskryminacyjne, przez co algorytmy oparte na odległości (takie jak k-NN) drastycznie tracą skuteczność.

---

### Ćwiczenie 46 - Degradacja KNN
* **Przy jakim wymiarze KNN z K = 1 przestaje być lepszy od losowego klasyfikatora?**
  Dokładność modelu zrównuje się z wynikiem klasyfikatora losowego (około 0.5) zazwyczaj w okolicach wymiaru *d* = 20 do *d* = 50 (i pozostaje na tym poziomie dla wyższych wymiarów). W tak wysokich wymiarach najbliższy sąsiad staje się punktem niemalże losowym pod kątem przestrzennym, więc jego etykieta nie niesie informacji użytecznej do predykcji.

---

### Ćwiczenie 47 - Objętość hiperkuli
* **Dla jakich *d* udział objętości hiperkuli w objętości otaczającej ją hiperkostki staje się pomijalny?**
  Udział ten maleje drastycznie i można go uznać za pomijalny w okolicach *d* >= 10 (spada wtedy do ułamków procenta, a cała objętość "ucieka" w rogi hiperkostki).
* **Dla jakich *d* metoda Monte Carlo przestaje dawać sensowne wyniki i dlaczego?**
Metoda ta zazwyczaj przestaje działać (zwraca objętość równą 0) dla wymiarów *d* >= 13 przy standardowej liczbie prób (np. 100 000 losowań). Dzieje się tak, ponieważ udział objętości kuli w kostce spada niemal do zera, przez co prawdopodobieństwo wylosowania punktu, który "trafi" wewnątrz hiperkuli, staje się tak znikome, że w rozsądnej liczbie prób żaden punkt się w niej nie znajduje.

---

### Ćwiczenie 48 - Regresja wielomianowa (Bias-Variance Tradeoff)
* **Wskaż optymalny stopień wielomianu:**
  Optymalny stopień (dla którego błąd walidacji krzyżowej osiąga minimum) wynosi zazwyczaj *d* = 3. Wielomian ten dobrze przybliża główny kształt ukrytej funkcji bez dopasowywania się do szumu.
* **Skomentuj wyniki:**
  Wyniki ilustrują kompromis między obciążeniem a wariancją:
  1. **Błąd treningowy** stale maleje wraz ze wzrostem stopnia *d*, ponieważ bardziej złożony model uczy się danych (oraz szumu) na pamięć.
  2. **Błąd walidacji krzyżowej** najpierw spada, osiąga minimum dla optymalnego *d*, a następnie drastycznie rośnie.
  3. Dla wysokich stopni (np. *d* > 5) model ulega silnemu **przeuczeniu (overfitting)** – idealnie dopasowuje się do punktów treningowych, ale jego predykcje pomiędzy nimi stają się skrajnie niestabilne, co skutkuje ogromnym błędem na nowych danych.