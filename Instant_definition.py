import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def user_input(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if not. " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Sorry we weren't able to predict your word!"
        else:
            return "We didn't understand your entry."
    else:
        return "That word doesn't exist, please check your input and try again."

word = input("please enter word here: ")


output = user_input(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
