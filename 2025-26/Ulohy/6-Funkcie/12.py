def remove_spaces(text: str) -> str:
    new_text = ""

    for char in text:
        if char != " ":
            new_text += char

    return new_text
