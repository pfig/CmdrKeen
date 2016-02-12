from setuptools import setup, find_packages
setup(
    name = "CommanderKeen",
    version = "0.1",
    packages = find_packages(),
    scripts = ['scripts/keen.py'],
    author = "Pedro Figueiredo",
    author_email = "pfig@me.com",
    description = "Commander Keen is a Slack bot with long term memory",
    long_description = """Commander Keen at your service

    The finest information sponge in the galaxy.
    """,
    license = "MIT",
    keywords = "slack bot chat",
    url = "https://pfig.github.io/CmdrKeen/",
    data_files = [('config', ['cfg/keen.json'])],
    install_requires = [
        'slackclient>=0.16',
        'websocket-client>=0.35',
        'requests>=2.9.1',
        'python-daemon>=2.1.1'
    ],
    tests_require = [
        'nose>=1.0',
        'tissue>=0.9',
        'nose-cov>=1.0'
    ],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Chat'
    ],
    test_suite = 'nose.collector'
)
