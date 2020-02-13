import pytest

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    try:
        s = Stack()
        all_tags = _extract_tags(html)
        for tag in all_tags:

            if not tag.__contains__('/'):
                s.push(tag)

            else:
                if s.isEmpty():
                    return False

                else:
                    tag = tag.replace("/", "")
                    top = s.pop()

                    if top != tag:
                        return False

        if s.isEmpty():
            return True

        return False

    except ValueError:
        return False

def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']

    '''

    # list of html tags to be returned
    tags = []
    start = html.find('<')

    if len(html) == 0 or start == -1:
        print(tags)
        return tags
    
    if html.count(">") != html.count("<"):
        raise ValueError('found < without matching >')


    # find first instance of open angle bracket
    index = start

    while index < len(html):

        # close bracket, append tag, and find next instance of open bracket
        if html[index] == '>':
            tags.append(html[start:index+1])
            start = html.find('<', index)

        index += 1


    return tags


