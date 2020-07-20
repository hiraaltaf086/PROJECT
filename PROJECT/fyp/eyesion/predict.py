from keras.preprocessing.image import  img_to_array, load_img
import numpy as np
from tensorflow.python.keras.models import load_model


def predict_class(url):
    img = load_img(url, target_size=(256, 256))
    img = img_to_array(img)
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    img = img_to_array(img)
    img = img.reshape(1, 256, 256, 3)
    model = load_model('C:/Users/Hira_Altaf/PycharmProjects/practice/fyp/eyesion/Model/DRmodel.h5')
    result = model.predict_on_batch(img)
    res = np.argmax(result)
    return res
