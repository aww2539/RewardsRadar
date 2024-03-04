import re
import requests
from bs4 import BeautifulSoup
from chase_cards import card_rewards_html_ids
def remove_html(string):
    return re.sub(r'<[^>]*>', "", string, 0).strip()

chase_url = "https://creditcards.chase.com/compare-credit-cards"
chase_page = requests.get(chase_url)
soup = BeautifulSoup(chase_page.content, "html5lib")

def scrape_chase_cards():
    for card in card_rewards_html_ids:
        with open('chase_rewards.txt', 'a') as f:
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

scrape_chase_cards()