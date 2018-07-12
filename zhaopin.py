__author__ = 'xianda'
import requests
import json
import time
from lxml import etree


class JobSpider(object):
    def __init__(self):
        self.url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500&jl=530&sm=0&p={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/55.0.2883.87 Safari/537.36'}

    def parser(self):
        job_list = []
        for i in range(1, 5):
            data = requests.get(self.url.format(i), headers=self.headers)
            s = etree.HTML(data.text)
            file = s.xpath('//*[@id="newlist_list_content_table"]/table')
            for tr in file:
                item = {
                    'job': tr.xpath('./tr[1]/td[1]/div/a/text()'),
                    'rate': tr.xpath('./tr[1]/td[2]/span/text()'),
                    'com': tr.xpath('./tr[1]/td[3]/a[1]/text()'),
                    'salary': tr.xpath('./tr[1]/td[4]/text()'),
                    'add': tr.xpath('./tr[1]/td[5]/text()')
                }
                job_list.append(item)
            time.sleep(0.1)
        return job_list

    def save(self, job_list):
        with open('job_list.txt', 'a', encoding='utf8') as f:
            for jobs in job_list:
                f.write(json.dumps(jobs, ensure_ascii=False))
                f.write('\n')
        print('保存成功！')

    def run(self):
        job_list = self.parser()
        self.save(job_list)


if __name__ == '__main__':
    job = JobSpider()
    job.run()

