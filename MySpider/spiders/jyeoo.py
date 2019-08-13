# -*- coding: utf-8 -*-
import random
import time

import scrapy
from MySpider.items import MyspiderItem


class JyeooSpider(scrapy.Spider):
    name = 'jyeoo'
    # allowed_domains = ['example.com']

    priority = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    cookies = {
        'QS_ED': '8',
        'QS_BK': '6d0fd80e-4c56-4362-8465-74f7f1907795',
        'QS_GD': '10_1',
        'remind_check': '1',
        'jyean': 'CCjUM4e3BTYyewpQAjDDDhD4GZHYOV62_TtC_Ekvxq7d_R0DAecMTzzexWAaWES4Pws9qNN26DIlmzzQVrEzdXeO8c3N-R64Y249-ehI8baCuKZMgmF699oOMC05bBVN0',
        'UM_distinctid': '16c7a566c271b1-0dddb7138e6ff-c343162-100200-16c7a566c28e2',
        'jye_cur_sub': 'bio2',
        'jy': 'DE92C099C2D09DF35AFB6F5D32761AF8D47D72E57B2CE59BD913AEB60D8C5C37FEBFE19DA498BC28A194C61636C62EB371D3F30859C7FA84A6484234BB2DF1CFEE244026C2B8B40F5AC84E2A039271C3AD7FBF0127F1E2E0D8FAE2F43E33073B9031C0C5E8120715867A334C47C7E5C471D208BB0CE2EA68DB6321B3D01D3CA6E62B7FB11DF524543EC83287FDF570049688E521683FA9D20346851098D8880967042ED7885DEB231067559C2FE69CBE640E13D5E9F8163202838EDD0E37E15D7FED05A0BFE8C26BDDC8F181B65DB63495834FF039C05EE2DA6CFF6382158873F2ADA84EF7342947BEC1D73C1317CDDDA5BFB237586894418A629DAD4D6D5F6F907A133F1993801A477AC3C9B23C6F49D23A38BF147B8AB26818C2AA25172CAE9C60C32D12F6D29131B986C951FD4648584F3D370E8B5DB61E24AA6DCB19CB16215A291291D6894C80AE82FC650CF569',
        'jye_notice_yd_notenough': '1|2019/8/12 20:54:56|0|false',
        'remind_check': '1',
        'CNZZDATA2018550': 'cnzz_eid%3D1209574642-1565419771-null%26ntime%3D1565614625',
        'jye_notice_homework': '1|2019/8/12 20:59:38|0|false'
    }

    def start_requests(self):
        urls = ['http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=undefined&r=0.39074550302074007',
                'http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=2&r=0.24845897500311466',
                'http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=3&r=0.39384550302074007',
                'http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=4&r=0.14883797500711466',
                'http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=5&r=0.54888797500711466',
                'http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=6&r=0.64845737500711466',
                'http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=7&r=0.64845787500731466',
                'http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=8&r=0.14845797500311486',
                'http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=9&r=0.34845797530711466',
                'http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=10&r=0.34845397500781466',
                'http://www.jyeoo.com/bio2/ques/partialques?f=1&q=1~~&lbs=&pd=1&pi=11&r=0.74843797500811468']
        for url in urls:
            yield scrapy.Request(priority=self.priority, url=url, cookies=self.cookies, headers=self.headers,
                                 callback=self.parse)

    def parse(self, response):
        questions = response.xpath('//div/ul/li["QUES_LI"]/fieldset/@id').extract()
        for id in questions:
            url = 'http://www.jyeoo.com/bio2/ques/detail/%s' % id
            yield scrapy.Request(priority=self.priority, url=url, cookies=self.cookies, headers=self.headers,
                                 callback=self.parse_detail)

    def parse_detail(self, response):
        question = response.xpath(
            "/html/body/div['content']/div/div['content']/div/div['cl-center']/div/div['detail-item QUES_LI']").extract_first().encode(
            'utf8')
        yield MyspiderItem(content=question)
