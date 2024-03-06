from re import findall, sub
from requests import get
from bs4 import BeautifulSoup
from .utils.scraper_helpers import remove_html
from .utils.scraper_db_helpers import conn, create_table, insert_cards
from ..models import ChaseCard

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


def get_chase_cards():
    cards_to_insert = []

    for card in card_data:
        new_card_object = ChaseCard()

        card_id = "{card_id}".format(card_id=card["card_id"])
        name = "{name}".format(name=card["name"])

        new_card_object.card_id = card_id
        new_card_object.name = name

        rewards = soup.find_all("script", attrs={"id": card_id})

        for reward in rewards:
            strings = findall(r'<p>.+?</p>', reward.string)

            for num, string in enumerate(strings, start=1):
                sup_tag_regex = r'<su[^>].+?</sup>'
                sup_tags = findall(sup_tag_regex, string)

                if sup_tags:
                    result = sub(sup_tag_regex, "", string, 0)
                    s = remove_html(result)
                else:
                    s = remove_html(string)

                field_name = "reward_{num}".format(num=num)
                setattr(new_card_object, field_name, s)

        card_tuple = tuple(new_card_object)
        cards_to_insert.append(card_tuple)

    create_table()

    insert_cards(cards_to_insert)
    conn.close()
