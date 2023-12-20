import tflite_runtime.interpreter as tflite

from io import BytesIO
from urllib import request
import numpy as np

from PIL import Image


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_input(x):
    x /= 255
    return x

interpreter = tflite.Interpreter(model_path='happy-sad-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


def predict(url):
    img = download_image(url)
    img_224 = prepare_image(img, [224,224])
    x = np.array(img_224, dtype='float32')
    X = np.array([x])
    X_prep = preprocess_input(X)

    interpreter.set_tensor(input_index, X_prep)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    float_predictions = preds[0, 0].round(3).tolist() 

    return float_predictions

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    bool_val = 'no'
    if result >= 0.38:
        bool_val = 'yes'
    return { 
        'probability of sad face' : result,
        'is it sad?' : bool_val
    } 