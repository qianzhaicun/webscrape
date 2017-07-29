import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('test', 'answer')

from diskcache import DiskCache
from advanced_link_crawler import link_crawler
link_crawler('http://example.webscraping.com/places/default/','/(places/default/(index|view))', cache=DiskCache())

from diskcache import RedisCache
from advanced_link_crawler import link_crawler
link_crawler('http://example.webscraping.com/places/default/','/(places/default/(index|view))',cache=RedisCache())


