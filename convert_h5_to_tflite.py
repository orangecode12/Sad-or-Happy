import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('xception_v4_1_10_0.862.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with open('happy-sad-model-v2.tflite', 'wb') as f_out:
    f_out.write(tflite_model)