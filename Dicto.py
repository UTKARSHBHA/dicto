import json
from difflib import get_close_matches
data = json.load(open("data.json"))

word = input("Enter a word: ")

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(word , data.keys())[0] } if yes, press 'Y' if no press 'N': ")
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        else :
            return "Sorry, please retry!"
    else:
        return "Sorry! word not found"
output = translate(word)

if type(output) == str:
    print(output)
elif type(output) == list:
    for u in output:
        print(u)



