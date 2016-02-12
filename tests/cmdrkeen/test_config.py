import pytest

from cmdrkeen.config import Config


def test_throws_exception_file_not_found():
    with pytest.raises(IOError):
        Config('no-such-file.json')


def test_throws_exception_invalid_json(invalid_json):
    with pytest.raises(ValueError):
        Config(str(invalid_json))


def test_requires_slack_token(config_no_token):
    with pytest.raises(ValueError):
        Config(str(config_no_token))


def test_requires_data_file(config_no_data_file):
    with pytest.raises(ValueError):
        Config(str(config_no_data_file))


def test_correct_defaults(config_use_defaults):
    config = Config(str(config_use_defaults))

    assert config.file == str(config_use_defaults)
    assert config.slack_token == 'xoxb-super-sekrit-token'
    assert config.data_file == 'frobnitzer'
    assert config.debug is True
    assert config.background is True
    assert config.log_file is None
    assert config.plugins is None


def test_full_configuration(config_full):
    config = Config(str(config_full))

    assert config.file == str(config_full)
    assert config.slack_token == 'xoxb-super-sekrit-token'
    assert config.data_file == 'frobnitzer'
    assert config.debug is False
    assert config.background is False
    assert config.log_file == 'keen.log'

    plugins = config.plugins
    assert type(plugins) is dict
    assert len(plugins) is 1
    assert 'weather' in plugins
    assert type(plugins['weather']) is dict
    assert len(plugins['weather']) is 1
    assert 'default_location' in plugins['weather']
    assert plugins['weather']['default_location'] == 'London, UK'


@pytest.fixture(scope='session')
def config_use_defaults(tmpdir_factory):
    use_defaults = """{
        "slack_token": "xoxb-super-sekrit-token",
        "data_file": "frobnitzer"
    }
    """
    fn = tmpdir_factory.mktemp('cfg').join('use-defaults.json')
    fn.write(use_defaults)

    return fn


@pytest.fixture(scope='session')
def config_full(tmpdir_factory):
    full_config = """{
        "slack_token": "xoxb-super-sekrit-token",
        "data_file": "frobnitzer",
        "debug": false,
        "background": false,
        "log_file": "keen.log",
        "plugins": {
            "weather": {
                "default_location": "London, UK"
            }
        }
    }
    """
    fn = tmpdir_factory.mktemp('cfg').join('keen.json')
    fn.write(full_config)

    return fn


@pytest.fixture(scope='session')
def config_no_token(tmpdir_factory):
    no_token = """{
        "data_file": "frobnitzer"
    }
    """
    fn = tmpdir_factory.mktemp('cfg').join('no-token.json')
    fn.write(no_token)

    return fn


@pytest.fixture(scope='session')
def config_no_data_file(tmpdir_factory):
    no_token = """{
        "slack_token": "xoxb-super-sekrit-token"
    }
    """
    fn = tmpdir_factory.mktemp('cfg').join('no-data-file.json')
    fn.write(no_token)

    return fn


@pytest.fixture(scope='session')
def invalid_json(tmpdir_factory):
    bad_json = """{
        foo: {"bar"}
    }
    """
    fn = tmpdir_factory.mktemp('cfg').join('invalid-json.json')
    fn.write(bad_json)

    return fn
