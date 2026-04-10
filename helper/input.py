"""handle user's input"""

__all__ = ["ask_folder"]

from os.path import exists
from typing import Tuple, Set

def ask_yes_no(question:str) -> bool :
    """askYesNo : ask input user to get yes or no"""
    value: str= input(f"{question} (Y/n) ? ")
    values: Set[str] = set(['y', 'Y', 'yes', 'Yes'])
    return value in values
    # TODO return value == "Y" or value == "y" or value == "yes" or value == "Yes"

def ask_folder(question: str, default:str, check:bool = True) -> Tuple[str, bool] :
    """askFolder : ask input user to get folder path"""
    folder: str = input(f"\n{question} (default: {default}) : ")
    if not folder:
        folder=default
    exist: bool = exists(folder)
    if not exist and check:
        return folder, ask_yes_no("Your folder doesn't exists, do you want to continue")
    return folder, True
