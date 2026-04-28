import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

# Ustawienia z treści zadania
d_max = 20
dimensions = np.arange(1, d_max + 1)
N_mc = 100000  # Liczba punktów losowanych w metodzie Monte Carlo

vol_analytical = []
vol_mc = []
ratios = [] # Stosunek objętości hiperkuli do hiperkostki

np.random.seed(42)

for d in dimensions:
    # 1. Objętość otaczającej hiperkostki [-1, 1]^d (długość boku = 2)
    vol_cube = 2**d
    
    # 2. Obliczenie analityczne (wzór: V_d = pi^(d/2) / Gamma(d/2 + 1) * R^d)
    # Ponieważ R=1, pomijamy R^d
    v_analyt = (np.pi**(d / 2)) / gamma(d / 2 + 1)
    vol_analytical.append(v_analyt)
    
    # Obliczenie stosunku
    ratios.append(v_analyt / vol_cube)
    
    # 3. Metoda Monte Carlo
    # Losujemy N_mc punktów z jednorodnego rozkładu na [-1, 1] w d wymiarach
    points = np.random.uniform(-1, 1, size=(N_mc, d))
    
    # Sprawdzamy, które punkty są w hiperkuli (suma kwadratów współrzędnych <= 1^2)
    inside_sphere = np.sum(points**2, axis=1) <= 1
    
    # Objętość = ułamek trafień * objętość całej przestrzeni losowania (hiperkostki)
    v_mc = (np.sum(inside_sphere) / N_mc) * vol_cube
    vol_mc.append(v_mc)

# Rysowanie wykresu objętości
plt.figure(figsize=(10, 6))
plt.plot(dimensions, vol_analytical, marker='o', label='Analityczna', color='blue')
plt.plot(dimensions, vol_mc, marker='x', linestyle='--', label='Monte Carlo', color='red')
plt.xlabel('Wymiar ($d$)')
plt.ylabel('Objętość hiperkuli $V_d$')
plt.title('Objętość hiperkuli o promieniu 1 w zależności od wymiaru')
plt.xticks(dimensions)
plt.legend()
plt.grid(True, linestyle='--')
plt.savefig('objętości_hiperkuli.png', dpi=300, bbox_inches='tight')

# wypisanie stosunku V_d / V_cube, aby odpowiedzieć na pierwsze pytanie
for d, ratio in zip(dimensions, ratios):
    print(f"d={d}: {ratio:.6f}")