import logging


logger = logging.getLogger(__name__)


def dot_items_globally():
    def global__setattr__decorator(scrapy__setattr__):
        def dot__setattr__(self, name, value):
            if name.startswith('_'):
                scrapy__setattr__(self, name, value)
            else:
                self.__setitem__(name, value)
        return dot__setattr__

    try:
        import scrapy
        scrapy.Item.__getattr__ = lambda self, name: self.__getitem__(name)
        scrapy.Item.__setattr__ = global__setattr__decorator(scrapy.Item.__setattr__)
        logger.debug('scrapy-dot-items were configured globally')
    except ModuleNotFoundError as e:
        logger.exception(e)
        logger.error('In order to use this library you need to have "scrapy" installed')
