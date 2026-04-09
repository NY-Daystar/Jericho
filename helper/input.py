from os.path import exists
from typing import Tuple

def askYesNo(question:str) -> bool :
    value: str= input(f"{question} (Y/n) ? ")
    return value == "Y" or value == "y" or value == "yes" or value == "Yes"

def askFolder(question: str, default:str, check:bool = True) -> Tuple[str, bool] :
    folder: str = input(f"\n{question} (default: {default}) : ")
    if folder == "": folder=default
    exist: bool = exists(folder)
    if not exist and check:
        return folder, askYesNo(f"Your folder doesn't exists, do you want to continue")
    return folder, True