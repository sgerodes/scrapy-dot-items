

def dot_item(scrapy_item_class):
    """
    A decorator for scrapy items
    @dot_item
    class YourScrapyItem(scrapy.Item):
        your_field = scrapy.Field()
        ...

    :param scrapy_item_class: a class that inherits from scrapy.Item
    """
    class ScrapyDotItem(scrapy_item_class):
        def __getattr__(self, key):
            return super().__getitem__(key)

        def __setattr__(self, name, value):
            print(f'{name}, {value}')
            print(name.startswith('_'))
            if not name.startswith('_'):
                super().__setitem__(name, value)
            else:
                super().__setattr__(name, value)
    return ScrapyDotItem
