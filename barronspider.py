import scrapy

class BarronSpider(scrapy.Spider):
    name = 'barronspider'
    start_urls = ['https://www.memrise.com/course/1185021/gre-barrons-3500-with-sentences-no-typing/']

    def parse(self, response):
        links = response.css("a.level")
        
        for link in links:
           url = 'https://www.memrise.com' + link.xpath("@href").extract_first()
           print(url)\