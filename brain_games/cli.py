import prompt

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ', empty=True)
    name = name if name else 'Friend'
    print('Hello, {}!'.format(name))

