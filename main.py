import os
import re

phoneme_dir = "phonemes"

def get_phoneme(word,tone):
    return phoneme_dir + "/" + word + tone + ".mp3"

def play_file(f):
    os.system("mplayer " + f)

def split_phoneme(phon):
    match = re.match(r"([a-z]+)([0-9]+)", phon, re.I)
    return match.groups()

def play_word(word):
    base,tone = split_phoneme(word)
    f = get_phoneme(base,tone)
    play_file(f)


def play_sentence(sen):
    #TODO
    # Add more sophisticated rules to playback
    # i.e Tone changing rules, smoother transitions between words, etc
    
    [play_word(w) for w in sen.split(" ")]

if __name__ == "__main__":
    sentence = "ni3 hao3"
    play_sentence(sentence)
