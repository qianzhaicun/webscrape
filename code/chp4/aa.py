import requests
resp = requests.get('http://example.webscraping.com/places/ajax/search.json?&search_term=A&page_size=10&page=0')
print(resp.json())