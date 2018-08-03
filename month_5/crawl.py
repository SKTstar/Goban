import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

url = "http:bj.58.com/pinpaigqongyu/pn/{page}/?minprince=2000_400"

page = 0

csv_file = open("rent.csv", "w")
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    if page > 50:
        break
    print("fetch: ", url.format(page=page))
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.txt, "lxml")
    house_list = html.select(".list>li")

    for house in house_list:
        house_title =house.select("h2")[0].string
        house_url = urljoin(url, house.select("a")[0]["href"])
        house_info_list = house_title.split()

        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select(".money")[0].select("b")[0].string.encode("utf8")
        csv_writer.writerow([house_title, house_location, house_money, house_url])
csv_file.close()