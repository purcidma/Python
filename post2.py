import requests
r = requests.post("http://bugs.python.org", read data={'number': 28062, 'type': 'issue', 'action': 'show'})
print(r.status_code, r.reason)

print(r.text[:300] + '...')
