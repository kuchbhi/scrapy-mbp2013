from scrapy.spider import BaseSpider
from apple.items import AppleItem
from scrapy.selector import HtmlXPathSelector
import re

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["apple.com"]
    start_urls = [
        "http://store.apple.com/sg/browse/home/specialdeals/mac"#,
        #"http://store.apple.com/sg/browse/home/specialdeals/mac"
    ]   
    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//td[contains(@class,"specs")]/text()').extract()
       items = []
       for site in sites:
           #print site
           item = AppleItem()
           s = re.sub(r"\W", "", site.encode("utf8"))
           if not "2013" in s:
               continue
           else:
               item['date'] = s 
           item['price'] = site.encode("utf8")
           items.append(item)
       return items