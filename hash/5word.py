from msilib.schema import Environment
from bs4 import BeautifulSoup
import requests


text_file = open("test.txt", "a")

url2 = f"https://wordfind.com/length/2-letter-words/" # formartierter string
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.content, "html.parser")
# print(soup)

div2 = soup2.find("div", attrs={"class": "lBlock"})
rows2 = div2.find_all("a")

def get_2_word():
    
    count = 0
    for i in rows2:
        word = i.text.split()
        string = str(word)
        text_file.write(string)
        text_file.write("\n")
        string2 = string[:3].upper() + string[3:]
        text_file.write(string2)
        text_file.write("\n")
        count += 1
        # print(word)
        # print(count)
        
get_2_word()

url3 = f"https://wordfind.com/length/3-letter-words/" # formartierter string
page3 = requests.get(url3)
soup3 = BeautifulSoup(page3.content, "html.parser")
# print(soup)

div3 = soup3.find("div", attrs={"class": "lBlock"})
rows3 = div3.find_all("a")

def get_3_word():
    
    count = 0
    for i in rows3:
        word = i.text.split()
        string = str(word)
        text_file.write(string)
        text_file.write("\n")
        string2 = string[:3].upper() + string[3:]
        text_file.write(string2)
        text_file.write("\n")
        count += 1
        # print(word)
        # print(count)
        
get_3_word()

url4 = f"https://wordfind.com/length/4-letter-words/" # formartierter string
page4 = requests.get(url4)
soup4 = BeautifulSoup(page4.content, "html.parser")
# print(soup)

div4 = soup4.find("div", attrs={"class": "lBlock"})
rows4 = div4.find_all("a")

def get_4_word():
    
    count = 0
    for i in rows4:
        word = i.text.split()
        string = str(word)
        text_file.write(string)
        text_file.write("\n")
        string2 = string[:3].upper() + string[3:]
        text_file.write(string2)
        text_file.write("\n")
        count += 1
        # print(word)
        # print(count)
        
get_4_word()

url5 = f"https://wordfind.com/length/5-letter-words/" # formartierter string
page5 = requests.get(url5)
soup5 = BeautifulSoup(page5.content, "html.parser")
# print(soup)

div5 = soup5.find("div", attrs={"class": "lBlock"})
rows5 = div5.find_all("a")

def get_5_word():
    
    count = 0
    for i in rows5:
        word = i.text.split()
        string = str(word)
        text_file.write(string)
        text_file.write("\n")
        string2 = string[:3].upper() + string[3:]
        text_file.write(string2)
        text_file.write("\n")
        count += 1
        # print(word)
        # print(count)
        
get_5_word()


