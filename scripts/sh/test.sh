#!/bin/bash
DOMAIN=$(echo "$1" | sed -e "s%http://%%g")
TYPE=$2

if [ -z ${TYPE} ];then
	TYPE="A"
fi

dig ${DOMAIN} ${TYPE} 
