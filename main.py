from stats import word_count, character_count, book_report
import sys
def get_book_text(filepath):
	with open(filepath) as f:
		text = f.read()
		return text
def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	text = get_book_text(sys.argv[1])
	num_words = word_count(text)
	num_characters = character_count(text)
	new_dict = book_report(num_characters)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for character in new_dict:
		if character["char"].isalpha():
			print(f"{character['char']}: {character['num']}")
	print("============= END ===============")
main()