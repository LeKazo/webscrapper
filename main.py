
import requests
from bs4 import BeautifulSoup

city = input("Enter a name of a City: ")


url = "https://www.google.com/search?q="+"weather"+city

html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

temp = soup.find_all('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
# todays_temp = temp[0].text

for x in temp:
    print(temp)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(temp[1].text)
time_skyDescription = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})
for y in time_skyDescription:
    print(time_skyDescription.text)
print("####################################################################################")

time_skyDescription2 = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})
for y in enumerate(time_skyDescription2):
    print(y.text)
    print("next")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# data = time_skyDescription.split('\n')
# data = time_skyDescription
time = time_skyDescription.text
# sky = data[1]
print(time_skyDescription)

listdiv = soup.find_all('div', attrs={'class': 'BNeawe s3v8rd AP7Wnd'})

# strd = listdiv[0].text

# print(listdiv)

# pos = strd.find('Wind')
# otherData = strd[pos:]

# print("Temperature is", temp)
# print("time: ", time)
# print("Sky Description")
# print(otherData)
