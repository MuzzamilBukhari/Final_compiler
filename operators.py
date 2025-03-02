def match_operators(word: str):
    if word in operators.keys():
        return operators[word]


operators = {
    "+": "PM",
    "-": "PM",
    
    "*": "MDME",
    "/": "MDME",
    "%": "MDME",
    "^": "MDME",
    
    "!=": "RO2",
    "==": "RO2",
    
    "<": "RO1",
    ">": "RO1",
    "<=": "RO1",
    ">=": "RO1",
    
    "AUR": "LO2",
    "YA": "LO2",
    
    "=": "=",
    
    "+=": "COMPASS",
    "-=": "COMPASS",
    "*=": "COMPASS",
    "/=": "COMPASS",
    "^=": "COMPASS",
    "%=": "COMPASS",
    
    "NAHI": "LO1"
}
