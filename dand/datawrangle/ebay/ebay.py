import requests
import pprint
from bs4 import BeautifulSoup

# Extract items from page
def get_items(page):
    item_list = []
    # Find class where items are located
    items = page.select(".dne-itemtile-detail")
    for item in items:
        # Select h3 tag
        h3_tag = item.h3
        # Get product name
        item_name = h3_tag['title'].encode('utf-8')
        # Get link to product
        item_link = h3_tag.a
        # Get price
        price = item.select(".dne-itemtile-price")

        if price:
            span = price[0].span
            item_price = span.text.encode('utf-8')

            item_info = {"item_name": item_name,
                         "item_link": item_link,
                         "item_price": item_price,
                         }
            item_list.append(item_info)

        item_info = {"item_name": item_name,
                     "item_link": item_link,
                     }

        item_list.append(item_info)
    return item_list

# Request page and parse it with Beautiful Soup
def load_page(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def main():
    link = "https://www.ebay.com/globaldeals/tecnologia"
    page = load_page(link)
    item_list = get_items(page)

    pprint.pprint(item_list)


if __name__ == '__main__':
    main()
