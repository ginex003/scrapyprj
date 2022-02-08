import scrapy
from ..items import OlxItem


class OlxSpider(scrapy.Spider):
    name = 'olx'
    start_urls = [
        'https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723'
    ]

    def parse(self, response, **kwargs):

        items = OlxItem()

        all_list_items = response.css('li.EIR5N')

        for itemss in all_list_items:
            item_name = itemss.css('._2tW1I::text').extract()
            price = itemss.css('._89yzn::text').extract()
            location = itemss.css('.tjgMj::text').extract()

            items['item_name'] = item_name
            items['price'] = price
            items['location'] = location

            yield items

    # price = response.css('._89yzn::text').extract()
    # yield {'price': price}
