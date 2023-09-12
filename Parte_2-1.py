import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregue a imagem em cores
imagem = cv2.imread('imagem.jpg')

# Divida a imagem em seus canais de cor (BGR)
canal_azul, canal_verde, canal_vermelho = cv2.split(imagem)

# Calcule o histograma do canal vermelho
histograma_vermelho = cv2.calcHist([canal_vermelho], [0], None, [256], [0, 256])

# Mostre o histograma
plt.figure(figsize=(8, 6))
plt.title('Histograma do Canal Vermelho')
plt.xlabel('Valor do Pixel')
plt.ylabel('Número de Pixels')
plt.plot(histograma_vermelho)
plt.xlim([0, 256])
plt.grid(True)
plt.show()
