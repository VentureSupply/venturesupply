from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from bs4 import BeautifulSoup
import subprocess
import os

# Create your views here.
def search(request):
    #f = open("curl.txt", "r")
    #f = open(os.path.join(PROJECT_ROOT, 'curl.txt'))
    curl = "curl 'http://www.clerkrecordersearch.org/cgi-bin/FbnResult01.html/input' -H 'Host: www.clerkrecordersearch.org' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'DNT: 1' -H 'Referer: http://www.clerkrecordersearch.org/cgi-bin/FBNSearch.html/input' -H 'Cookie: Session=YXXXXXXXXXXXXYNNNNNN; DISPLAYWITHOUTCLICK=; PUBLICVIEWER=; PUBLICAPI=M; ScreenHeight=715; ScreenWidth=1366' -H 'Connection: keep-alive' --data 'Order=Y&Official=N&Birth=N&Marriage=N&Death=N&Session=YXXXXXXXXXXXXYNNNNNN&Maps=N&Fbn=N&SearchType=0021+&USERKEY=2015050700000000000005OFF&SearchDate=00000000&BusinessName=GOOGLE&BNAME=Search...&OwnerName=&F_Month=00&F_Day=00&F_Year=0000'"
    #curl = f.read()
    shell_output = subprocess.check_output(curl, shell=True)
    soup = BeautifulSoup(shell_output)
    table = soup.find_all('table')
    trs = table[2].findAll("tr")[4:]
    business_list = []
    business_data = {}
    for tr in trs:
        tds = tr.find_all('td')
        name = str.strip(tds[0].text)
        status = str.strip(tds[3].text)
        business_data = {
            'name': name,
            'status': status,
        }
        business_list.append(business_data)
        for b in business_list:
            return HttpResponse("<h1>%s</h1>" % b)
            print(b)

    #return HttpResponse("<h1>a</h1>")
