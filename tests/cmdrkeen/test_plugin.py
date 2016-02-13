import sys


from cmdrkeen.plugin import Plugin


def test_loads_plugin():
    config = {
        'default_location': 'London, UK'
    }
    plugin = Plugin('weather', config, plugin_dir='/usr/local/keen/plugins')
    assert '/usr/local/keen/plugins' in sys.path
    assert plugin.name == 'weather'
    assert plugin.module.config is config


def test_load_error_handles_exception():
    plugin = Plugin('frobnitzer')
    assert plugin.module is None
