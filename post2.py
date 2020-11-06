import requests
r = requests.post("http://bugs.python.org", data={'number': 14791, 'type': 'behavior', 'action': 'show'})
print(r.status_code, r.reason)

print(r.text[:300] + '...')
