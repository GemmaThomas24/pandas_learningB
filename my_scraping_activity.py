from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
# ----------------------------------------------
# ACTIVITY 2- DATA ACQUISITION
# ----------------------------------------------

with open('index.html','r') as file:
    html_text = file.read()
# the above has scraped my website and put the output in html_text variable

# print(dir(html_text))

souped_html = BeautifulSoup(html_text, "lxml")

# print(souped_html)
topics = souped_html.find_all("h3")

first_place = souped_html.find_all(class_="first")

second_place = souped_html.find_all(class_="second")

third_place = souped_html.find_all(class_="third")

topics_list = []
for topic in topics:
    print(topic.text.strip())
    topics_list.append(topic.text.strip())

firstplace_list = []
for first in first_place:
    print(first.text.strip())
    firstplace_list.append(first.text.strip())

secondplace_list = []
for second in second_place:
    print(second.text.strip())
    secondplace_list.append(second.text.strip())

thirdplace_list = []
for third in third_place:
    print(third.text.strip())
    thirdplace_list.append(third.text.strip())

df = pd.DataFrame({
    "Topic" : topics_list,
    "First Place" : firstplace_list,
    "Second Place" : secondplace_list,
    "Third Place" : thirdplace_list
})

print(df)

df.to_excel("output_myactivity.xlsx")