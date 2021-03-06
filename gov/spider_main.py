# -*- coding: utf-8 -*-
from time import sleep
from mysql_handler import MysqlHandler
from html_downloader import HtmlDownloader
from html_parser import HtmlParser, town_parser
import traceback


class CodeSpider(object):
    def __init__(self):
        # 实例化其他模块类
        self.mysql_handler = MysqlHandler()
        self.html_downloader = HtmlDownloader()
        self.html_parser = HtmlParser()
        # 爬取起点url
        self.root_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html'
        # 用于后续url的拼接
        self.split_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
        # 省页面列表
        self.province_url_list = []
        # 市页面列表
        self.city_url_list = []
        # 区页面列表
        self.county_url_list = []
        # 乡镇、街道页面列表
        self.town_url_list = []

    def craw(self):
        try:
            # 记录正在下载、解析的url，便于分析错误
            downloading_url = self.root_url
            html_content = self.html_downloader.download(downloading_url)
            # 第一个参数：需要解析的html代码
            # 第二个参数：用于url拼接的url
            self.province_url_list = self.html_parser.province_parser(html_content, self.split_url)
            for province_name, province_url, province_code in self.province_url_list:
                # 第一个参数：1-插入一个省数据；2-市数据；3-区数据；4-乡镇街道数据
                # 第二个参数：省市区街道名称
                # 第三个参数：上级的id，注意省没有上级id
                # 第四个参数：市区街道的行政区划编码
                province_id = self.mysql_handler.insert(1, province_name, None, None)
                if province_id == 0:
                    continue
                sleep(5)
                # 记录正在下载、解析的url，便于分析错误
                downloading_url = province_url
                try:
                    html_content = self.html_downloader.download(downloading_url)
                except Exception as e:
                    sleep(10)
                    print e, "重新下载 省份"
                    html_content = self.html_downloader.download(downloading_url)
                self.city_url_list = self.html_parser.city_parser(html_content, self.split_url)
                for city_name, city_url, city_code in self.city_url_list:
                    city_id = self.mysql_handler.insert(2, city_name, province_id, city_code)
                    # 例如直辖市没有下级页面
                    if city_url is None:
                        continue
                    # 记录正在下载、解析的url，便于分析错误
                    downloading_url = city_url
                    try:
                        html_content = self.html_downloader.download(downloading_url)
                    except Exception as e:
                        sleep(10)
                        print e, "重新下载 直辖市"
                        html_content = self.html_downloader.download(downloading_url)

                    self.county_url_list = self.html_parser.county_parser(html_content, self.split_url + province_code + "/")
                    for county_name, county_url, county_code in self.county_url_list:
                        county_id = self.mysql_handler.insert(3, county_name, city_id, county_code)
                        if county_url is None:
                            continue
                        # 记录正在下载、解析的url，便于分析错误
                        downloading_url = county_url
                        try:
                            html_content = self.html_downloader.download(downloading_url)
                        except Exception as e:
                            sleep(10)
                            print e, "重新下载乡镇"
                            html_content = self.html_downloader.download(downloading_url)
                        self.town_url_list = town_parser(html_content, self.split_url)
                        for town_name, town_url, town_code in self.town_url_list:
                            # 输出抓取到的乡镇街道的名称、链接（实际不需要）、编号代码
                            if town_code == "130408100000":
                                print town_url
                            print(town_name, town_url, town_code)
                            self.mysql_handler.insert(4, town_name, county_id, town_code)
            self.mysql_handler.close()
        except Exception as e:
            print('[ERROR] Craw Field!Url:', downloading_url, 'Info:', e)
            # 利用traceback定位异常
            traceback.print_exc()

if __name__ == '__main__':
    obj_spider = CodeSpider()
    obj_spider.craw()