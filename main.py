from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


html_text = requests.get("https://www.scrapethissite.com/pages/simple/").text
# requesting browser to get you the info from web page. Finds/checks with google you're allowesd to make a connection- here is the page
# then save the results of the request html_text

# print(dir(html_text)
# terminal code 200 = yes I was able to get that
# html_text holding the whole object
# objects have prop and methods - we don;t know what properties it has
# find out by using function called dir(). Make a directry of the properties of html_text

# print(html_text)
# output is the html content of the page- e.g what we did in index.html

souped_html = BeautifulSoup(html_text, "lxml")

countries = souped_html.find_all("h3")

country_capital = souped_html.find_all("span", class_="country-capital")

population = souped_html.find_all("span", class_="country-population")

country_area = souped_html.find_all("span", class_="country-area")


population_list = []
for population in population:
    print(population.text.strip())
    population_list.append(population.text.strip())

countries_list = []
for country in countries:
    print(country.text.strip())
    countries_list.append(country.text.strip())

capitals_list = []
for capital in country_capital:
    print(capital.text.strip())
    capitals_list.append(capital.text.strip())

areas_list =[]
for area in country_area:
    print(area.text.strip())
    areas_list.append(area.text.strip())


df = pd.DataFrame({
    "Countries" : countries_list,
    "Capital City" : capitals_list,
    "Population" : population_list,
    "Area(Km2)" : areas_list
})

print(df)

df.to_excel("output.xlsx")
# df = pd.DataFrame([country.text.strip() for country in countries])

# print(df)