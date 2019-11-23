# _*_ coding:utf8 _*_


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from Spider.items import UrlItem


class UrlSpider(CrawlSpider):
    name = 'url_spider'  # 用于区分不同的 spider，值唯一
    start_urls = ['https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC/128981']  # 启动时进行爬取的url列表
    allowed_domains = ['baike.baidu.com']
    allowed_urls = ['https://baike.baidu.com/item/',]  # 允许的url列表为空，默认都爬取

    # rules = (
    #     # 定义规则，使用链接提取器提取下一页链接
    #     Rule(LinkExtractor(allow='https://baike.baidu.com/item/', restrict_xpaths='//div[@class="para"]/a[@target="_blank"]/@href'),
    #          callback='get_view_urls', follow=False),
    # )
    # rules = (
    #     # 定义规则，使用链接提取器提取下一页链接
    #     Rule(
    #          callback='get_view_urls', follow=False),
    # )
    # 设置 pipeline
    custom_settings = {
        "ITEM_PIPELINES": {
            'Spider.pipelines.UrlPipeline': 300
        },
    }

    # def get_view_urls(self, response):
    #     itemld = ItemLoader(item=UrlItem(), response=response)
    #     itemld.add_value('view_urls', response.url)  # xpath 定位每页中的链接位置
    #     # itemld.add_xpath('view_urls', '//div[@class="para"]/a[@target="_blank"]/@href')  # xpath 定位每页中的链接位置
    #     return itemld.load_item()

    def _parse_response(self, response, callback, cb_kwargs, follow=True):
        itemld = ItemLoader(item=UrlItem(), response=response)
        itemld.add_xpath('view_urls', '//div[@class="para"]/a[@target="_blank"]/@href')  # xpath 定位每页中的链接位置
        return itemld.load_item()