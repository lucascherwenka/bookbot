def sort_on(items):
	return items["num"]
def word_count(text):
        words = text.split()
        num_words = len(words)
        return num_words
def character_count(text):
	character_dict = {}
	for letter in text:
		ch = letter.lower()
		if ch in character_dict:
			character_dict[ch] += 1
		else:
			character_dict[ch] = 1
	return character_dict
def book_report(character_dict):
	new_list = []
	for character, number in character_dict.items():
		new_dict = {"char": character,"num": number}
		new_list.append(new_dict)
	new_list.sort(reverse=True, key=sort_on)
	return new_list
