"""Translator module: function to translate from google """

from typing import Tuple

from deep_translator import GoogleTranslator

def translate(data: str, language_source="en", language_target="fr") -> Tuple[str | None, Exception | None]:
    """ Translate: will translate data from language_source to language_target """
    try:
        gs: GoogleTranslator = GoogleTranslator(source=language_source, target=language_target)
        return gs.translate(data), None
    except Exception as ex:
        return None, ex
