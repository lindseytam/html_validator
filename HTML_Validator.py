def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''


    all_tags = _extract_tags(html)

    # if there's an odd number of tags, no need to compute anything
    if len(all_tags) % 2 == 1:
        print("False")
        return False

    j = 0

    while len(all_tags) > 0 and j < len(all_tags) - 1:

        if all_tags[j] == all_tags[j + 1].replace("/", "") and len(all_tags[j]) < len(all_tags[j+1]):
            del all_tags[j + 1]
            del all_tags[j]
            print(all_tags)
            j -= 1
        else:
            j += 1

    print(len(all_tags) == 0)
    return len(all_tags) == 0


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

    if len(html) == 0:
        print(tags)
        return tags

    if len(html) == 1 and (html.find('<') != -1 or html.find('>') != -1):
        tags.append(html)
        return tags


    # find first instance of open angle bracket
    index = start

    while index < len(html):

        # close bracket, append tag, and find next instance of open bracket
        if html[index] == '>' or html[index] == ' ':
            tags.append(html[start:index+1])
            start = html.find('<', index)


        index += 1

    print(tags)
    return tags


# html = 'this is a <strong test'
html = 'this is a <strong test'
_extract_tags(html)
validate_html(html)
