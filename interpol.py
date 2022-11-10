import numpy as np

def interpol(x: list, y: list) -> list:
    # Função que recebe uma sequência de n pontos (x, y) e retorna os
    # coeficientes do polinômio de grau n-1 que os interpola.
    n = len(x) # quantidade de pontos
    A = np.zeros([n, n])
    b = np.array(y)
    # Monta a matriz A:
    for i in range(n):
        for j in range(n):
            A[i, j] = x[i] ** j
    # Multiplica A e b
    return np.linalg.solve(A, b).tolist()
