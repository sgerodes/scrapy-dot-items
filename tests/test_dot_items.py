import scrapy
from src.scrapy_dot_items import dot_item, dot_items_globally


def test_dot_items_mixin():
    @dot_item
    class RealEstateItem(scrapy.Item):
        price = scrapy.Field()
        area = scrapy.Field()

    dot_scrapy_item = RealEstateItem()

    # test getters
    dot_scrapy_item['price'] = 1000
    assert dot_scrapy_item.price == 1000

    # test setters
    dot_scrapy_item.area = 70
    assert dot_scrapy_item['area'] == 70


def test_dot_items_global():
    dot_items_globally()

    class RealEstateItem(scrapy.Item):
        price = scrapy.Field()
        area = scrapy.Field()

    dot_scrapy_item = RealEstateItem()

    # test getters
    dot_scrapy_item['price'] = 1000
    assert dot_scrapy_item.price == 1000

    # test setters
    dot_scrapy_item.area = 70
    assert dot_scrapy_item['area'] == 70
