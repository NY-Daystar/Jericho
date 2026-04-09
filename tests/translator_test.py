from translator import translate

def test_translate_hello(monkeypatch):
    class MockTranslator:
        def translate(self):
            return "bonjour"

    def mock_google_translator():
        return MockTranslator()

    monkeypatch.setattr(
        "translator.GoogleTranslator",
        mock_google_translator
    )

    result, _ = translate("hello")
    print(f"translate result: {result}")
    assert result == "bonjour"