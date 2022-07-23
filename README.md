# Title

## Description

Simplifies the scrapy items, letting you access the attriburtes via the dot 

    regular_scrapy_item['some_field'] = 42 # the regular bulky way to do it
    print(regular_scrapy_item.get('some_field'))

    scrapy_dot_item.some_field = 42  # the simple dot-items way
    print(scrapy_dot_item.some_field)

## Installation

    pip install scrapy-dot-items

## Usage

### Apply to a single scrapy item class

You can add functionality with the dot_item decorator to a single class
    
    from scrapy_dot_items import dot_item

    @dot_item
    class RealEstateItem(scrapy.Item):
        price = scrapy.Field()

    dot_scrapy_item = RealEstateItem()

    dot_scrapy_item.price = 1000
    print(dot_scrapy_item.price)  # prints 1000


### Apply to all scrapy items 

You can apply this functionality globally


    from scrapy_dot_items import dot_items_globally

    dot_items_globally()  # now every scrapy.Item class will have this functionality

    class RealEstateItem(scrapy.Item):
        price = scrapy.Field()

    dot_scrapy_item = RealEstateItem()

    dot_scrapy_item.price = 1000
    print(dot_scrapy_item.price)  # prints 1000