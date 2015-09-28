import eventlet
eventlet.monkey_patch()

import logging
import time

from osprofiler import utils

logger = logging.getLogger('osprofiler.%s' % __name__)


class PluginException(Exception):
    """
    Really just a regular exception for now.

    """
    pass


class PluginBase(object):

    def __init__(self, **kwargs):
        self.config = kwargs.get('config', {})
        self.handlers = kwargs.get('handlers', [])
        self.host_id = utils.host_identifier()

    def get_sample(self):
        raise PluginException("Method get_sample not implemented.")

    def execute(self):
        while True:
            try:
                data = self.get_sample()
                for handler in self.handlers:
                    handler.handle(data)
            except Exception:
                logger.exception("Exception running %s.get_sample" %
                                 self.__class__.__name__)

            time.sleep(self.config.get('sample_interval', 5))
