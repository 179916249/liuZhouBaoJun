#coding:utf-8
import requests
import time
from loginM.login import LoginClass
import re

# login = LoginClass()        #实例化登陆成功


class CarInfoClass(LoginClass):

    def __init__(self):
        super(CarInfoClass,self).__init__()

    def getCarsInfo(self):
        """
        获取客户车辆单页列表
        :return:
        """

        def getCarsInfo(curCode):
            # 客户详情信息
            kfcarxx1 = open(r'kfcar/kfxx/kfcarxx1.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx1.read(), )
            kfcarxx1.close()

            kfcarxx2 = open(r'kfcar/kfxx/kfcarxx2d.dll', 'rb')
            #返回详细信息
            res = self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx2.read(), )
            kfcarxx2.close()
            print(res.content.decode('GBK', 'ignore'))

            kfcarxx3 = open(r'kfcar/kfxx/kfcarxx3.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx3.read(), )
            kfcarxx3.close()

            kfcarxx4 = open(r'kfcar/kfxx/kfcarxx4.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx4.read(), )
            kfcarxx4.close()

            kfcarxx5 = open(r'kfcar/kfxx/kfcarxx5.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx5.read(), )
            kfcarxx5.close()

            kfcarxx6 = open(r'kfcar/kfxx/kfcarxx6.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx6.read(), )
            kfcarxx6.close()

            kfcarxx7 = open(r'kfcar/kfxx/kfcarxx7.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx7.read(), )
            kfcarxx7.close()

            kfcarxx8 = open(r'kfcar/kfxx/kfcarxx8.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx8.read(), )
            kfcarxx8.close()

            kfcarxx9 = open(r'kfcar/kfxx/kfcarxx9.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx9.read(), )
            kfcarxx9.close()

            kfcarxx10 = open(r'kfcar/kfxx/kfcarxx10.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx10.read(), )
            kfcarxx10.close()

            kfcarxx11 = open(r'kfcar/kfxx/kfcarxx11.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx11.read(), )
            kfcarxx11.close()

            kfcarxx12 = open(r'kfcar/kfxx/kfcarxx12.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx12.read(), )
            kfcarxx12.close()

            kfcarxx13 = open(r'kfcar/kfxx/kfcarxx13.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx13.read(), )
            kfcarxx13.close()

            kfcarxx14 = open(r'kfcar/kfxx/kfcarxx14.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx14.read(), )
            kfcarxx14.close()

            kfcarxx15 = open(r'kfcar/kfxx/kfcarxx15.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx15.read(), )
            kfcarxx15.close()

            kfcarxx16 = open(r'kfcar/kfxx/kfcarxx16.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx16.read(), )
            kfcarxx16.close()

            kfcarxx17 = open(r'kfcar/kfxx/kfcarxx17.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx17.read(), )
            kfcarxx17.close()

            kfcarxx18 = open(r'kfcar/kfxx/kfcarxx18.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx18.read(), )
            kfcarxx18.close()

            kfcarxx19 = open(r'kfcar/kfxx/kfcarxx19.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx19.read(), )
            kfcarxx19.close()

            kfcarxx20 = open(r'kfcar/kfxx/kfcarxx20.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx20.read(), )
            kfcarxx20.close()

            kfcarxx21 = open(r'kfcar/kfxx/kfcarxx21.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx21.read(), )
            kfcarxx21.close()

            kfcarxx22 = open(r'kfcar/kfxx/kfcarxx22.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx22.read(), )
            kfcarxx22.close()

            kfcarxx23 = open(r'kfcar/kfxx/kfcarxx23.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx23.read(), )
            kfcarxx23.close()

            kfcarxx24 = open(r'kfcar/kfxx/kfcarxx24.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx24.read(), )
            kfcarxx24.close()

            kfcarxx25 = open(r'kfcar/kfxx/kfcarxx25.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx25.read(), )
            kfcarxx25.close()

            kfcarxx26 = open(r'kfcar/kfxx/kfcarxx26.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx26.read(), )
            kfcarxx26.close()

            kfcarxx27 = open(r'kfcar/kfxx/kfcarxx27.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx27.read(), )
            kfcarxx27.close()

            kfcarxx28 = open(r'kfcar/kfxx/kfcarxx28.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx28.read(), )
            kfcarxx28.close()

            kfcarxx29 = open(r'kfcar/kfxx/kfcarxx29d.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx29.read(), )
            kfcarxx29.close()

            kfcarxx30 = open(r'kfcar/kfxx/kfcarxx30.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarxx30.read(), )
            kfcarxx30.close()


        def pageCarsInfo(page):
            """
            根据页码获取当页的list
            :param page:
            :return:
            """
            kfcarlist_1 = open(r'kfcar/kfcarlist_1.dll', 'rb')
            res = self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarlist_1.read(), )
            kfcarlist_1.close()
            res.content.decode('utf-8', 'ignore')
            # print(res.content.decode('utf-8', 'ignore'))
            time.sleep(1)
            kfcarlist0 = open(r'kfcar/kfcarlist0.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarlist0.read(), )
            kfcarlist0.close()
            time.sleep(1)
            kfcarlist1 = open(r'kfcar/kfcarlist1.dll', 'rb')
            self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarlist1.read(), )
            kfcarlist1.close()
            time.sleep(1)
            kfcarlist2 = open(r'kfcar/kfcarlist2.dll', 'rb')
            kfcarlist2 = kfcarlist2.read().replace(b'\x001\x000\x000\x00,\x001\x00,\x004\x006\x003',
                                                   b'\x001\x000\x000\x00,\x00'+b'%s'%(bytes(str(page),encoding='utf-8'))+b'\x00,\x004\x006\x003')

            res = self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarlist2, )
            kfcarlist1.close()
            bData = res.content
            bData = bData.replace(b'\n',b'').replace(b'\t',b'').replace(b'\r',b'')
            print(bData)
            # curCodes = re.findall(b'\x14(\d{8,11})',bData,re.M)     #当前页客户编号列表
            # curNmes = re.findall(b'\x06(.+?)\x00',bData,re.M)
            # curList = re.findall(b'\x14\d{8,11}.+?U\x00',bData,re.S)
            curList = re.findall(b'\x14\d{8,11}.+?UU\x00 | \x14\d{8,11}.+?\x00\x00\x00\x00\?\x00\x00\x00\x00\x00\x00',bData)
            print(curList,)
            print(len(curList))
            # print('=' * 100)
            # print(res.content.decode('GBK', 'ignore'))
            for i in curList:
                # print(i)
                print(i.decode('GBK','ignore').replace('\n','').replace('\t','').replace('\r',''))
                time.sleep(1)




        time.sleep(3)
        """
        
        for i in range(1,21):
            print(i,'='*100)
            pageCarsInfo(i)
            time.sleep(1)
        """

        # pageCarsInfo(3)
        # time.sleep(1)
        # getCarsInfo(3)


        kfcarlistout = open(r'kfcar/kfcarlistout.dll', 'rb')        #退出客户车辆列表菜单
        self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfcarlistout.read(), )
        kfcarlistout.close()

    def testGetCus(self):
        """
        测试获取1页的客户信息
        :return:
        """
        # 打开客户管理-客户信息
        kfxx1 = open('../loginM/dll/kfxx1.dll', 'rb')
        self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfxx1.read(), )
        kfxx1.close()

        kfxx2 = open('../loginM/dll/kfxx2.dll', 'rb')
        self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfxx2.read(), )
        kfxx2.close()

        kfxx3 = open('../loginM/dll/kfxx3.dll', 'rb')
        self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfxx3.read(), )
        kfxx3.close()

        kfxx4 = open('../loginM/dll/kfxx4.dll', 'rb')
        self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfxx4.read(), )
        kfxx4.close()

        kfxx5 = open('../loginM/dll/kfxx5.dll', 'rb')
        self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfxx5.read(), )
        kfxx5.close()

        kfxx6 = open('../loginM/dll/kfxx6.dll', 'rb')
        self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfxx6.read(), )
        kfxx6.close()

        # 客户信息-查询page<1>
        kfxxcx1 = open('../loginM/dll/kfxxcx1.dll', 'rb')
        curs = self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfxxcx1.read(), )
        kfxxcx1.close()

        kfxxcx2 = open('../loginM/dll/kfxxcx2.dll', 'rb')
        self.session.post('http://47.98.81.205/httpsvr/httpsrvr.dll', headers=self.headers, data=kfxxcx2.read(), )
        kfxxcx2.close()

        return curs.content

if __name__ == "__main__":
    # time.sleep(10)
    car = CarInfoClass()
    # car.getCarsInfo()
    print(car.testGetCus().decode('utf-8','ignore'))
    car.logout()

