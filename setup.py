from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'Sharevia - Single Line Multi Device Sharing Tool'
LONG_DESCRIPTION = 'A python based library that let user create a sharing platform where multiple device can connect and access shared files.'

# Setting up
setup(
    name="sharevia",
    version=VERSION,
    author="Neetish Singh(AAYS Analytics)",
    author_email="<neetishsingh97@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'server','fastapi','shareit','xender','multi','smart','wifi','secure'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)