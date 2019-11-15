#!/bin/bash
# https://github.com/IanSmith123/ucas-wifi

userid=yourstudentid
password=yourpassword

login() {
	url=$(curl -Ls -o /dev/nulll -w %{url_effective}  210.77.16.21 )
	queryString=${url:38}

	result=$(curl 'http://210.77.16.21/eportal/InterFace.do?method=login'  --data "userId=$userid" -d "password=$password" -d "service=" -d "queryString=$queryString" -d "operatorPwd=&operatorUserId=&validcode="  -s)

	echo $result
}

out() {

	curl "http://210.77.16.21/eportal/InterFace.do?method=logout" -s >/dev/null
	echo "log out success"
}

if [ "$1" == "logout" ]; then
	out
else
	login
fi
