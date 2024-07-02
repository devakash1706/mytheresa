import scrapy
from mytheresa.spiders.items import ProductItem


class AllproductSpider(scrapy.Spider):
    name = "allproduct"
    allowed_domains = ["www.mytheresa.com"]
    start_urls = ['https://www.mytheresa.com/int_en/men/shoes.html']

    def parse(self, response):
        products = response.css('div.item')
        for product in products:
           yield{
               'name' : product.css('div.item__info__header__designer::text').get(),
            #    'price' : product.css('span.pricing__prices__value.pricing__prices__value--discount span::text')[1].get(),
               'description' : product.css('div.item__info__name a::text').get(),
               'url' : product.css('div.item__images__image img::attr(src)').get(),
            #    'discount' : product.css('span.pricing__info__percentage::text').get(),
           }
        

        next_page = response.css('a.pagination__item.pagination__item__text.pagination__item.pagination__item__text--active::attr(href)').extract()[2]
        

      #  print("NEXT---------------------------------------------------------------------------------")
      #  print(next_page)

        if next_page is not None:
           next_page_url = 'https://www.mytheresa.com' + next_page
        #    print("NEXT---------------------------------------------------------------------------------")
        #    print(next_page_url)
           yield response.follow(next_page_url, callback=self.parse) 
