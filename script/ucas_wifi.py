#!/usr/bin/env python3
import re
import os
import sys
import json
import getpass
from urllib.parse import urlparse

import requests

config_path = os.path.join(os.path.expanduser('~'), '.ucas_wifi.json')


def login_ucas(stuid, password):
    url = "http://210.77.16.21"
    r = requests.get(url)
    payload = {
        "userId": stuid,
        "password": password,
        "service": "",
        "queryString": urlparse(r.url).query,
        "operatorPwd": '',
        "operatorUserId": '',
        "validcode": '',
    }
    r = requests.post("http://210.77.16.21/eportal/InterFace.do?method=login", data=payload)
    r.encoding = 'u8'

    # print(r.json())
    if r.json().get("result") == "success":
        print("登录成功")
    else:
        print("登录失败")
        print(r.json().get('message'))


def get_traffic():
    url = "http://210.77.16.21/eportal/InterFace.do?method=getOnlineUserInfo"

    r = requests.get(url)
    r.encoding = 'u8'

    try:
        max_flow = r.json().get('maxFlow')
        user_name = r.json().get("userName")
        user_id = r.json().get("userId")
        user_ip = r.json().get("userIp")
        # user_mac = r.json().get('userMac')

        print("用户名: {}".format(user_name))
        print("登录账号: {}".format(user_id))
        print("IP: {}".format(user_ip))
        print("剩余流量: {}".format(max_flow))

    except:
        print("获取用户信息失败，请稍后重试 :(")
        pass


def logout():
    url = "http://210.77.16.21/eportal/InterFace.do?method=logout"
    requests.get(url)


def get_user_info():
    if not os.path.isfile(config_path):
        print("未检测到账户信息，请输入账户信息")
        with open(config_path, 'w', encoding='utf8') as f:
            _stuid = input("请输入用户名: ")
            _password = getpass.getpass("输入密码，输入时密码不可见: ")
            dic = {
                "stuid": _stuid,
                "password": _password,
            }
            f.write(json.dumps(dic, indent=2))
        print("已经保存账户信息，路径为{}".format(config_path))

    if os.path.getsize(config_path):
        j = json.load(open(config_path))
    else:
        print("请重置登录信息再继续操作")
        exit(1)

    _stuid = j['stuid']
    _password = j['password']

    return _stuid, _password


def detectportal():
    url = "http://detectportal.firefox.com/success.txt"
    try:
        if requests.get(url, timeout=2).text.strip() == 'success':
            return True
        else:
            return False
    except:
        return True


def main():
    """
    判断将要执行的操作
    :return:
    """
    if len(sys.argv) == 1:
        stuid, password = get_user_info()
        # 检测联网状况，判定是否需要登录
        if detectportal():
            print("正常联网，无需登录")
            get_traffic()
            exit(0)

        # 避免检测超时导致的误判
        logout()
        login_ucas(stuid, password)

    else:
        args = sys.argv[1]
        if args == "logout":
            logout()
            print("已注销")

        elif args == 'reset':
            # config_path = os.path.join(os.path.expanduser('~'), '.scunet.json')
            if os.path.isfile(config_path):
                os.remove(config_path)
                print("账户信息已清除")
            else:
                print("未检测到账户信息")

        elif args == 'info':
            get_traffic()

        elif args == "direct":
            stuid, password = get_user_info()
            # 跳过检测步骤 直接登录
            # 避免检测超时导致的误判
            logout()
            login_ucas(stuid, password)

        elif args == 'help':
            output = """
            {}
            
            ucas-wifi          : login
            ucas-wifi logout   : log out
            ucas-wifi reset    : clear user info
            ucas-wifi info     : get traffic info
            ucas-wifi direct    : direct login and skip detect portal
            ucas-wifi help     : print this message
            
            
            
            Bug report URL: https://github.com/iansmith123/ucas-wifi
            
            powered by Les1ie.
            
            {}
            """.format('*' * 52, '*' * 52)
            print(output)
        else:
            print("无法识别的指令 {}, 请运行 ucas-wifi help 查看帮助".format(args))


if __name__ == '__main__':
    main()
