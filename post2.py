import requests

req_body = {'name': 'kyle pogi',
                'salary': '3232323',
                'age': '34'}

response = requests.post('http://dummy.restapiexample.com/api/v1/create', json=req_body)

print(response.status_code)
print(response.json())