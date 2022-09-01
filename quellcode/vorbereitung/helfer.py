def frage(frage: str, default: str = None) -> str:
    """
    Fragt eine Eingabe ab und gibt diese zurück.
    Wenn keine Eingabe erfolgt wird der Default-Wert zurückgegeben.
    """
    extra = ""
    if default is not None:
        extra = " [{}]".format(default)

    eingabe = input(f"{frage}{extra}: ")
    if eingabe == "":
        return default
    return eingabe
