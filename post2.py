import requests
#r = requests.post('http://bugs.python.org', data={'@number': 18061, '@type': 'issue', '@action': 'show'})
in_values = {'number' : 18061, 'type': issue, 'action':'show'}
r = requests.post('http://bugs.python.org',data = in_values)
print(r.status_code, r.reason)

print(r.text[:300] + '...')
