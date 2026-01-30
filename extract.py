import requests
from bs4 import BeautifulSoup

def extract_flipkart_data():
    product_name = []
    product_price = []
    product_review = []

    for i in range(2, 10):
        url = "https://www.flipkart.com/search?q=mobile+under+50000&page=" + str(i)
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        
        box = soup.find("div", class_="QSCKDh dLgFEE")
        if box is None:
            continue  
        
        names = box.find_all("div", class_="RG5Slk")
        prices = box.find_all("div", class_="hZ3P6w DeU9vF")
        reviews = box.find_all("div", class_="MKiFS6")

      
        max_len = max(len(names), len(prices), len(reviews))
        names += [None]*(max_len - len(names))
        prices += [None]*(max_len - len(prices))
        reviews += [None]*(max_len - len(reviews))

        for n, p, r in zip(names, prices, reviews):
            product_name.append(n.text if n else None)
            product_price.append(p.text if p else None)
            product_review.append(r.text if r else None)

    return {
        "Product Name": product_name,
        "Prices": product_price,
        "Reviews": product_review
    }

