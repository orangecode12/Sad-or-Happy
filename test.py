import requests

#url = 'https://t22jqto1bc.execute-api.eu-west-1.amazonaws.com/test-it/predict'#'http://localhost:8080/2015-03-31/functions/function/invocations'

url = 'https://j1td1a2v7d.execute-api.eu-west-1.amazonaws.com/test/predict' #'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url':'https://github.com/orangecode12/Data_for_capstone1/blob/main/me.jpg?raw=true'}

result = requests.post(url, json=data).json()
print(result)
