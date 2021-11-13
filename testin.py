import discord

from bs4 import BeautifulSoup
import requests

A = ""
B = ""
html_text = requests.get("https://www.sharesansar.com/category/ipo-fpo-news").text

soup = BeautifulSoup(html_text, "lxml")
Searchs = soup.find_all("div", class_="newslist")
for result in Searchs:
    t = result.find_all("div", class_="col-md-10 col-sm-10 col-xs-12")
    for a in t:
        Title = a.find("h4", class_="featured-news-title").text
        if "IPO Shares Listed" in Title:
            Date = result.find("span", class_="text-org").text
            A = Title
            B = Date


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        word_list = ["!IPO"]

        # don't respond to ourselves
        if message.author == self.user:
            return

        messageContent = message.content
        if len(messageContent) > 0:
            for word in word_list:
                if word in messageContent:
                    await message.delete()
                    await message.channel.send(f"{A}\n{B}")


client = MyClient()
client.run("BOT Token")
