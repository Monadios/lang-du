import os

phoneme_dir = "phonemes"

def make_file(word,tone):
    return phoneme_dir + "/" + word + tone + ".mp3"

def play_file(f):
    os.system("mplayer " + f)

if __name__ == "__main__":
    ni3 = make_file("ni", "3")
    hao3 = make_file("hao", "3")
    play_file(ni3)
    play_file(hao3)
