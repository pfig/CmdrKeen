from setuptools import setup, find_packages


def long_description_from_readme():
    with open('README.rst') as readme:
        return readme.read()

setup(
    name="CommanderKeen",
    version="0.1",
    packages=find_packages(),
    scripts=['scripts/keen.py'],
    author="Pedro Figueiredo",
    author_email="pfig@me.com",
    description="Commander Keen is a Slack bot with long term memory",
    long_description=long_description_from_readme(),
    license="MIT",
    keywords="slack bot chat",
    url="https://pfig.github.io/CmdrKeen/",
    data_files=[('config', ['cfg/keen.json'])],
    setup_requires=['pytest-runner'],
    install_requires=[
        'slackclient>=0.16',
        'websocket-client>=0.35',
        'requests>=2.9.1',
        'python-daemon>=2.1.1'
    ],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Chat'
    ]
)
