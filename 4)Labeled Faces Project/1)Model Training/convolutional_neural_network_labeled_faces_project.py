# -*- coding: utf-8 -*-
"""Convolutional Neural Network-Labeled Faces Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13HII1F-Xrfxlq8Wqs7xUSOqkaRsTjDdo
"""

#LFW (Labeled Faces in the Wild) verisetinden yüz tanıma üzerine bir cnn
#modeli eğiteceğiz. Bu model için klasör içerisindeki görsellerin oludğu klasör
#zipini import edelim

from google.colab import files

# ZIP dosyasını yükle
uploaded = files.upload()

import zipfile

# Zip dosyasını "lfw_faces" klasörüne açıyoruz
with zipfile.ZipFile("lfw-deepfunneled.zip", 'r') as zip_ref:
    zip_ref.extractall("lfw_faces")

print("ZIP dosyası başarıyla çıkarıldı.")

#Klasörde kaç kişi ve kaç görsel olduğunu kontrol etme

import os

klasor_yolu="lfw_faces/lfw-deepfunneled"
kisi_listesi=os.listdir(klasor_yolu)

print(f"Toplam kişi sayısı: {len(kisi_listesi)}")

for kisi in kisi_listesi[:5]:
  foto_sayisi=len(os.listdir(os.path.join(klasor_yolu,kisi)))

  print(f"{kisi}: {foto_sayisi} fotoğraf")

#bir kişinin kaç fotoğrafı olduğunu bulma

#bılarının az sayıda görseli mevcut bunları ayıracğız modelin iyi eğitilebilmesi için

#En az 15 görseli olan kişileri seçip ayırma

import shutil
kaynak_dizin= "lfw_faces/lfw-deepfunneled"

hedef_dizin="filtered_faces"

os.makedirs(hedef_dizin,exist_ok=True)
#yeni klasör oluşturma

for kisi in os.listdir(kaynak_dizin):
  #kişileri dolaşarak yeterli fortoğrafı olan kişileri hedef dizine atayacağız

  kisi_klasoru=os.path.join(kaynak_dizin,kisi)
  resimler= os.listdir(kisi_klasoru)


  if( len(resimler)) >=15: # en az 15 görseli varsa

       hedef_kisi_klasoru= os.path.join(hedef_dizin,kisi)

       os.makedirs(hedef_kisi_klasoru, exist_ok=True)


       for resim in resimler:
        #görselleri yeni klasöre kopyalama

        kaynak_resim = os.path.join(kisi_klasoru, resim)
        shutil.copy(kaynak_resim,hedef_kisi_klasoru)



print("Yeterli verisi olan kişiler kopyalandı")

#filtrelenmiş Verilerin Kontrolü

import os

filtreli_dizin="filtered_faces"

kisi_listesi=os.listdir(filtreli_dizin)

print(f"Yeni kişi sayısı (15+ görseli olan kişiler):{len(kisi_listesi)}")


for kisi in kisi_listesi[:5]:
  foto_sayisi= len(os.listdir(os.path.join(filtreli_dizin,kisi)))

  print(f"{kisi}: {foto_sayisi} görsel")

#ilk 5 kişinin kaç görsel olduğunu gösterme

#Eğitim ve Test Verileri Ayrımı


import os
import random
import shutil
from sklearn.model_selection import train_test_split

kaynak_dizin = "filtered_faces"
train_dizin= "data_split/train"
val_dizin = "data_split/val"

os.makedirs(train_dizin , exist_ok=True)
os.makedirs(val_dizin, exist_ok=True)

#her kişi için işlemi yapacağız görsellerinin bir kısmı  eğitim
#bir kısmı doğrulama verisi olacak

for kisi in os.listdir(kaynak_dizin):
  resimler = os.listdir(os.path.join(kaynak_dizin, kisi))

  train_imgs, val_imgs = train_test_split(resimler, test_size=0.2, random_state=42)
  #eğitim ve doğrulama olarak ayrılması

  os.makedirs(os.path.join(train_dizin,kisi),exist_ok=True)
  os.makedirs(os.path.join(val_dizin, kisi),exist_ok=True)
  #kişilerin ayrılan görselleri için klasörler oluşturma

   #eğitim verilerini kalsörlerine kopyalama
  for img in train_imgs:
    shutil.copy(os.path.join(kaynak_dizin,kisi,img),
                os.path.join(train_dizin,kisi,img))

  #Doğrulama verilerini klasörlerine kopyalama

  for img in val_imgs:
    shutil.copy(os.path.join(kaynak_dizin,kisi,img),
                os.path.join(val_dizin, kisi, img))


print("Veri başarıyla eğitim ve doğrulama için ayrıldı")

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

#ImageDataGenerator ile Veri Okuma

train_datagen=ImageDataGenerator(rescale =1./255)#0-255 arası görselleri 1-0 arası
#normalize eder
val_datagen=ImageDataGenerator(rescale=1./255)

#Eğitim verisini okuma

train_generator = train_datagen.flow_from_directory(
    "data_split/train", #okuyacağı klasör dizini
    target_size=(100,100),#resimlerin geleceği boyut
    batch_size=32,
    class_mode='categorical' #sınıflandırma türü
)

#doğrulama verisini okuma

val_generator= val_datagen.flow_from_directory(
    "data_split/val",#okuyacağı klasör dizini
    target_size=(100,100), #resimleri boyutu
    batch_size=32,
    class_mode='categorical' # sınıflandırma türü
)

#CNN Modeli Kurulumu ve Eğitimi

model=tf.keras.Sequential()
#sıfırdan cnn modeli inşası


model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))

#ilk konvolüsyon katmani özellik çıkarımı
model.add(MaxPooling2D(pool_size=(2,2)))
#boyutu küçültür,bilgi yoğunluğunu arttırr

model.add(Conv2D(64,(3, 3),activation='relu'))
#2. katman
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(128,(3, 3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
#3. katman

model.add(Flatten())
#modeli düzleştirme 2D den 1D ye

model.add(Dense(128,activation='relu')) #tam bağlantılı katman
model.add(Dropout(0.5))#overfittingi önlemek için


model.add(Dense(train_generator.num_classes, activation='softmax'))
#çıkış katmanı

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
#modeli derleme


model.summary()#modelin özetini çıkarma

#Modeli Eğitme

from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(monitor='val_loss',patience=3, restore_best_weights=True)

history = model.fit(
    train_generator,
    epochs=15 ,
    validation_data=val_generator,
    callbacks=[early_stop]
)

model.save("lfw_yuz_tanima_modeli.h5")

#Modeli indirme

from google.colab import files

files.download("lfw_yuz_tanima_modeli.h5")