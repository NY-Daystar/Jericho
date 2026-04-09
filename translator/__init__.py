from deep_translator import GoogleTranslator

from typing import Tuple

def translate(data: str, language_source="en", language_target="fr") -> Tuple[str, Exception]:
    '''translate will translate data from language_source to language_target'''
    gs: GoogleTranslator = GoogleTranslator(source=language_source, target=language_target)
    
    try:
        return gs.translate(data), None
    except Exception as ex:
        return None, ex
