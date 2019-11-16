#!/bin/bash
# https://github.com/IanSmith123/ucas-wifi

userid=yourstudentid
password=yourpassword

login() {
	result=$(curl 'http://210.77.16.21/eportal/InterFace.do?method=login'  --data "userId=$userid" -d "password=$password" -d "queryString=wow" -s ) 
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
