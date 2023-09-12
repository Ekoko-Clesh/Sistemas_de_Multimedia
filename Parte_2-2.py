import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("imagem.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

plt.subplot(1, 2, 1)
plt.title('Imagem Original (RGB)')
plt.imshow(image_rgb)
plt.axis('off')

# Mostre a imagem no espaço de cores HSV
plt.subplot(1, 2, 2)
plt.title('Imagem HSV')
plt.imshow(image_hsv)
plt.axis('off')

plt.show()
