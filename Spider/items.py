# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class UrlItem(scrapy.Item):
    """
    主程序提取出页面链接
    """
    view_urls = scrapy.Field()


class ViewItem(scrapy.Item):
    """
    从每个页面中提取出标题、正文、附件
    """
    url = scrapy.Field()  # 网页链接
    title = scrapy.Field()  # 标题
    paragraphs = scrapy.Field()  # 正文
    file_name = scrapy.Field()  # 附件名称
    file_urls = scrapy.Field()  # 附件url


class FileDownloadItem(scrapy.Item):
    """
    下载附件
    """
    file_urls = scrapy.Field()
    files = scrapy.Field()

class EncyclopediaItem(scrapy.Item):

    name = Field()  # 此词条名称
    name_en = Field()  # 英文名称
    name_other = Field()  # 其他名称
    original_url = Field()  # 词条链接
    summary = Field()  # 简介
    source_site = Field()  # 词条来源网站
    edit_number = Field()  # 词条被编辑次数
    fetch_time = Field()  # 词条抓取时间
    update_time = Field()  # 词条更新时间
    item_tag = Field()  # 词条分类标签
    thumbnail_url = Field()  # 词条缩率图url
    album_url = Field()  # 词条缩率图url
    keywords_url = Field()  # 此词条内容所包含的其他词条
    polysemous = Field()  # 多义词，本词条不包含任何内容

    text_content = Field()  # 正文内容，是一个dict
    basic_info = Field()  # 属性内容，是一个dict
    text_image = Field()  # 正文内容中包含的图片dict