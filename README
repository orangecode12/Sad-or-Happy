# Sad or Happy face classification

In this project, two models were trained to classify images of people into two categories: sad and happy. I've took part of this dataset from kaggle.
The full dataset with 6 categories: https://www.kaggle.com/datasets/sujaykapadnis/emotion-recognition-dataset
The redused dataset with 2 categories can be downloaded as:
git clone https://github.com/orangecode12/Data_for_capstone1

I wanted to use pre-trained CNN, but at first look, all models from https://keras.io/api/applications/ performed terribly. They didn't even predict a person in the images. That is why I decided to find some keras-based models for person recognition. As a result, I found vgg-face, which is not supported now)) I tried to use it, but it was extremely slow. So I decided to train a custom CNN. I've reached the 0.843 accuracy on the validation dataset. Then I deployed it as a Lambda function, and became very inspired, that it works. On the last day, I trained the Xception base model too and it reached 0.862 accuracy on the validation dataset. I also deployed it to the AWS Lambda. Now you can test both models. 

The output format is a bit different:
- The custom CNN model returns the probability of a Sad face, thus all faces with a probability higher than 0.38 are meant Sad. Others are Happy. 
- The Xception model returns the probabilities of both classes

### For testing:
- find a sad or happy face
- cut it: the face should occupy 80 percent of the image or more, and the image should be a rectangle (250x250, for example)
- save it as .jpg
- create a URL for it

You can test both models using the links:
custom CNN:	https://j1td1a2v7d.execute-api.eu-west-1.amazonaws.com/test/predict
xception:	https://t22jqto1bc.execute-api.eu-west-1.amazonaws.com/test-it/predict


### Instructions for creating docker container:
docker build -t sad_or_happy_image .
docker run -it --rm -p 8080:8080 sad_or_happy_image:latest

Instructions for pushing to aws ecr:
aws ecr create-repository --repository-name sad_or_happy_images
docker login -u AWS -p $(aws ecr get-login-password --region eu-west-1) 019406907121.dkr.ecr.eu-west-1.amazonaws.com
docker tag sad_or_happy_image:latest 019406907121.dkr.ecr.eu-west-1.amazonaws.com/sad_or_happy_images:sad_or_happy_model_001
docker push 019406907121.dkr.ecr.eu-west-1.amazonaws.com/sad_or_happy_images:sad_or_happy_model_001

After that, I created a Lambda function and API Gateway via AWS web interface. 

Remember I've spent much more time developing a custom CNN model (notebook_train.ipynb), so the research is deeper.


### Files in this project:
- requirements.txt  - contains all dependencies for training the model
- convert_h5_to_tflite.py - convert .h5 to .tflite
- test.py - testing script

- For the custom CNN:
	- notebook_train.ipynb 		- training and fine-tuning the model
	- happy-sad-model.tflite 	- converted to .tflite
	- lambda_function_v1.py 	- lambda function
	- Dockerfile_v1				- docker for building lambda function

- For the xception model:
	- notebook_xception.ipynb 	- training and fine-tuning the model
	- happy-sad-model-v2.tflite - converted to .tflite
	- lambda_function.py 		- lambda function
	- Dockerfile				- docker for building lambda function

#### IMPORTANT!
to reproduce custom CNN deployment rename lambda_function_v1.py to lambda_function.py and Dockerfile_v1	to Dockerfile

I also wanted to publish the models in .h5 format, but they are too heavy for regular github operations, so I'll publish them later
- model_v3_50_0.843.h5		- final model .h5
- xception_v4_1_10_0.862.h5 - final model .h5


## Thank your for taking time to evaluate!


## If you have any questions, please, don't hesitate to ask me via LinkedIn. The link is below.

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mariia-gornostaeva/)