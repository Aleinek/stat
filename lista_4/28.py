import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

lambda_0 = 2.0
# W numpy funkcja exponential przyjmuje parametr skali (scale = 1/lambda)
scale_param = 1.0 / lambda_0 

# --- (a) i (b) ---
n_a = 30
x_a = np.random.exponential(scale=scale_param, size=n_a)

lambdas = np.linspace(0.5, 4.0, 100)
sum_x = np.sum(x_a)

# Funkcja log-wiarygodności
log_lik = n_a * np.log(lambdas) - lambdas * sum_x

# Estymator MNW
lambda_hat = 1.0 / np.mean(x_a)
max_log_lik = n_a * np.log(lambda_hat) - lambda_hat * sum_x

plt.figure(figsize=(10, 5))
plt.plot(lambdas, log_lik, label=r'$\ell(\lambda)$', color='blue')
plt.axvline(x=lambda_hat, color='red', linestyle='--', label=f'MNW: {lambda_hat:.2f}')
plt.scatter([lambda_hat], [max_log_lik], color='red')
plt.title('Log-wiarygodność dla n=30')
plt.legend()
plt.savefig('fig/28_log_likelihood.png')

# --- (c) ---
n_values_c = [5, 30, 200]

plt.figure(figsize=(10, 5))
for n in n_values_c:
    x_c = np.random.exponential(scale=scale_param, size=n)
    # Wzór przeskalowany: l(lambda)/n = log(lambda) - lambda * mean(x)
    log_lik_scaled = np.log(lambdas) - lambdas * np.mean(x_c)
    plt.plot(lambdas, log_lik_scaled, label=f'n={n}')

plt.axvline(x=lambda_0, color='black', linestyle=':', label=f'Prawdziwe lambda={lambda_0}')
plt.title(r'Przeskalowana log-wiarygodność $\ell(\lambda)/n$')
plt.legend()
plt.savefig('fig/28_scaled_log_likelihood.png')

# --- (d) ---
B = 1000
n_values_d = [5, 30, 200]

for n in n_values_d:
    # Generowanie B estymatorów dla danego n
    lambda_hats = [1.0 / np.mean(np.random.exponential(scale=scale_param, size=n)) for _ in range(B)]
    bias = np.mean(lambda_hats) - lambda_0
    print(f"n={n:<3} | Średnie MNW: {np.mean(lambda_hats):.4f} | Obciążenie: {bias:.4f}")