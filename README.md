# UCAS-WIFI
命令行登录UCAS wifi 。

[![PyPI version](https://img.shields.io/pypi/v/ucas-wifi.svg)](https://github.com/IanSmith123/ucas-wifi) [![GitHub stars](https://img.shields.io/github/stars/IanSmith123/ucas-wifi.svg)](https://github.com/IanSmith123/ucas-wifi/stargazers) [![GitHub license](https://img.shields.io/github/license/IanSmith123/ucas-wifi)](https://github.com/IanSmith123/ucas-wifi/blob/master/License)

# How to use

## 安装
本程序依赖于python，且只在python3 on win10和python3 on debian 9 测试通过，未测试其他环境。
```bash
$ pip3 install ucas-wifi
```

## 打开终端
请确保已经正确连接寝室的网线或者`UCAS`WiFi之后再使用本程序。

- 检查是否已经可以正常访问互联网，无法访问则登入
```bash
$ ucas-wifi
```

- 跳过检查是否正常联网的检查，直接登录
```bash 
$ ucas-wifi direct
```

- 注销
```bash
$ ucas-wifi logout
```

- 查看剩余流量
```bash
$ ucas-wifi info
```

- 重置保存的账户密码

```bash
$ ucas-wifi reset
```

- 查看帮助信息

```bash
$ ucas-wifi help
```

- 升级本脚本
```bash
$ pip3 install -U ucas-wifi -i https://pypi.org/simple
```

# Hint
- 账户信息保存在`~/.ucas-wifi.json`
- 程序检查联网是通过访问  `http://detectportal.firefox.com/success.txt` 获取返回网页内容来判断是否可以联网的，这个网址可以使用IPV6访问，因此如果获取到了IPV6地址即可认为已经可以联网了，如果仍旧想要登录账号，请使用 `ucas-wifi direct `命令

# Todo
- [ ] 使用bash/ash完成认证过程，适配openwrt （代码早就写完了只是懒得更新 :)

# Changelog
- 2019-9-9 13:34:00 适配UCAS无线网络完成，可以正常登陆和登出，支持显示剩余流量
- 2019-9-9 20:25:56 使用`console_scripts`打包入口
- 2019-9-10 08:41:58 增加跳过检查联网步骤直接登录选项
- 2019-9-10 08:42:21 增加`ucas-wifi info`选项，支持获取当前账户信息
- 2019-9-13 01:13:54  README中添加bug说明， info获取的流量可能不实时
- 2019-11-11 20:02:51 README中添加 `ucas-wifi direct`和`ucas-wifi info`命令的说明

# Bug

- `ucas-wifi info`使用的API可能存在一定的延迟，流量信息可能不准确 （暂不打算修复）


# Refer

- https://github.com/IanSmith123/SCUNET


# More

不接受任何形式的提需求，只接受PR :)

Les1ie

2019-9-9 13:35:15

