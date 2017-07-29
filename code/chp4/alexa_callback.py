import csv
from zipfile import ZipFile
from io import TextIOWrapper, BytesIO
import requests


class AlexaCallback:
    def __init__(self, max_urls=500):
        self.max_urls = max_urls
        self.seed_url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
        self.urls = []

    def __call__(self):
        z = ZipFile("top-1m.csv.zip", "r")
        for filename in z.namelist(  ):
            csv_filename = filename
            with z.open(csv_filename) as csv_file:
                for _, website in csv.reader(TextIOWrapper(csv_file)):
                    self.urls.append('http://' + website)
                    if len(self.urls) == self.max_urls:
                        break
                    
                    
'''
z = zipfile.ZipFile("top-1m.csv.zip", "r")

for filename in z.namelist(  ):
    print 'File:', filename,
    bytes = z.read(filename)
    print 'has',len(bytes),'bytes'

'''                    
