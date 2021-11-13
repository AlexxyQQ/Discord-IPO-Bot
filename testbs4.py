from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.sharesansar.com/category/ipo-fpo-news").text

soup = BeautifulSoup(html_text, "lxml")
Searchs = soup.find_all("div", class_="newslist")
for result in Searchs:
    t = result.find_all("div", class_="col-md-10 col-sm-10 col-xs-12")
    for a in t:
        Title = a.find("h4", class_="featured-news-title").text
        if "IPO Shares Listed" in Title:
            Date = result.find("span", class_="text-org").text
            print(Title)
            print(Date)
            print("\n")
