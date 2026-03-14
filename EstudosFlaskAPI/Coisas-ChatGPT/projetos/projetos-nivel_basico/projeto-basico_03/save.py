# Text Analyzer API

from flask import Flask, request
import unicodedata

app = Flask(__name__)

@app.route("/analyse", methods=["POST"])
def analyse():
    data = request.json
    text = data["text"]

    words = count_words(text)
    characters = 0
    phrases = 0
    vowels = 0
    longest_word = ""
    frequency = {}


    # characters
    for word in text.strip().split():
        characters += len(word)

    # phrases
    phrases = len(text.strip()[:-1].split("."))

    # vowels
    for i in range(len(text)):
        if remove_seats(text[i].lower()) in "aeiou":
            vowels += 1

    #longest_word
    all_words = text.replace(".", "").replace(",", "").split()
    for word_current in all_words:
        if(len(word_current) > len(longest_word)):
            longest_word = word_current

    #frequency
    rank_words = {}
    words_ = text.strip().replace(".", "").replace(",", "").split()
    for word_current in words_:
        found_word = False
        for key, value in rank_words.items():
            if (word_current == key):
                found_word = True
                rank_words[key] += 1
                break
        if (not(found_word)):
            rank_words[word_current] = 1

    for key, value in rank_words.items():
        # if value > 1: se eu quiser que só apareça as palavras que aparecem mais de uma vez.
        frequency[key] = value

    return {"message": f"     - The number of words in the text is: {words}     - The number of characters in the text is: {characters}"
                       f"     - The number of phrases in the text is: {phrases}     - The number of vowels in the text is: {vowels}"
                       f"     - The longest word in the text is: {longest_word}     - The words frequency is: {frequency}"}

def remove_seats(text):
    text_normalized = unicodedata.normalize("NFD", text)

    text_no_seat = "".join(
        char for char in text_normalized
        if unicodedata.category(char) != "Mn"
    )

    return text_no_seat


# words
def count_words(text):
    return len(text.strip().split())

if __name__ == "__main__":
    app.run(debug=True)