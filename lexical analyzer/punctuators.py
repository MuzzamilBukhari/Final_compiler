def match_puncutators(word: str):
    if word in punctuators.keys():
        return punctuators[word]

punctuators = {
    "(": "(",
    ")": ")",
    "{": "{",
    "}": "}",
    "[": "[",
    "]": "]",
    ".": ".",
    ",": ",",
    ":": ":",
    ";":";",
    "?":"?"
}