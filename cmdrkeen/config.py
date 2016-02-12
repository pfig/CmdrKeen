import json
import logging


logger = logging.getLogger(__name__)


class Config(object):
    """A configuration for a Commander Keen bot

    This will read and parse a configuration file containing parameters for
    a Commander Keen Slack bot.

    Configurations are made of a set of JSON-encoded variables. Commander Keen
    understands the following parameters (variables marked with *
    are mandatory)::

        * ``slack_token``: the bot's token (*)
        * ``data_file``: the path for the SQLite3 file containing factoids (*)
        * ``background``: whether to run as a daemon, boolean (default: true)
        * ``log_file``: the path for the log file (default: None)
        * ``debug``: whether to run in debug mode, boolean (default: true)
        * ``plugins``: an object defining the plugins to load (default: none)

    The ``plugins`` object is a map of name -> configuration. Commander Keen
    will try to load the corresponding package from ``cmdrkeen.plugins.name``
    and configure it accordingly, by passing the configuration object to the
    constructor.

    As an example, consider the following configuration stored in the file
    ``keen.json``::

        {
            "slack_token": "xoxb-super-sekrit-token",
            "data_file": "brain.sqlite3",
            "background": false,
            "plugins": {
                "weather": {
                    "default_location": "London, UK"
                }
            }
        }

        This would run the bot in the foreground and try to load the weather
        plugin from ``cmdrkeen.plugins.weather``, with the given configuration
        object.
    """
    def __init__(self, file_path):
        """Constructor

        Builds a configuration object given a file path.

        :param file_path: the path to the configuration file.
        :returns: a ``Config`` object initialised with the given file path.
        """
        self.file = file_path
        self.slack_token = None
        self.data_file = None
        self.background = True
        self.log_file = None
        self.debug = True
        self.plugins = None

        self.__configure_from_file(file_path)

    def __configure_from_file(self, file_path):
        """Configure the bot from a file

        Reads ``file_path`` and configures the bot accordingly.
        """
        with open(file_path, 'r') as config:
            try:
                json_cfg = json.loads(config.read())
            except Exception as e:
                logger.error('Error reading configuration ({}): {}'.format(
                    file_path, e))
                raise e

            slack_token = json_cfg.get('slack_token', None)
            data_file = json_cfg.get('data_file', None)
            if not (slack_token and data_file):
                logger.error('Slack token and data file required')
                raise ValueError

            self.slack_token = slack_token
            self.data_file = data_file

            self.__configure_optional(json_cfg)

    def __configure_optional(self, json_cfg):
        """Configure optional parameters

        Given a configuration object, configures the optional
        parameters for the bot.
        """
        self.background = json_cfg.get('background', True)
        self.debug = json_cfg.get('debug', True)
        self.log_file = json_cfg.get('log_file', None)
        self.plugins = json_cfg.get('plugins', None)
