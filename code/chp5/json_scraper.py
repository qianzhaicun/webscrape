import requests
import string

PAGE_SIZE = 10

template_url = 'http://example.webscraping.com/places/ajax/search.json?&search_term={}&page_size={}&page={}'
    
#template_url = 'http://example.webscraping.com/places/ajax/search.json?page={}&page_size={}&search_term={}'    
  

countries = set()

for letter in string.ascii_lowercase:
    print('Searching with %s' % letter)
    page = 0
    while True:
        resp = requests.get(template_url.format(letter, PAGE_SIZE,page))
        if resp.status_code != 200:
            break
        data = resp.json()
        print('adding %d more records from page %d' %
              (len(data.get('records')), page))
        for record in data.get('records'):
            countries.add(record['country'])
        page += 1
        if page >= data['num_pages']:
            break

with open('../data/countries.txt', 'w') as countries_file:
    countries_file.write('\n'.join(sorted(countries)))
