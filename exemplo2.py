import cv2

classificador = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('pessoas//mprj-01.JPG')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)


facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.05, minNeighbors=11, minSize=(10,10))
print(len(facesDetectadas))
print(facesDetectadas)


for (x, y, l, a) in facesDetectadas:
    print(x, y, l, a)
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 1)

cv2.imshow("Faces detectadas", imagem)
cv2.waitKey()
