#make a POST request
import requests
dictToSend = {'question': 'what is the answer?'}
response_to_request = requests.post('http://localhost:5000/post/reply/misc/address', json=dictToSend)
print('response from server:', response_to_request.text)
dictFromServer = response_to_request.json()
