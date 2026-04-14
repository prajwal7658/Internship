import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers,models
import json

Image_Size=(224,224)
Batch=32

path=r"C:\Users\Hp\Desktop\Internship Program\fruit\fruit_ripeness_dataset\archive (1)\dataset\dataset\train"

datagen=ImageDataGenerator(rescale=1./255,validation_split=0.2)

train_ds=datagen.flow_from_directory(path,target_size=Image_Size,batch_size=Batch,class_mode="categorical",subset="training")

with open("labels.json", "w") as f:
    json.dump(train_ds.class_indices, f)

print("Labels saved")
val_ds=datagen.flow_from_directory(path,target_size=Image_Size,batch_size=Batch,class_mode="categorical",subset="validation")

model = models.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape = (224,224,3)),
    layers.MaxPool2D(),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPool2D(),
    layers.Conv2D(128,(3,3),activation = 'relu'),
    layers.MaxPool2D(),
    layers.Flatten(),
    layers.Dense(128,activation='relu'),
    layers.Dense(train_ds.num_classes,activation='softmax')])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

model.fit(train_ds,epochs=6,validation_data=val_ds)

model.save('apple_data.h5')
print("Model saved")
