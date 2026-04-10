"""Handle user's input """

__all__ = ["ask_folder"]

from os.path import exists
from typing import Tuple, Set

def ask_yes_no(question:str) -> bool :
    """AskYesNo : ask input user to get yes or no """
    value: str= input(f"{question} (Y/n) ? ")
    values: Set[str] = set(['y', 'Y', 'yes', 'Yes'])
    return value in values

def ask_folder(question: str, default:str, check:bool = True) -> Tuple[str, bool] :
    """AskFolder : ask input user to get folder path """
    folder: str = input(f"\n{question} (default: {default}) : ")
    if not folder:
        folder=default
    exist: bool = exists(folder)
    if not exist and check:
        return folder, ask_yes_no("Your folder doesn't exists, do you want to continue")
    return folder, True
