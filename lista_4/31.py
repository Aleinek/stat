import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# --- Funkcja główna ---
def conf_interval(mu, sigma, n):
    x = np.random.normal(mu, sigma, n)
    x_mean = np.mean(x)
    s = np.std(x, ddof=1) # Estymator odchylenia standardowego (nieobciążony, ddof=1)
    
    # Kwantyl rozkładu t-Studenta dla 95% przedziału ufności (alpha=0.05 -> 1-alpha/2 = 0.975)
    t_quant = stats.t.ppf(0.975, df=n-1)
    
    margin = t_quant * (s / np.sqrt(n))
    ci_lower = x_mean - margin
    ci_upper = x_mean + margin
    
    covers_mu = (ci_lower <= mu <= ci_upper)
    width = 2 * margin
    
    return (ci_lower, ci_upper), covers_mu, width

# --- (a) ---
mu_0, sigma_0 = 260.0, 18.0
n_a = 9
B = 1000

covers_count_a = 0
widths_a = []

for _ in range(B):
    _, covers, width = conf_interval(mu_0, sigma_0, n_a)
    covers_count_a += covers
    widths_a.append(width)

empirical_coverage_a = covers_count_a / B
avg_width_a = np.mean(widths_a)

# Teoretyczna szerokość, gdy sigma jest znana (używamy rozkładu normalnego)
z_quant = stats.norm.ppf(0.975)
known_sigma_width = 2 * z_quant * (sigma_0 / np.sqrt(n_a))

print(f"(a) Empiryczne pokrycie: {empirical_coverage_a:.3f}")
print(f"(a) Średnia szerokość (nieznane sigma): {avg_width_a:.2f}")
print(f"(a) Szerokość (znane sigma): {known_sigma_width:.2f}\n")

# --- (b) ---
n_intervals = 100
plt.figure(figsize=(8, 10))
red_count = 0

for i in range(n_intervals):
    (ci_lower, ci_upper), covers, _ = conf_interval(mu_0, sigma_0, n_a)
    color = 'blue' if covers else 'red'
    if not covers:
        red_count += 1
    plt.plot([ci_lower, ci_upper], [i, i], color=color)

plt.axvline(x=mu_0, color='black', linestyle='--', label=f'Prawdziwe $\\mu$ = {mu_0}')
plt.title(f'100 przedziałów ufności (kolor czerwony: {red_count}%)')
plt.xlabel('Czas (s)')
plt.ylabel('Numer iteracji')
plt.legend()
plt.savefig('fig/31_conf_intervals.png')

# --- (c) ---
n_values_c = [5, 9, 30, 100]

print("(c) Zestawienie dla różnych wartości n:")
for n in n_values_c:
    covers_count_c = 0
    widths_c = []
    for _ in range(B):
        _, covers, width = conf_interval(mu_0, sigma_0, n)
        covers_count_c += covers
        widths_c.append(width)
        
    emp_cov = covers_count_c / B
    avg_w = np.mean(widths_c)
    print(f"n={n:<3} | Pokrycie empiryczne: {emp_cov:.3f} | Średnia szerokość: {avg_w:.2f}")