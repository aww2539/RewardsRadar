import re
import requests
from bs4 import BeautifulSoup

card_data = [
        {"name": "Chase Sapphire Preferred", "id": "t-r6-4"},
        {"name": "Chase Sapphire Reserve", "id": "t-r6-37"},
        {"name": "Chase Freedom Unlimited", "id": "t-r6-36"},
        {"name": "Chase Freedom Flex", "id": "t-r6-56"},
        {"name": "Chase Freedom Rise", "id": "t-r6-71"}
    ]

chase_url = "https://creditcards.chase.com/compare-credit-cards"
chase_page = requests.get(chase_url)
soup = BeautifulSoup(chase_page.content, "html5lib")


def remove_html(string):
    return re.sub(r'<[^>]*>', "", string, 0).strip()

def scrape_chase_cards():
    for card in card_data:
        with open('chase/output/chase_rewards.txt', 'a') as f:
            f.write("{name}".format(name = card["name"]))
            f.write("\n")

            rewards = soup.find_all("script", attrs={"id": "{id}".format(id = card["id"])})

            for reward in rewards:
                strings = re.findall(r'<p>.+?</p>', reward.string)

                for string in strings:
                    sup_tag_regex = r'<su[^>].+?</sup>'
                    sup_tags = re.findall(sup_tag_regex, string)

                    if sup_tags:
                        result = re.sub(sup_tag_regex, "", string, 0)
                        s = remove_html(result)
                    else:
                        s = remove_html(string)

                    f.write("{s}".format(s=s))
                    f.write("\n")
            f.write("\n")
    f.close()


# Specific compare URLs if needed for later use
# freedom_cards_url = "https://creditcards.chase.com/compare-credit-cards/?iCELL=61FZ&list=36%2C56%2C71"
# sapphire_cards_url = "https://creditcards.chase.com/compare-credit-cards/?iCELL=61FZ&list=36%2C56%2C71"
# amazon_cards_url = "https://creditcards.chase.com/compare-credit-cards?list=22%2C66&iCELL=6C1Y"