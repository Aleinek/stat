import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

# Ustawienia początkowe z treści zadania
n = 200
degrees = np.arange(1, 16)
mse_cv_values = []
mse_train_values = []

np.random.seed(42) # Dla powtarzalności wyników

# 1. Wygenerowanie danych
x = np.random.uniform(0, 1, n)
epsilon = np.random.normal(0, 0.3, n) # Odchylenie standardowe to 0.3 (wariancja 0.3^2)
y = np.sin(2 * np.pi * x) + epsilon

# scikit-learn oczekuje dwuwymiarowej tablicy cech X
X = x.reshape(-1, 1)

for d in degrees:
    # 2. Utworzenie modelu regresji wielomianowej stopnia d
    model = make_pipeline(PolynomialFeatures(d), LinearRegression())
    
    # 3. Obliczenie błędu walidacji krzyżowej (5-fold CV)
    # cross_val_score z 'neg_mean_squared_error' zwraca wartości ujemne, więc je odwracamy
    scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
    mse_cv = -np.mean(scores)
    mse_cv_values.append(mse_cv)
    
    # 4. Obliczenie błędu treningowego na całym zbiorze
    model.fit(X, y)
    y_pred = model.predict(X)
    mse_train = mean_squared_error(y, y_pred)
    mse_train_values.append(mse_train)

# Znalezienie optymalnego stopnia d
optimal_d = degrees[np.argmin(mse_cv_values)]

# Rysowanie wykresu
plt.figure(figsize=(10, 6))
plt.plot(degrees, mse_train_values, marker='o', label='Błąd treningowy (MSE)')
plt.plot(degrees, mse_cv_values, marker='s', label='Błąd walidacji krzyżowej ($MSE_{CV}$)')
plt.axvline(x=optimal_d, color='red', linestyle='--', label=f'Optymalne $d$ = {optimal_d}')

plt.xlabel('Stopień wielomianu ($d$)')
plt.ylabel('Błąd średniokwadratowy (MSE)')
plt.title('Błąd treningowy i walidacji krzyżowej w zależności od stopnia wielomianu')
plt.xticks(degrees)
# Używamy skali logarytmicznej dla osi Y, ponieważ dla d > 10 błąd CV zazwyczaj "eksploduje"
plt.yscale('log') 
plt.legend()
plt.grid(True, linestyle='--')
plt.savefig('regresja_wielomianowa.png', dpi=300, bbox_inches='tight')