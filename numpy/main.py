import numpy as np

# a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
# A = np.array(a)

# print(A)

# dim = A.ndim 
# print(dim) #! 2 -> Perchè è un array bidimensionale (righe e colonne)

# shape = A.shape 
# print(shape) #! (3, 3) -> 3 righe e 3 colonne

# size = A.size 
# print(size) #! 9 -> 9 elementi
 
# el12 = A[1, 2] 
# print(el12) #! 23

# print(A[0][0:2]) #! [11 12]

# print(A[0:2, 2]) #! [13, 23] -> Prende gli elementi 2 delle colonne  0 e 1

# X = np.array([[1, 0], [0, 1]]) #* Creazione di un np.array direttamente
# print(X)

# Y = np.array([[2, 1], [1, 2]]) 
# print(Y)

# Z = X + Y 
# print(Z)

# V = np.array([[1, 2], [2, 1]]) 
# W = 2 * V 
# print(W) #! [[2, 4], [4, 2]] -> Funziona solo con gli np.array (non con semplici array di Python)
# U = V * W
# print(U) #! [[2, 8], [8, 2]]

# A = np.array([[0, 1, 1], [1, 0, 1]])
# B = np.array([[1, 1], [1, 1], [-1, 1]])
# C = np.dot(A,B) #? Prodotto dei 2 array -> Non capisco il calcolo -> Approfondire prodotto matriciale in un futuro spero lontano, anzi spero mai
# print(C)
# print(np.sin(C)) #! Seno di C


Z = np.array([[1,1],[2,2],[3,3]]) 
print(Z.T) #! Trasposta della matrice Z