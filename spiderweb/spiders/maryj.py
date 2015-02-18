from scrapy.spider import Spider
from scrapy.selector import Selector

class MySpider (Spider):
	name ="hulk"
	allowed_domains =["www.whiteoliveseo.co.uk"]
	start_urls = ["http://www.whiteoliveseo.co.uk/about"]

	def parse(self, response):
		hxs = 	response.selector.xpath('//p')
		titles = response.selector.xpath('//a')
		for titles in titles:
			title = response.xpath("p").extract()
			link = response.xpath("a/@href").extract()
			print title, link