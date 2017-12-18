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
            if caseDict['CaseData'] != '':
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
            print(headers)
            # 设置报告打印内容
            print('用例 ' + caseNum, end=': ')
            print(caseName)
            print('数据参数 : ' + caseData)
            # print('搜索商品 : ' + caseDataDict['keyword'])
            if caseRun == 'Y':
                expectValue = eval(caseDict['ExpectValue'])
                if method == 'Post':
                    response = requests.post(url, data, headers=headers)
                    result = response.json()
                    # 设置断言
                    if result['code'] == expectValue['code'] and result['msg'] == expectValue['msg']:
                        caseDict['CaseResult'] = 'Pass'
                    else:
                        caseDict['CaseResult'] = 'Fail'
                    print('返回结果', end=': ')
                    print(result)
                    print('执行结果',end=': ')
                    print(caseDict['CaseResult'], '\n')
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


if __name__ == '__main__':
    unittest.main()
    # wmapiTest = WmApiTest()
    # wmapiTest.tempLogin()



