import requests

r = requests.put('http://localhost:8080/xnat/data/services/auth', data=dict(username='admin', password='admin'))
r.raise_for_status()
cookies = {'JSESSIONID': r.text}

