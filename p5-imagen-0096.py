import cv2
# Leer la imagen con cv2 = computer version
img = cv2.imread('perro.jpg')
#Determinar el tipo de imagen numpy.ndarray
print(type(img))
# Mostrar pixeles (554, 554, 3)
print(img.shape)
# mostrando imagen en ventana barra de titulo 'Solovino 0096'
cv2.imshow('Solovino 0096', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()
