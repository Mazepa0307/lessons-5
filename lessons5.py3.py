import string
def create_hashtag(input_string):
    translator = str.maketrans('', '', string.punctuation + '')
    cleaned_string = input_string.translate(translator)

    hashtag = cleaned_string.title()

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    hashtag = f'#{hashtag}'
    return hashtag

user_input = input('Enter a string: ')
print(create_hashtag(user_input))