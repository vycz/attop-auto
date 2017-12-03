# -*- coding: UTF-8 -*-

# author by : tataki

import requests
import math
import re
import random
import time
import argparse

def tokenify(number):
    tokenbuf = []
    charmap = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*$"
    remainder = number
    while remainder > 0:
        tokenbuf.append(charmap[remainder & 0x3F])
        remainder = math.floor(remainder / 64)
    return "".join(tokenbuf)


def ssid(DWRSESSIONID):
    t = int(time.time())
    r = random.randint(1000000000000000, 9999999999999999)
    return DWRSESSIONID + "/" + tokenify(t) + "-" + tokenify(r)


class attop(object):
    def __init__(self):
        self.session = requests.session()

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'Content-Type': 'text/plain',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.attop.com/'
        }
        self.cookies = {

        }

    def login(self):
        sess = self.session.get('http://www.attop.com/', headers=self.headers)
        if sess.status_code != requests.codes.OK:
            print('打开失败')
            return False
        # for k, v in sess.cookies.items():
        #     self.cookies[k] = v

        # 获得dwrsessid
        params = {
            'callCount': '1',
            'c0-scriptName': '__System',
            'c0-methodName': 'generateId',
            'c0-id': 0,
            'batchId': 0,
            'instanceId': 0,
            'page': '%2Findex.htm',
            'scriptSessionId': '',
            'windowName': ''
        }
        sess = self.session.post('http://www.attop.com/js/ajax/call/plaincall/__System.pageLoaded.dwr',
                                 headers=self.headers, data=params)

        # 得到必要参数
        self.dwrsessid = re.search(r'[0-9a-zA-Z*$]{27}', sess.text).group(0)
        requests.utils.add_dict_to_cookiejar(self.session.cookies, {'DWRSESSIONID' : self.dwrsessid})
        imgheaders = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Referer': 'http://www.attop.com/login_pop.htm',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7'
        }
        sess = self.session.get('http://www.attop.com/image.jpg', headers=imgheaders)
        rand = sess.headers['set-cookie']
        rand = re.search('\d{4}', rand, flags=0).group(0)

        loginparams = {
            'callCount': '1',
            'windowName': '',
            'c0-scriptName': 'zsClass',
            'c0-methodName': 'coreAjax',
            'c0-id': '0',
            'c0-param0': 'string:loginWeb',
            'c0-e1': 'string:%s' % options.username,
            'c0-e2': 'string:%s' % options.password,
            'c0-e3': 'string:%s' % str(rand),
            'c0-e4': 'number:2',
            'c0-param1': 'Object_Object:{username:reference:c0-e1, password:reference:c0-e2, rand:reference:c0-e3, autoflag:reference:c0-e4}',
            'c0-param2': 'string:doLogin',
            'batchId': '4',
            'instanceId': '0',
            'page': '%2Flogin_pop.htm',
            'scriptSessionId': ssid(self.dwrsessid)
        }

        self.headers['Referer'] = 'http://www.attop.com/login_pop.htm'

        self.session.post(
            'http://www.attop.com/js/ajax/call/plaincall/zsClass.coreAjax.dwr',
            headers=self.headers,
            data=loginparams
        )

        self.headers['Referer'] = 'http://www.attop.com/index.htm'
        sess = self.session.get(
            'http://www.attop.com/user/index.htm',
            headers=self.headers
        )

    def doass(self, id):
        id = id
        url = 'http://www.attop.com/js/ajax/call/plaincall/zsClass.dotAjax.dwr'
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'Content-Type': 'text/plain',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://www.attop.com/wk/media_pop.htm?id={0}'.format(id)
        }
        scriptSessionId = ssid(self.dwrsessid)
        params = {
            'callCount': '1',
            'windowName': '',
            'c0-scriptName': 'zsClass',
            'c0-methodName': 'dotAjax',
            'c0-id': '0',
            'c0-param0': 'string:doWkMediaPj',
            'c0-e1': 'number:{0}'.format(id),
            'c0-e2': 'number:3',
            'c0-param1': 'Object_Object:{id:reference:c0-e1, type:reference:c0-e2}',
            'c0-param2': 'string:doWkMediaPj',
            'batchId': '1',
            'instanceId': '0',
            'page': '%2Fwk%2Fmedia_pop.htm%3Fid%3D{0}'.format(id),
            'scriptSessionId': scriptSessionId
        }

        sess = self.session.post(
            url,
            headers=header,
            data=params
        )
        print(sess.text)
        status_code = re.search(r'flag:(\d+),', sess.text).group(1)
        if status_code == '1':
            print("成功")
        elif status_code == '131':
            print("已阅读过")

        print('状态码:'+status_code)
        return True

    def dovideo(self, pageid, batchid):
        url = 'http://www.attop.com/js/ajax/call/plaincall/zsClass.commonAjax.dwr'
        self.headers['Referer']= 'http://www.attop.com/wk/learn.htm?id=48&jid={0}'.format(pageid)
        scriptSessionId = ssid(self.dwrsessid)
        data = {
            'callCount': '1',
            'windowName': '',
            'c0-scriptName': 'zsClass',
            'c0-methodName': 'commonAjax',
            'c0-id': '0',
            'c0-param0': 'string:getWkOnlineNum',
            'c0-e1': 'number:48',
            'c0-e2': 'number:{0}'.format(pageid),
            'c0-param1': 'Object_Object:{bid:reference:c0-e1, jid:reference:c0-e2}',
            'c0-param2': 'string:doGetWkOnlineNum',
            'batchId': batchid,
            'instanceId': '0',
            'page': '%2Fwk%2Flearn.htm%3Fid%3D48%26jid%3D{0}'.format(pageid),
            'scriptSessionId': scriptSessionId
        }
        sess = self.session.post(
            url,
            headers=self.headers,
            data=data
        )
        print(sess.text)

    def get_pages(self, pageid):
        url = 'http://www.attop.com/wk/learn.htm?id='+pageid
        self.headers['Referer']= 'http://www.attop.com/user/study_index.htm'
        sess = self.session.get(
            url,
            headers=self.headers)
        soup = BeautifulSoup(sess.text)
        book_list = soup.select("li[class='nHalf']")
        


def main():

    at = attop()
    at.login()
    if options.mode == 0 or options.mode == 1:
        #完成教程评价
        for id in range(3500,3800):
            print("ID:" + str(id))
            at.doass(id)
            time.sleep(3)
    if options.mode == 0 or options.mode == 2:
        #观看时长
        #http://www.attop.com/wk/learn.htm?id=48&jid=993
        #http://www.attop.com/wk/learn.htm?id=48&jid=1013
        for id in range(options.start, options.end):
            #每批15秒 大概每章10分钟
            for batchid in range(0, 40):
                at.dovideo(id, batchid)
                time.sleep(15)

    if options.mode == 0 or options.mode ==3:
        #刷题
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='to login attop')
    parser.add_argument('-u', '--username', help='attop username', default='')
    parser.add_argument('-p', '--password', help='attop password', default='')
    parser.add_argument('-s', '--start', help='start page', default=0)
    parser.add_argument('-e', '--end', help='end page', default=0)
    parser.add_argument('-m', '--mode', help='1为刷评价,2为刷学习时长,3为刷题,默认全刷', default=0)
    options = parser.parse_args()
    main()
