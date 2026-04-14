import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Ustawienie ziarna losowości dla powtarzalności wyników
np.random.seed(42)

# Zdefiniowane parametry zadania
mu_0 = 200
sigma = 18
alpha = 0.05
# Wartość krytyczna z_alpha/2 dla testu dwustronnego (ok. 1.96)
z_crit = norm.ppf(1 - alpha/2) 

# --- Funkcje pomocnicze ---

def teoretyczna_moc(mu, n):
    """Zwraca teoretyczną moc testu ze wzoru z poprzedniego zadania."""
    delta = (mu - mu_0) / (sigma / np.sqrt(n))
    # Pełny wzór na moc (oba ogony rozkładu)
    moc = (1 - norm.cdf(z_crit - delta)) + norm.cdf(-z_crit - delta)
    return moc

def empiryczna_moc(mu, n, B=1000):
    """Generuje B prób o rozmiarze n i zwraca odsetek odrzuceń H0."""
    # Generujemy B prób po n obserwacji
    proby = np.random.normal(mu, sigma, size=(B, n))
    
    # Obliczamy średnią dla każdej z B prób
    srednie = np.mean(proby, axis=1)
    
    # Obliczamy statystykę testową Z dla każdej próby
    Z = (srednie - mu_0) / (sigma / np.sqrt(n))
    
    # Sprawdzamy, w ilu przypadkach |Z| > z_crit
    odrzucenia = np.sum(np.abs(Z) > z_crit)
    
    # Zwracamy empiryczną moc (proporcję odrzuceń)
    return odrzucenia / B


# ==========================================
# (a) Empiryczny błąd I rodzaju (mu = 200, n = 36)
# ==========================================
print("--- Punkt (a) ---")
n_a = 36
blad_1_rodzaju = empiryczna_moc(mu=mu_0, n=n_a, B=1000)
print(f"Empiryczny błąd I rodzaju (dla mu=200): {blad_1_rodzaju:.3f} (czyli {blad_1_rodzaju*100}%)")


# ==========================================
# (b) Empiryczna vs Teoretyczna moc dla wybranych mu
# ==========================================
print("\n--- Punkt (b) ---")
wartosci_mu = [202, 205, 210, 220]

print(f"{'mu':<5} | {'Moc Empiryczna':<15} | {'Moc Teoretyczna':<15}")
print("-" * 42)
for mu in wartosci_mu:
    moc_emp = empiryczna_moc(mu, n_a, B=1000)
    moc_teo = teoretyczna_moc(mu, n_a)
    print(f"{mu:<5} | {moc_emp:<15.3f} | {moc_teo:<15.3f}")


# ==========================================
# (c) Wykres krzywej mocy empirycznej i teoretycznej
# ==========================================
# Zakres mu od 185 do 215, weźmy punkty co 1 jednostkę
zakres_mu = np.arange(185, 216)

# Obliczenia
moc_empiryczna_lista = [empiryczna_moc(mu, n_a, B=1000) for mu in zakres_mu]
moc_teoretyczna_lista = [teoretyczna_moc(mu, n_a) for mu in zakres_mu]

plt.figure(figsize=(10, 5))
# Rysujemy punkty empiryczne
plt.plot(zakres_mu, moc_empiryczna_lista, 'o', label='Moc empiryczna (symulacja)', alpha=0.7)
# Rysujemy ciągłą linię teoretyczną
plt.plot(zakres_mu, moc_teoretyczna_lista, '-', label='Moc teoretyczna', linewidth=2)

plt.title('Punkt (c): Krzywa mocy testu (n=36)')
plt.xlabel('Prawdziwa wartość średniej ($\mu$)')
plt.ylabel('Moc testu')
plt.axvline(mu_0, color='red', linestyle='--', label='$\mu_0 = 200$ (H0)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('krzywa_mocy.png', dpi=300, bbox_inches='tight')


# ==========================================
# (d) Krzywe mocy dla różnych rozmiarów próby n
# ==========================================
wartosci_n = [9, 36, 100]
gesty_zakres_mu = np.linspace(185, 215, 200) # Gęstszy zakres dla gładkich linii

plt.figure(figsize=(10, 5))

for n in wartosci_n:
    moc_dla_n = [teoretyczna_moc(mu, n) for mu in gesty_zakres_mu]
    plt.plot(gesty_zakres_mu, moc_dla_n, label=f'n = {n}')

plt.title('Punkt (d): Wpływ rozmiaru próby na moc testu')
plt.xlabel('Prawdziwa wartość średniej ($\mu$)')
plt.ylabel('Moc testu')
plt.axvline(mu_0, color='red', linestyle='--', alpha=0.5)
plt.axhline(alpha, color='gray', linestyle=':', label=r'$\alpha = 0.05$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('krzywe_mocy.png', dpi=300, bbox_inches='tight')