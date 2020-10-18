from distutils.core import setup
#the set is used for daily new updattion
setup(
    name = "dailykindle",
    version = "1.0.0",
    description = "Build MOBI documents out of news feeds.",
    url = "http://bitbucket.org/pelletier/dailykindle/",
    author = "Thomas Pelletier",
    author_email = "thomas@pelletier.im",
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    install_requires = ['jinja2','feedparser'],
)
