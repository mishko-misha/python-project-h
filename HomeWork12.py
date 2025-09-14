text_for_hashtag = input("Please enter your text to generate to hashtag: ")

text_title = text_for_hashtag.title()
text_with_out_punctuation_gaps = ''.join(char for char in text_title if char.isalnum())
hashtag = '#' + text_with_out_punctuation_gaps[:140]
print(f"Text is generated to new hashtag: {hashtag}")
