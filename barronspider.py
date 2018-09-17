import scrapy

class BarronSpider(scrapy.Spider):
    name = 'barronspider'
    start_urls = ['https://www.memrise.com/course/1185021/gre-barrons-3500-with-sentences-no-typing/']

    def parse(self, response):
        links = response.css("a.level")

        for link in links:
           url = 'https://www.memrise.com' + link.xpath("@href").extract_first()
           print(url)
           
           request = scrapy.Request(url,callback=self.parse_card)
           yield request
           break

    def parse_card(self, response):
        words = response.css('div.thing.text-text div.col_a.col.text div.text')
        file = open("barronWordList.txt","a")
        for word in words:
            word_text = word.xpath('text()').extract_first()
            print(word_text)
            file.write(word_text)
            file.write("\r\n")

        file.close()

