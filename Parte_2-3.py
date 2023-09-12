import cv2

# Carregue a imagem
imagem = cv2.imread('imagem.jpg')

# Converta a imagem de BGR (padrão do OpenCV) para RGB
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Converter RGB para YUV
imagem_yuv = cv2.cvtColor(imagem_rgb, cv2.COLOR_RGB2YUV)

# Separe os canais Y, U e V
y, u, v = cv2.split(imagem_yuv)

# Mostre a imagem original
cv2.imshow('Imagem Original', cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))

# canais Y, U e V individualmente
cv2.imshow('Canal Y (Luminância)', y)
cv2.imshow('Canal U (Crominncia Azul)', u)
cv2.imshow('Canal V (Crominância Vermelha)', v)

cv2.waitKey(0)
cv2.destroyAllWindows()
