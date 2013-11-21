#!/bin/bash
curl -c /tmp/wlt "http://wlt.ustc.edu.cn/cgi-bin/ip?cmd=login&name=orcking&password=87291682" > /dev/null 
curl -b /tmp/wlt "http://wlt.ustc.edu.cn/cgi-bin/ip?cmd=set&type=6&exp=0" > /dev/null 
rm /tmp/wlt 
