# opencv kütüphanesini içe aktaralım
# ...

import cv2

# matplotlib kütüphanesini içe aktaralım
# ...
import matplotlib.pyplot as plt

# resmi siyah beyaz olarak içe aktaralım
# ...

img = cv2.imread("odev1.jpg",0)

# resmi çizdirelim
# ...
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"),plt.title("Original")


# resmin boyutuna bakalım
# ...
print(img.shape)


# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
# ...
# ...
img = cv2.resize(img, (int(img.shape[1]*4/5), int(img.shape[0]*4/5)))
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"),plt.title("Resized")


# orijinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim
# ...
# ...
cv2.putText(img, "Kopek",(210,300), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
cv2.imshow("Text",img)


# orijinal resmin 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim
# ...
# ...
_, thres_img = cv2.threshold(img, thresh = 50, maxval = 255, type = cv2.THRESH_BINARY)  
plt.figure(), plt.imshow(thres_img, cmap = "gray"), plt.axis("off"),plt.title("Threshold")


# orijinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
# ...
# ...

gauss = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gauss, cmap = "gray"), plt.axis("off"),plt.title("Gaussian")

# orijinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim
# ...
# ...

laplacian = cv2.Laplacian(img, ddepth = cv2.CV_64F) #64F resimler için 
plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"),plt.title("Laplacian")

# orijinal resmin histogramını çizdirelim
# ...
# ...

img = cv2.imread("odev1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

color = ["b","g","r"]
plt.figure()

for i, c in enumerate(color):
    hist = cv2.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0,256])
    plt.plot(hist, color = c)

















