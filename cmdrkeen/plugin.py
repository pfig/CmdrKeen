import logging

from cmdrkeen.job import Job


logger = logging.getLogger(__name__)


class Plugin(object):
    """A Commander Keen plugin

    Bot plugins are loaded upon initialisation, if the configuration file
    contains any references to them, e.g.::

        {
            // ...
            "plugins": {
                "weather": {
                    "default_location": "London, UK"
                }
            }
        }

    When a bot configures itself with the above configuration, it will try to
    load the Weather plugin from the ``cmdrkeen.plugins.weather`` package,
    with the configuration object::

        {
            "default_location": "London, UK"
        }

    If for any reason this fails, the bot will log the failure and continue.
    """
    base_package = 'cmdrkeen.plugins'

    def __init__(self, name, config=None):
        self.name = name
        self.jobs = []
        self.outputs = []

        try:
            self.module = __import__(self.base_package + '.' + name)
        except ImportError as e:
            logger.error('Failed to load plugin {}: {}'.format(name, e))
            self.module = None
            return
        self.module.config = config

        if 'setup' in dir(self.module):
            self.module.setup()

        logger.info('Plugin {} loaded'.format(name))

    def register_jobs(self):
        if 'crontable' in dir(self.module):
            for t, fn in self.module.crontable:
                self.jobs.append(Job(t, eval('self.module.' + fn)))
