import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layes,models
import json

Image_Size=(224,224)
Batch=32

path=r"C:\Users\Hp\Desktop\Internship Program\DATASETS\moth\train"

datagen=ImageDataGenerator(rescale=1./255,validation_split=0.2)

train_ds=datagen.flow_from_directory(path,target_size=Image_Size,batch_size=Batch,class_mode="categorical",subset="training")

with open("labels.json","w") as f:
    json.dump(train_ds.class_indices,f)
    
print("Labels saved")
val_ds=datagen.flow_from_directory(path,target_size=Image_Size,batch_size=Batch,class_mode="categorical",subset="validation")

model=models.Sequential([
    layers.Conv2D()
])