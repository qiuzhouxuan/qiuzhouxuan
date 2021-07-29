import json

import pytest
import requests


class TestFCArequest:
    # 获取token 鉴权
    token = ""

    # 执行测试用例顺序
    @pytest.mark.run(order=1)
    def test_get_token(self):
        url = "https://auth.stsdp.fcachinagsdp.com/cvp/oauth2/token/"
        payload = 'grant_type=client_credentials&scope=cvp.com%2Fscope%2Fadmin'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'authorization': 'Basic MTAwMDk6MmIwODBlMWQxZGQ2NDYxYTg3OTI1ZGZhNTczNjRjMTM='
        }
        response = requests.post(url, headers=headers, data=payload)
        print(response.json())
        TestFCArequest.token = response.json()["access_token"]

    # 获取UIN
    @pytest.mark.run(order=3)
    def test_get_uin(self):
        url = "https://mbproxy.stsdp.fcachinagsdp.com/iam-gateway/v2/iam_gateway/car_terminal/check_account_exist"
        payload = json.dumps({
            "phone": "15527114645"
        })
        headers = {
            'Authorization': 'Bearer ' + TestFCArequest.token,
            'Content-Type': 'application/json',
            'companyid': '2'
        }
        response = requests.post(url, headers=headers, data=payload)
        print(response.json())

    @pytest.mark.run(order=4)
    def test_01(self):
        pass

    @pytest.mark.run(order=6)
    def test_02(self):
        print("武汉测试学习")
        pass

    @pytest.mark.run(order=5)
    def test_03(self):
        pass

    @pytest.mark.run(order=2)
    def test_04(self):
        assert 11 == 12

    def test_get_vin(self):
        url = "https://cmm.stsdp.fcachinagsdp.com/v1.0/vehicles/REALJEEPTEST00001/factory"
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + TestFCArequest.token
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)

    def test_get_vin2(self):
        url = "https://cmm.stsdp.fcachinagsdp.com/v1.0/vehicles/REALJEEPTEST00001/factory"
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + TestFCArequest.token
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)


if __name__ == '__main__':
    # 详细信息，失败用例重跑次数,生成测试报告jtml文件
    #                          "--html=邱邱.html","--capture=sys"
    pytest.main(["-vs", "-rerun=2", "--html=邱邱1.html", "--capture=sys"])
