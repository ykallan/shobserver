# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
pymysql.install_as_MySQLdb()

class ShangguanPipeline(object):

    def __init__(self):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            database='scrapy',
            user='root',
            passwd='root',
            charset='utf8',
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.conn.ping(reconnect=True)
        self.cursor.execute('''INSERT INTO shobserver(title, summary, resorce, writer, release_time, 
        content, news_type) VALUES(%s, %s, %s, %s, %s, %s, %s)''',
        (item['title'], item['summary'], item['resorce'], item['writer'], item['release_time'],
         item['content'], item['news_type']))

        self.conn.commit()
        return item

    def close(self, spider):
        pass