import scrapy

class ProductItem(scrapy.Item):
    breadcrumbs = scrapy.Field()
    image_url = scrapy.Field()
    brand = scrapy.Field()
    product_name = scrapy.Field()
    listing_price = scrapy.Field()
    sizes = scrapy.Field()
    description = scrapy.Field()
    other_images =  scrapy.Field()