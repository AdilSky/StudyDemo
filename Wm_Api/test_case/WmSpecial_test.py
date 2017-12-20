# FileName : WmSpecial_test.py
# Author   : Adil
# DateTime : 2017/12/18 19:38
# SoftWare : PyCharm

import unittest,requests

import os,json
from Wm_Api.common import Excel
from Wm_Api import readConfig as RC


class WmApiTest(unittest.TestCase):
    '''未名Api测试'''

    # 定义一个类变量
    cartId = 0
    cartIds = []
    orderId= 0
    orderIds = []

    @classmethod
    def setUpClass(cls):
        cls.yiyaoURL = 'https://www.yiyao.cc'
        cls.bijiaURL =  'http://bijia.yiyao.cc'
        cls.SpecialURL = 'http://sales-app-api.assistant'
        # 实例化 Ex
        cls.Ex = Excel.Excel()

    @classmethod
    def tearDownClass(cls):

        pass


    def tempLogin(self):
        SpecialURL = 'http://sales-app-api.assistant'
        userInfo = {}
        url = SpecialURL + '/v1/auth/login'
        data = {"username":"13411111111","password":"111111",
                "grant_type":"password","client_id":"3000",
                "scope":"ALL:ALL",
                "client_secret":"app-passwd"}
        data = json.dumps(data)
        headers = {'content-type': 'application/json; charset=utf8'}
        response = requests.post(url, data, headers=headers)
        result = response.json()
        token_type = result['data']['token_type']
        access_token = result['data']['access_token']
        userInfo = {'token_type':token_type,'access_token':access_token}
        Authorization = token_type + access_token
        # print(WmApiTest.userInfo)
        # print(json.dumps(result[data,]))
        #WmApiTest.userInfo = {'token_type':,'access_token':}
        # print(result)
        return Authorization



    def testSpecial(self):
        '''特派员'''
        print('特派员', '\n')
        resultList = []
        titleList = []
        caseList = self.Ex.readExcel('ApiInfo.xlsx', 'Special')
        Authorization = self.tempLogin()
        # print(userInfo)
        # AuthorizationValues = userInfo['token_type'] + userInfo['access_token']
        Authorization = {'Authorization':Authorization}
        for caseDict in caseList:
            url = self.SpecialURL + caseDict['ApiLoad']
            titleList = list(caseDict)
            caseNum = caseDict['CaseNum']
            method = caseDict['Method']
            caseData = caseDict['CaseData']   # 这样获取的数据 是str 类型的

            if caseData != '':
                caseDataDict = eval(caseData)              # 使用eval 转换为dict 类型
            # 将dict类型转化为json类型
            data = json.dumps(caseDataDict)
            caseRun = caseDict['CaseRun']
            caseName = caseDict['CaseName']
            # 设置请求头
            headers = caseDict['Header']
            if headers !='':
                headers = eval(headers)
                headers = dict(headers,**Authorization)
            # print(userInfo)
            # print(headers)
            # 设置报告打印内容
            print('用例 ' + caseNum, end=': ')
            print(caseName)

            # print('搜索商品 : ' + caseDataDict['keyword'])
            if caseRun == 'Y':
                expectValue = eval(caseDict['ExpectValue'])
                if method == 'Post':
                    print('数据参数 : ' + data)
                    response = requests.post(url, data, headers=headers)
                    result = response.json()
                    # 设置断言
                    if result['code'] == expectValue['code'] and result['msg'] == expectValue['msg']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result,'\n')
                    print('执行结果',end=': ')
                    print(caseDict['CaseResult'], '\n')
                    print()
                    # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                    caseDict['ResultInfo'] = str(result)

                if method == 'Get':
                    response = requests.get(url, params=data, headers=headers)
                    result = response.json()
                    # 设置断言
                    if result['code'] == expectValue['code'] and result['hint'] == expectValue['hint']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result)
                    print('执行结果', end=': ')
                    print(caseDict['CaseResult'], '\n')
                    # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                    caseDict['ResultInfo'] = str(result)
            else:
                print('返回结果: 用例设置无需执行，故没有执行！', '\n')
            resultList.append(caseDict)
            # print(resultList)
        self.Ex.writeExcel('Special', titleList, resultList)

    # 购物车更新data
    def getCatData(self,data):
        # print(type(data))
        # print(data)
        dataDict = eval(data)
        # print(type(dataDict))
        dataDict['id'] = WmApiTest.cartId
        dataDict = json.dumps(dataDict)
        return dataDict
        # print(data['id'])

    # 删除购物车获取cartIdsList
    def getCartDataList(self, data):
        # print(type(data))
        # print(data)
        dataDict = eval(data)
        # print(type(dataDict))
        dataDict['idList'] = WmApiTest.cartIds
        dataDict = json.dumps(dataDict)
        return dataDict
        # print(data['id'])
    # 订单初始化cartIdsList
    def getCartList(self, data):
        # print(type(data))
        # print(data)
        dataDict = eval(data)
        # print(type(dataDict))
        dataDict['cartIds'] = WmApiTest.cartIds
        dataDict = json.dumps(dataDict)
        # print(dataDict)
        return dataDict
        # print(data['id'])

    # 获取orderList
    def getOrderList(self,data):

        dataDict = eval(data)
        # print(type(dataDict))
        dataDict['orderIds'] = WmApiTest.orderIds
        dataDict = json.dumps(dataDict)
        return dataDict

    def getOrderId(self,data):
        dataDict = eval(data)
        # print(type(dataDict))
        dataDict['orderId'] = WmApiTest.orderId
        dataDict = json.dumps(dataDict)
        # print(dataDict)
        return dataDict


    def testSpecialCart(self):
        '''购物车'''
        print('购物车', '\n')
        resultList = []
        titleList = []
        caseList = self.Ex.readExcel('ApiInfo.xlsx', 'SpecialCart')
        Authorization = self.tempLogin()
        # print(userInfo)
        # AuthorizationValues = userInfo['token_type'] + userInfo['access_token']
        Authorization = {'Authorization':Authorization}
        for caseDict in caseList:
            url = self.SpecialURL + caseDict['ApiLoad']
            titleList = list(caseDict)
            caseNum = caseDict['CaseNum']
            method = caseDict['Method']
            caseData = caseDict['CaseData']   # 这样获取的数据 是str 类型的
            if caseData != '':
                caseDataDict = eval(caseData)              # 使用eval 转换为dict 类型
            # 将dict类型转化为json类型
            data = json.dumps(caseDataDict)
            caseRun = caseDict['CaseRun']
            caseName = caseDict['CaseName']
            # 设置请求头
            headers = caseDict['Header']
            if headers !='':
                headers = eval(headers)
                headers = dict(headers,**Authorization)
            # print(userInfo)
            # print(headers)
            # 设置报告打印内容
            print('用例 ' + caseNum, end=': ')
            print(caseName)

            # print('搜索商品 : ' + caseDataDict['keyword'])
            if caseRun == 'Y':
                expectValue = eval(caseDict['ExpectValue'])
                if method == 'Post':
                    if caseName == '购物车-更新':
                        # 调用数据拼装函数
                        data = self.getCatData(data)

                    if caseName == '购物车--删除':
                        # 调用 数据 list拼装函数
                        data = self.getCartDataList(data)
                    print('数据参数 : ' + data)
                    response = requests.post(url, data, headers=headers)
                    result = response.json()
                    if caseName =='购物车--列表':
                        WmApiTest.cartId = result['data']['items'][0]['id']
                        # print(WmApiTest.cartId)
                        WmApiTest.cartIds = []
                        WmApiTest.cartIds.append(WmApiTest.cartId)
                        # print(WmApiTest.cartIds)
                        # print('返回购物车')
                    # 设置断言
                    if result['code'] == expectValue['code'] and result['msg'] == expectValue['msg']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result, '\n')
                    print('执行结果', end=': ')
                    print(caseDict['CaseResult'], '\n')
                    print()
                    # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                    caseDict['ResultInfo'] = str(result)

                if method == 'Get':
                    response = requests.get(url, params=data, headers=headers)
                    result = response.json()
                    # 设置断言
                    if result['code'] == expectValue['code'] and result['hint'] == expectValue['hint']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result)
                    print('执行结果', end=': ')
                    print(caseDict['CaseResult'], '\n')
                    # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                    caseDict['ResultInfo'] = str(result)
            else:
                print('返回结果: 用例设置无需执行，故没有执行！', '\n')
            resultList.append(caseDict)
            # print(resultList)
        self.Ex.writeExcel('SpecialCart', titleList, resultList)


    def testSpecialOrder(self):
        '''订单'''
        print('订单', '\n')
        resultList = []
        titleList = []
        caseList = self.Ex.readExcel('ApiInfo.xlsx', 'SpecialOrder')
        Authorization = self.tempLogin()
        # print(userInfo)
        # AuthorizationValues = userInfo['token_type'] + userInfo['access_token']
        Authorization = {'Authorization':Authorization}
        for caseDict in caseList:
            url = self.SpecialURL + caseDict['ApiLoad']
            titleList = list(caseDict)
            caseNum = caseDict['CaseNum']
            method = caseDict['Method']
            caseData = caseDict['CaseData']   # 这样获取的数据 是str 类型的
            if caseData != '':
                caseDataDict = eval(caseData)              # 使用eval 转换为dict 类型
            # 将dict类型转化为json类型
            data = json.dumps(caseDataDict)
            caseRun = caseDict['CaseRun']
            caseName = caseDict['CaseName']
            # 设置请求头
            headers = caseDict['Header']
            if headers !='':
                headers = eval(headers)
                headers = dict(headers,**Authorization)
            # print(userInfo)
            # print(headers)
            # 设置报告打印内容
            print('用例 ' + caseNum, end=': ')
            print(caseName)
            # print('数据参数 : ' + caseData)
            # print('搜索商品 : ' + caseDataDict['keyword'])
            if caseRun == 'Y':
                expectValue = eval(caseDict['ExpectValue'])
                if method == 'Post':
                    if caseName == '订单--初始化':
                        # 调用 数据 list拼装函数
                        data = self.getCartList(data)
                    if caseName == '订单--初始化结果' or caseName == '订单--提交' :
                        data = self.getOrderList(data)

                    if caseName == '订单--详情':
                        data = self.getOrderId(data)
                    print('数据参数 : ' + data)
                    response = requests.post(url, data, headers=headers)
                    result = response.json()
                    if caseName =='购物车--列表':
                        WmApiTest.cartId = result['data']['items'][0]['id']
                        # print(WmApiTest.cartId)
                        WmApiTest.cartIds = []
                        WmApiTest.cartIds.append(WmApiTest.cartId)
                        # print(WmApiTest.cartIds)
                        # print('返回购物车')

                    if caseName == '订单--初始化':
                        # print(result['data'])
                        WmApiTest.orderIds = result['data']
                        WmApiTest.orderId = result['data'][0]
                        # print(WmApiTest.orderId)
                    # 设置断言
                    if result['code'] == expectValue['code'] and result['msg'] == expectValue['msg']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result, '\n')
                    print('执行结果', end=': ')
                    print(caseDict['CaseResult'], '\n')
                    print()
                    # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                    caseDict['ResultInfo'] = str(result)

                if method == 'Get':
                    response = requests.get(url, params=data, headers=headers)
                    result = response.json()
                    # 设置断言
                    if result['code'] == expectValue['code'] and result['hint'] == expectValue['hint']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result)
                    print('执行结果', end=': ')
                    print(caseDict['CaseResult'], '\n')
                    # 这里要对结果进行一下处理，要不无法存入excel。转为Str类型。
                    caseDict['ResultInfo'] = str(result)
            else:
                print('返回结果: 用例设置无需执行，故没有执行！', '\n')
            resultList.append(caseDict)
            # print(resultList)
        self.Ex.writeExcel('SpecialOrder', titleList, resultList)







if __name__ == '__main__':
    unittest.main()
    # wmapiTest = WmApiTest()
    # wmapiTest.tempLogin()



