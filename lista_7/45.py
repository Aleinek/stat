import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

# Ustawienia początkowe z treści zadania
n = 500
dimensions = [1, 2, 5, 10, 50, 100, 500]
R_values = []

np.random.seed(42) # Ustawienie ziarna dla powtarzalności

for d in dimensions:
    # 1. Wygenerowanie 500 punktów z rozkładu jednostajnego [0, 1]^d
    X = np.random.uniform(0, 1, size=(n, d))
    
    # 2. Obliczenie macierzy odległości euklidesowych między wszystkimi parami punktów
    distances = cdist(X, X)
    
    # 3. Zastąpienie zer na przekątnej (odległość do samego siebie) nieskończonością, 
    # aby nie uznać punktu za swojego własnego najbliższego sąsiada
    np.fill_diagonal(distances, np.inf)
    
    # 4. Znalezienie odległości do najbliższego (d_min) i najdalszego (d_max) sąsiada
    d_min = np.min(distances, axis=1)
    
    # Dla d_max zamieniamy przekątną z powrotem na 0 lub -inf (aby nie zaburzała max)
    np.fill_diagonal(distances, -np.inf)
    d_max = np.max(distances, axis=1)
    
    # 5. Obliczenie miary R(d) dla danego wymiaru
    R_d = np.mean((d_max - d_min) / d_min)
    R_values.append(R_d)

# Rysowanie wykresu R(d)
plt.figure(figsize=(8, 5))
plt.plot(dimensions, R_values, marker='o', linestyle='-', color='b')
plt.xlabel('Wymiar (d) - skala logarytmiczna')
plt.ylabel('Wartość $R(d)$')
plt.title('Koncentracja odległości w zależności od wymiaru')
plt.xscale('log') # Skala logarytmiczna na osi X dla lepszej wizualizacji rzędu wielkości
plt.grid(True, which="both", ls="--")
plt.savefig('koncentracja_odleglosci.png', dpi=300, bbox_inches='tight')