from bs4 import BeautifulSoup
import subprocess

f = open("curl.txt", "r")
curl = f.read()
shell_output = subprocess.check_output(curl, shell=True)
soup = BeautifulSoup(shell_output)
for td in soup.find_all('td'):
    print(td.text)
