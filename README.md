scrapy-mbp2013
==============

Scrap Apple Store US page for update on 2013 MBPs

This is a basic project using Scrapy running on Windows 8 (Python 2.7)
There are quite a few dependecies missing to get Scrapy working out of the box.

Following sites were helpful:
1. http://www.lfd.uci.edu/~gohlke/pythonlibs/
2. http://doc.scrapy.org/en/latest/intro/install.html
3. https://pypi.python.org/pypi/setuptools/0.9.7#windows

easy_install for Windows was very easy to work with eventually.

spy.py is the place where the web page to be crawled are listed.
The keyword = 2013, to be parsed is also put in the def parse of the same spyder class.

Items class has not been put to maximum use, it can be helpful in saving parsed data in a structured manner.

Tinker, play around at your own risk. Feel free to fork, modify and share...
