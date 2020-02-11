import HTML_Validator


def test__extract_tags_1():
    with pytest.raises(ValueError, match='found < without matching >'):
        HTML_Validator._extract_tags('<')

def test__extract_tags_2():
    with pytest.raises(ValueError, match='found < without matching >'):
        HTML_Validator._extract_tags('this is a <strong test')

def test__extract_tags_3():
    assert HTML_Validator._extract_tags('this is a <strong test>') == ['<strong test>']

def test__extract_tags_4():
    with pytest.raises(ValueError, match='found < without matching >'):
        HTML_Validator._extract_tags('this is a <strong< test')


def test_validate_html_1():
    assert not HTML_Validator.validate_html('<')

def test_validate_html_2():
    assert not HTML_Validator.validate_html('this is a <strong test')

def test_validate_html_3():
    assert not HTML_Validator.validate_html('this is a <strong test>') == ['<strong test>']

def test_validate_html_4():
    assert not HTML_Validator.validate_html('this is a <strong< test')

