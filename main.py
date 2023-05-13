import requests
from bs4 import BeautifulSoup


search = input().replace(" ", "+")
url = f"https://store.steampowered.com/search/?term= {search}"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
games = soup.find_all("div", class_="responsive_search_name_combined")

for game in games:
    title = game.find("span", class_="title").text.strip()
    price = game.find("div", class_="search_price").text.strip()
    index = price.find(".")
    discount = game.find("div", class_="search_discount").text.strip()

    if discount != '':
        print(f"Название:  {title} \n Цена без скидки: {price[:index]} \n"
        f"Скидка: {discount} \n Цена со скидкой: {price[index+1:]} \n")

    #class ="col search_price  responsive_secondrow"