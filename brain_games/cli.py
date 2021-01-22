# -*- coding:utf-8 -*-

"""helper function."""

import prompt


def welcome_user():
    """Print welcome.

    get user name from input line
    and print greeting on screen.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ', empty=True)
    name = name if name else 'Friend'
    print('Hello, {0}!'.format(name))
