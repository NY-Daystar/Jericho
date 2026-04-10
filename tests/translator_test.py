"""poetry run pytest tests/translator_test.py -s """
 
import translator

def test_translate():
    expected: str = "Bonjour"
    value: str = "Hello"
    
    result, err = translator.translate(value)

    assert not err
    assert result == expected

def test_translate_error():
    value: str = ""
    
    _, err = translator.translate(value, 'language_source_bizarre')

    assert err
