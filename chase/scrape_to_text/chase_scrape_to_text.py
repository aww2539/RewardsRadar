from re import findall, sub
from ..utils import card_data, soup, remove_html

def scrape_chase_cards_to_text():
    for card in card_data:
        with open('chase/scrape_to_text/chase_rewards.txt', 'a') as f:
            f.write("{name}".format(name = card["name"]))
            f.write("\n")

            rewards = soup.find_all("script", attrs={"id": "{id}".format(id = card["id"])})

            for reward in rewards:
                strings = findall(r'<p>.+?</p>', reward.string)

                for string in strings:
                    sup_tag_regex = r'<su[^>].+?</sup>'
                    sup_tags = findall(sup_tag_regex, string)

                    if sup_tags:
                        result = sub(sup_tag_regex, "", string, 0)
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