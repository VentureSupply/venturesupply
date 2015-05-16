from bs4 import BeautifulSoup
import subprocess


def curl():
    f = open("curl.txt", "r")
    curl = f.read()
    shell_output = subprocess.check_output(curl, shell=True)
    soup = BeautifulSoup(shell_output)
    scrape(soup)

def scrape(soup):
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
            print(b)

curl()
