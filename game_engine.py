import requests
import random
import os


BLOGS_API = os.environ["BLOG_ENDPOINT"]

response = requests.get(BLOGS_API)
texts = response.json()

class GameEngine():
    """Generates random text and calculates the final score"""
    def __init__(self):
        self.texts = texts
        self.rdm_text = ""


    def get_text(self):
        """Returns a random text from a list"""
        rand_int = random.randint(0, len(texts) - 1)
        random_text = self.texts[f'{rand_int}']
        self.rdm_text = random_text
        return random_text

    def calculate_score(self, typed_text):
        """Takes the typed test as an input and calculates users words per minute, error count
        returns final score"""
        rdm_text_list = self.rdm_text.split(" ")
        typed_text_list = typed_text.split(" ")
        typed_text_list_clean = typed_text_list[0:len(typed_text_list) - 1]
        comparison_list = rdm_text_list[0:len(typed_text_list_clean)]
        matches = set(typed_text_list_clean) & set(comparison_list)
        error_count = len(comparison_list) - len(matches)
        wpm = (len(typed_text_list))
        score = (wpm * 5) - (error_count * 10)
        print(f"this is the score: {score}")
        return score





