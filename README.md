# UCAS-WIFI
命令行登录UCAS wifi

[![PyPI version](https://img.shields.io/pypi/v/ucas-wifi.svg)](https://github.com/IanSmith123/ucass-wifi) [![GitHub stars](https://img.shields.io/github/stars/IanSmith123/ucas-wifi.svg)](https://github.com/IanSmith123/ucas-wifi/stargazers) [![GitHub license](https://img.shields.io/github/license/IanSmith123/ucas-wifi.svg)](https://github.com/IanSmith123/ucas-wifi/blob/master/License)

# How to use

## 安装
本程序依赖于python，且只在python3 on win10 测试通过，未测试其他环境。
```bash
$ pip3 install ucas-wifi
```

## 打开终端
请确保已经正确连接寝室的网线或者`UCAS`WiFi之后再使用本程序。

- 登入

```bash
$ ucas-wifi
```

- 注销

```bash
$ ucas-wifi logout
```
- 重置账户密码

```bash
$ ucas-wifi reset
```

- 查看帮助信息

```bash
$ ucas-wifi help
```

- 升级本脚本
```
$ pip3 install -U ucas-wifi -i https://pypi.org/simple
```

# Hint
- 账户信息保存在`~/.ucas-wifi.json`
- win10将会使用toast提示命令执行情况，如果不需要该提示框, 重设用户信息的时候选择`n`即可

# Todo
- [ ] 使用bash/ash完成认证过程，适配openwrt

# Changelog
- 2019-9-9 13:34:00 适配UCAS无线网络完成，可以正常登陆和登出，支持显示剩余流量


# Refer

- https://github.com/IanSmith123/SCUNET



# More

不接受任何形式的提需求，只接受PR :)

Les1ie

2019-9-9 13:35:15

