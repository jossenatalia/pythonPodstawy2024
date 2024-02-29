import requests

key = 'test_RC3K27cmSgqEQOeqz27FiVQez_L1CeJAAsSiWeDK2zZWsEGmEFDPTGaS3eG6_5xO'
url = 'https://demo.reportportal.io/'
page = requests.get(url, params={'key': key})

print(page.text)

json = page.json()
