# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib2
import time


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            raise Exception('url is None')
        # 输出当前进行下载的url
        print(url)
        # 伪装浏览器
        request = urllib2.Request(url, None, {'Cookie': 'AD_RS_COOKIE=20081945',
                                                     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                                                                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                   'Chrome/69.0.3497.100 Safari/537.36'})
        try:
            response = urllib2.urlopen(request)
            print(response.getcode())
            if response.getcode() != 200:
                # 线程暂停5秒
                time.sleep(5)
                # 递归调用
                return self.download(url)
            else:
                return response.read()
        except urllib2.HTTPError as e:
            print(e)
            time.sleep(5)
            return self.download(url)