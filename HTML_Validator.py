import pytest

def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

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

    return True


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

#     if start != -1:
#         tags.append(html[start])

#     print(tags)

    return tags


