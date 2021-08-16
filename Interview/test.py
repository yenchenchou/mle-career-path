import scrapy


class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
        "https://www.myvisajobs.com/Reports/2018-Green-Card-Sponsor.aspx"
    ]

    def parse(self, response):
        table = response.xpath("//*[@class='tbl']").getall()
        print(table)


if __name__ == "__main__":
    crawler = MySpider()
    crawler.parse()
