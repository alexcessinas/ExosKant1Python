def get_word_count(sentence):
    # Votre code ici
    count = 0
    for i in sentence.split():
        if(i.isalpha()):
        	count += 1
    return count


def run():
    assert get_word_count("Bonjour") == 1
    assert get_word_count("Bonjour toi") == 2
    assert get_word_count("Bonjour ca va ?") == 3
    assert get_word_count("Bonjour ca va toi ?!") == 4
    assert get_word_count("") == 0