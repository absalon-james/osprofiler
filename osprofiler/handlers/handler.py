import utils

class Handler(object):

    def __init__(self, *args, **kwargs):
        self.config = kwargs.get('config')