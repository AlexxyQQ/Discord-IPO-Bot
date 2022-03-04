from bs4 import BeautifulSoup
import requests

symbol = "mlbs"


def a():
    html_text = requests.get(
        f"https://merolagani.com/CompanyDetail.aspx?symbol={symbol}"
    ).text

    soup = BeautifulSoup(html_text, "lxml")
    Searchs = soup.find_all("div", class_="container")
    for result in Searchs:
        Title_find = result.find_all("h4", class_="page-header")

        for finds in Title_find:
            Title = finds.find("span").text

        Body_find = result.find_all("div", class_="panel-body")

        for find2 in Body_find:
            list_found = find2.find_all("tbody", class_="panel panel-default")

            for Strong in list_found:
                LTP_find = Strong.find_all("strong")

                for print_LTP in LTP_find:
                    LTP = print_LTP.find("span", class_="text-increase").text
                    return f"{Title} \n LTP: {LTP}"
