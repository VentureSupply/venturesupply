from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from bs4 import BeautifulSoup
import subprocess
import os
from .forms import NameForm

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return HttpResponseRedirect('#')
    else:
        form = NameForm()
    
    return render(request, 'search/search.html', {'form': form})

# Create your views here.
def search(request):
    #f = open("curl.txt", "r")
    #f = open(os.path.join(PROJECT_ROOT, 'curl.txt'))
    form = NameForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
    business_name =  name
    curl = "curl 'http://www.clerkrecordersearch.org/cgi-bin/FbnResult01.html/input' -H 'Host: www.clerkrecordersearch.org' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'DNT: 1' -H 'Referer: http://www.clerkrecordersearch.org/cgi-bin/FBNSearch.html/input' -H 'Cookie: Session=YXXXXXXXXXXXXYNNNNNN; DISPLAYWITHOUTCLICK=; PUBLICVIEWER=; PUBLICAPI=M; ScreenHeight=715; ScreenWidth=1366' -H 'Connection: keep-alive' --data 'Order=Y&Official=N&Birth=N&Marriage=N&Death=N&Session=YXXXXXXXXXXXXYNNNNNN&Maps=N&Fbn=N&SearchType=0021+&USERKEY=2015050700000000000005OFF&SearchDate=00000000&BusinessName="+business_name+"&BNAME=Search...&OwnerName=&F_Month=00&F_Day=00&F_Year=0000'"
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
            if b['name'] == business_name:
                if b['status'] == "ACTIVE":
                    return HttpResponse("Taken")

    return HttpResponse("Available")

        

    #return HttpResponse("<h1>a</h1>")
    return render_to_response('search/search.html', context_instance=RequestContext(request))
