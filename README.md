# Title

## Description

Simplifies the scrapy items, letting you access the attriburtes via the dot 

The regular bulky way to do it:

    regular_scrapy_item['some_field'] = 42
    print(regular_scrapy_item.get('some_field'))

The simple dot-items way:

    scrapy_dot_item.some_field = 42
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

## Backwards compatibility

scrapy-dot-items are backwards compatible. You can install it into your old project and mix regular and dot style. 
    
    dot_scrapy_item['price'] = 2000  # you can still set and get the items the regular way too
    print(dot_scrapy_item.get('price'))  # prints 2000
    print(dot_scrapy_item.price)  # prints 2000


## For contributers

This project uses pipenv instead of pip. Setup:
- intall pipenv with 'pip install pipenv'
- create a virtual environment using pipenv with 'pipenv shell' in the root directory
- install the dependencies with 'pipenv install'

Attention:
Please install all packages with 'pipenv install <package_name>'. Do NOT use 'pip install ...'.
The same for unistalling 'pipenv uninstall <package_name>'