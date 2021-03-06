# -*- coding: utf-8 -*-
import MySQLdb
import MySQLdb.cursors


class MysqlHandler(object):
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="code_spider", charset="gbk")

    # 第一个参数：1-插入一个省数据；2-市数据；3-区数据；4-乡镇街道数据
    # 第二个参数：省市区街道名称
    # 第三个参数：上级的id，注意省没有上级id
    # 第四个参数：市区街道的12位行政区划编码
    def insert(self, level, name, pre_id, code):
        insert_id = 0
        try:
            cursor = self.db.cursor()
            if level == 1:
                cursor.execute("select id from province where province_name=(%s)", [name])
                result = cursor.fetchone()
                if result:
                    return insert_id
                cursor.execute('INSERT INTO province (province_name) VALUES (%s)', [name])
            elif level == 2:
                cursor.execute('INSERT INTO city (city_name, province_id, city_code) VALUES (%s, %s, %s)'
                               , [name, pre_id, code])
            elif level == 3:
                cursor.execute('INSERT INTO county (county_name, city_id, county_code) VALUES (%s, %s, %s)'
                               '', [name, pre_id, code])
            else:
                cursor.execute('INSERT INTO town (town_name, county_id, town_code) VALUES (%s, %s, %s)'
                               , [name, pre_id, code])
            insert_id = cursor.lastrowid
            self.db.commit()
        except Exception as e:
            Exception('MySQL ERROR:', e.message)
        # 返回存储后的id
        return insert_id

    # 最后需要调用该方法来关闭连接
    def close(self):
        self.db.close()
