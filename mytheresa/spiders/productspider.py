import scrapy
from mytheresa.spiders.items import ProductItem


class ProductspiderSpider(scrapy.Spider):
    name = "productspider"
    allowed_domains = ["www.mytheresa.com"]
    start_urls = ['https://www.mytheresa.com/int/en/men/dolce-gabbana-custom-2-zero-sneakers-black-p00512377']  # Replace with the actual URL of the page listing multiple products

    def parse(self, response):
        item = ProductItem()
        item = {
                'breadcrumbs' : response.css('div.breadcrumb__item a::text').getall(),
                'image_url' : response.css('div.swiper-slide img::attr(src)').get() ,
                'brand' : response.css('div.product__area__branding__designer a::text').get(),
                'product_name' : response.css('div.product__area__branding__name::text').get(),
                'listing_price' : response.css('span.pricing__prices__price ::text')[1].get(),
                'sizes' : response.css('span.sizeitem__label ::text').getall() ,
                'description' : response.css('div.accordion__body ::text').get().strip(),
                'other_images' : response.css('div.photocarousel__items div.swiper-wrapper div.swiper-slide img::attr(src)').getall(),
        }
        
        # print(item)
        yield item
