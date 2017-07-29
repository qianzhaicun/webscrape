import requests
from lxml import etree

def scrape_callback(url, html):
    if url.endswith('.xml'):
        # Parse the sitemap XML file
        resp = requests.get(url)
        tree = etree.fromstring(resp.content)
        links = [e[0].text for e in tree]
        return links
    else:
        # Add scraping code here
        pass

if __name__ == "__main__":
    from threaded_crawler import threaded_crawler
    sitemap = 'http://www.gap.com/products/sitemap_index.xml'
    threaded_crawler(sitemap, '[gap.com]*',scraper_callback=scrape_callback)