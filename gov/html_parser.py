# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re


def town_parser(html_content, url):
    if html_content is None:
        raise Exception('Html is None')
    html_content = html_content.decode('gbk', 'ignore').encode('gbk')
    soup = BeautifulSoup(html_content, 'html.parser', from_encoding='gbk')
    # 找出“西湖街道”、“留下街道”等<tr>标签
    url_trs = soup.find_all('tr', 'towntr')
    # 生成包含乡镇街道名称、下级url、乡镇街道级12位编码的元组的列表
    urls = [(tr.contents[1].get_text() if tr.contents[1].a is None else tr.contents[1].a.get_text(),
             None if tr.contents[0].a is None else url + tr.contents[0].a['href'],
             tr.contents[0].get_text() if tr.contents[0].a is None else tr.contents[0].a.get_text())
            for tr in url_trs]
    return urls


class HtmlParser(object):
    # 第一个参数：需要解析的html代码
    # 第二个参数：用于拼装下级页面的url
    def province_parser(self, html_content, url):
        if html_content is None:
            raise Exception('Html is None')
        # 将html代码从gb2312转码到utf-8
        html_content = html_content.decode('gb2312', 'ignore').encode('gbk')
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='gbk')
        # 找出“北京市”、“天津市”等<td>标签
        url_tds = soup.find_all('a', href=re.compile(r'\d+.html'))
        # 生成包含省名称、下级url、省编码（在后续拼装区级页面需要用到）的元组的列表
        urls = [(td.get_text(), url + td['href'], td['href'].replace('.html', '')) for td in url_tds]
        return urls

    def city_parser(self, html_content, url):
        if html_content is None:
            raise Exception('Html is None')
        html_content = html_content.decode('gb2312', 'ignore').encode('gbk')
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='gbk')
        # 找出“杭州市”、“温州市”等<tr>标签
        url_trs = soup.find_all('tr', 'citytr')
        # 生成包含市名称、下级url、市级12位编码的元组的列表
        urls = [(tr.contents[1].get_text() if tr.contents[1].a is None else tr.contents[1].a.get_text(),
                 None if tr.contents[0].a is None else url + tr.contents[0].a['href'],
                 tr.contents[0].get_text() if tr.contents[0].a is None else tr.contents[0].a.get_text())
                for tr in url_trs]
        return urls

    def county_parser(self, html_content, url):
        if html_content is None:
            raise Exception('Html is None')
        html_content = html_content.decode('gb2312', 'ignore').encode('gbk')
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='gbk')
        # 找出“上城区”、“下城区”等<tr>标签
        url_trs = soup.find_all('tr', 'countytr')
        # 生成包含区名称、下级url、区级12位编码的元组的列表
        urls = [(tr.contents[1].get_text() if tr.contents[1].a is None else tr.contents[1].a.get_text(),
                 None if tr.contents[0].a is None else url + tr.contents[0].a['href'],
                 tr.contents[0].get_text() if tr.contents[0].a is None else tr.contents[0].a.get_text())
                for tr in url_trs]
        return urls
