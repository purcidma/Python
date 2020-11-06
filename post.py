import requests

# Making a POST request
r = requests.post('https://httpbin.org/post', data ={'now':'test'})

# check status code for response recieved
# success code - 200
print(r)

# print content of request
print(r.json())