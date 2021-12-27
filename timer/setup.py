from setuptools import setup

VERSION = "1.0.0"
DESCRIPTION = "A simple Timer class"
LONG_DESCRIPTION = "A simple, but featureful, Timer class with context manager and decorator support"

setup(
    name = "timer",
    version = VERSION,
    author = "Edoardo Baldi",
    author_email = "hi@edobld.me",
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages = ["timer"],
    install_requires = [],
    classifiers = [],
)
