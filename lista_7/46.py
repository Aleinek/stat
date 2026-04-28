import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Ustawienia początkowe z treści zadania
n_train = 1000
n_test = 500
dimensions = [1, 2, 5, 10, 20, 50, 100]
accuracies = []

np.random.seed(42) # Dla powtarzalności wyników

for d in dimensions:
    # 1. Wygenerowanie zbioru treningowego z rozkładu normalnego N(0,1)
    X_train = np.random.randn(n_train, d)
    
    # 2. Obliczenie norm (długości) wektorów i wyznaczenie promienia r_d (mediana)
    norms_train = np.linalg.norm(X_train, axis=1)
    r_d = np.median(norms_train)
    
    # 3. Przypisanie etykiet: 1 jeśli norma <= r_d, w przeciwnym razie 0
    y_train = (norms_train <= r_d).astype(int)
    
    # 4. Wygenerowanie niezależnego zbioru testowego
    X_test = np.random.randn(n_test, d)
    norms_test = np.linalg.norm(X_test, axis=1)
    
    # Etykiety testowe wyznaczamy używając promienia r_d ze zbioru treningowego!
    y_test = (norms_test <= r_d).astype(int)
    
    # 5. Wytrenowanie modelu KNN z K = 1
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    
    # 6. Ocena dokładności na zbiorze testowym
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

# Rysowanie wykresu
plt.figure(figsize=(8, 5))
plt.plot(dimensions, accuracies, marker='o', linestyle='-', color='r', label='Dokładność 1-NN')
plt.axhline(y=0.5, color='gray', linestyle='--', label='Klasyfikator losowy (0.5)')
plt.xlabel('Wymiar (d) - skala logarytmiczna')
plt.ylabel('Dokładność (Accuracy)')
plt.title('Degradacja metody KNN w przestrzeniach wysokowymiarowych')
plt.xscale('log') # Skala logarytmiczna na osi X dla lepszej czytelności
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('degradacja_knn.png', dpi=300, bbox_inches='tight')