import io
import re
import requests
from PyPDF2 import PdfReader

unlimited_url = "https://www.chase.com/freedomunlimited/rewardsagreement"
flex_url = "https://www.chase.com/freedomflex/rewardsagreement"
rise_url = "https://www.chase.com/freedomrise/rewardsagreement"
sapphire_url = "https://www.chase.com/sapphire/rewardsagreement"
reserve_url = "https://www.chase.com/reserve/rewardsagreement"

credit_cards = [unlimited_url, flex_url, rise_url, sapphire_url, reserve_url]

for card_num, card in enumerate(credit_cards, start=1):
    print("Start card #{card_num} load".format(card_num = card_num))
    with open('rewards_list.txt', 'a') as f:
        f.write("Card #{card_num}".format(card_num = card_num))
        f.write("\n")
    f.close()
    page = requests.get(card)
    file = io.BytesIO(page.content)
    reader = PdfReader(file)


    # extracting text from page
    text = reader.pages[1].extract_text()
    # trim unneeded text around awards section
    trim_to_rewards_section = text[text.find('You’ll earn:'):].split('• Rewards Categories')[0]

    # make bullet points uniform
    small_bullet_regex = r"·(?=)"
    small_bullet_sub = "•"
    formatted_rewards = re.sub(small_bullet_regex, small_bullet_sub, trim_to_rewards_section, 0, re.MULTILINE)
    
    # replace line breaks 
    line_break_regex = r"\n(?=)"
    line_break_sub = ""
    rewards_without_line_breaks = re.sub(line_break_regex, line_break_sub, formatted_rewards, 0, re.MULTILINE)



    extract_rewards_regex = r"(?<=› )[^›•]+(?=•)"
    matches = re.finditer(extract_rewards_regex, rewards_without_line_breaks)

    for match_num, match in enumerate(matches, start=1):
        print("{match}".format(match = match.group()))

        with open('rewards_list.txt', 'a') as f:
            f.write("{match}".format(match_num = match_num, match = match.group()))
            f.write("\n")
        f.close()
    
    with open('rewards_list.txt', 'a') as f:
        f.write("\n")
    f.close()
 
# regex playground link: https://regex101.com/r/fLHT9f/56
# regex playground link: https://regex101.com/r/fLHT9f/59
# regex playground link: https://regex101.com/r/fLHT9f/56
# regex playground link: https://regex101.com/r/fLHT9f/56
