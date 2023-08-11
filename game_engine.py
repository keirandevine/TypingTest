import requests
import random


response = requests.get("https://api.npoint.io/fcc0380fe644901de912")
texts = response.json()

class GameEngine():
    def __init__(self):
        self.texts = texts
        self.rdm_text = ""


    def get_text(self):
        rand_int = random.randint(0, len(texts) - 1)
        random_text = texts[f'{rand_int}']
        self.rdm_text = random_text
        return random_text

    def calculate_score(self, typed_text):
        rdm_text_list = self.rdm_text.split(" ")
        typed_text_list = typed_text.split(" ")
        error_count = 0
        print(typed_text_list)
        for i in range(0, len(rdm_text_list)):
            if rdm_text_list[i] != typed_text_list:
                error_count += 1
        wpm = int(len(typed_text_list))
        wpm_score = wpm * 5
        score = wpm_score
        print(f"this is the score: {score}")
        return score





