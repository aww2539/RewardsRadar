from re import sub
from requests import get
from bs4 import BeautifulSoup

card_data = [
        {"name": "Chase Sapphire Preferred", "card_id": "t-r6-4"},
        {"name": "Chase Sapphire Reserve", "card_id": "t-r6-37"},
        {"name": "Chase Freedom Unlimited", "card_id": "t-r6-36"},
        {"name": "Chase Freedom Flex", "card_id": "t-r6-56"},
        {"name": "Chase Freedom Rise", "card_id": "t-r6-71"}
    ]

chase_url = "https://creditcards.chase.com/compare-credit-cards"
chase_page = get(chase_url)
soup = BeautifulSoup(chase_page.content, "html5lib")

def remove_html(string):
    return sub(r'<[^>]*>', "", string, 0).strip()