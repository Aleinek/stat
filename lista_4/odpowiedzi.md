# Zadanie 28

### (c) Jak zmienia się kształt krzywej $\ell(\lambda)/n$ gdy $n$ rośnie?

Krzywa opisana jest wzorem $\frac{\ell(\lambda)}{n} = \log(\lambda) - \lambda \bar{x}$. Jej kształt zależy w całości od wariancji średniej z próby $\bar{x}$.
* **Dla małych $n$ (np. 5):** Średnia z próby mocno fluktuuje, przez co krzywa może być przesunięta, a jej wierzchołek znajdować się stosunkowo daleko od prawdziwej wartości $\lambda_0 = 2$.
* **Dla dużych $n$ (np. 200):** Zgodnie z Prawem Wielkich Liczb, średnia $\bar{x}$ stabilizuje się wokół wartości oczekiwanej ($0.5$). Krzywa zbiega do funkcji granicznej, a jej wierzchołek precyzyjnie osiada bardzo blisko wartości $\lambda_0 = 2$.


### (d) Czy średnia z B wartości jest bliska $\lambda_0 = 2$? Jak wielkość obciążenia zmienia się z $n$?

1. **Obecność obciążenia:** Dla małych prób estymator $\hat{\lambda} = \frac{1}{\bar{x}}$ regularnie przeszacowuje prawdziwą wartość parametru (obciążenie jest zawsze dodatnie). Matematycznie wynika to z nierówności Jensena ($E\left[\frac{1}{\bar{X}}\right] > \frac{1}{E[\bar{X}]}$).
2. **Skala wraz ze wzrostem $n$:** Ze wzrostem rozmiaru próby $n$, obciążenie zauważalnie maleje i zbliża się do zera. Potwierdza to, że estymator odwrotności średniej jest asymptotycznie nieobciążony. (Teoretyczne obciążenie dla tego modelu wynosi dokładnie $\frac{\lambda_0}{n-1}$).

---

# Zadanie 31

### (a) Czy empiryczna częstość pokrycia jest bliska 95%? Porównanie szerokości dla znanego i nieznanego $\sigma$

* **Częstość pokrycia:** Empiryczna częstość pokrycia oscyluje wokół 0.95 (ok. 95%), co zgadza się z teorią. Wynika to z faktu, że statystyka $T = \frac{\bar{X} - \mu}{S/\sqrt{n}}$ ma dokładnie rozkład t-Studenta z $n-1$ stopniami swobody, ponieważ próba pochodzi z rozkładu normalnego.
* **Porównanie szerokości:** Średnia szerokość przedziału ufności dla nieznanego $\sigma$ (ok. 30.5 s) jest wyższa niż szerokość dla znanego $\sigma$ (23.52 s). Użycie estymatora $S$ zamiast prawdziwego $\sigma$ wprowadza dodatkową niepewność, dlatego rozkład t-Studenta ma "grubsze ogony" niż rozkład normalny ($t_{0.025}(8) \approx 2.306$ vs $z_{0.025} \approx 1.96$), co wymusza poszerzenie przedziału, aby zachować deklarowany poziom ufności 95%.

### (b) Jaki procent odcinków jest czerwony?

Zgodnie z przyjętym poziomem ufności (95%), średnio **5%** przedziałów (odcinków) na wykresie nie pokrywa prawdziwej wartości parametru $\mu = 260$. W pojedynczym eksperymencie dla 100 prób będzie to liczba oscylująca w okolicach 5 (zazwyczaj od 3 do 7 czerwonych odcinków).

### (c) Częstość pokrycia i szerokość przedziału dla różnych $n \in \{5, 9, 30, 100\}$

1. **Pokrycie empiryczne:** Dla każdej wartości $n$ częstość pokrycia wynosi około 95%. Założenie o normalności rozkładu pozwala precyzyjnie modelować przedział ufności niezależnie od rozmiaru próby (nie musimy tu polegać na przybliżeniach asymptotycznych z Centralnego Twierdzenia Granicznego).
2. **Średnia szerokość:** Zauważamy drastyczny spadek średniej szerokości przedziału w miarę wzrostu rozmiaru próby $n$. Spowodowane jest to dwoma czynnikami: po pierwsze w mianowniku wzoru znajduje się pierwiastek z rozmiaru próby ($\sqrt{n}$), a po drugie kwantyle rozkładu t-Studenta maleją i zbiegają do kwantyli rozkładu normalnego (niepewność estymacji wariancji spada).