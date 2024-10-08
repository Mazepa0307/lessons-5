import string
def create_hashtag(input_string):
    translator = str.maketrans('', '', string.punctuation + '')
    cleaned_string = input_string.translate(translator)

    hashtag = ''.join(word.capitalize() for word in cleaned_string.split())
    hashtag = f'#{hashtag}'

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

user_input = input('Enter a string: ')
print(create_hashtag(user_input))
