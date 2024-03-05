from re import findall, sub
from .utils import card_data, soup, remove_html
from .db_helpers import conn, create_table, insert_cards
from models.chase_card import ChaseCard

def get_chase_cards():
        cards_to_insert = []

        for card in card_data:
            card_object = ChaseCard()

            card_id = "{card_id}".format(card_id = card["card_id"])
            name = "{name}".format(name = card["name"])

            card_object.card_id = card_id
            card_object.name = name

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
                    setattr(card_object, field_name, s)

            card_tuple = tuple(card_object)
            cards_to_insert.append(card_tuple)

        create_table()

        insert_cards(cards_to_insert)
        conn.close()            
