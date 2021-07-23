import scrapy

class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
        'https://www.myvisajobs.com/Reports/2021-Green-Card-Sponsor.aspx'
    ]

    def parse(self, response):
        for h3 in response.xpath('//h3').getall():
            print()