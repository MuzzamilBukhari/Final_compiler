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
    
    "&": "LO2",
    "|": "LO2",
    
    "=": "=",
    
    "+=": "COMPASS",
    "-=": "COMPASS",
    "*=": "COMPASS",
    "/=": "COMPASS",
    "^=": "COMPASS",
    "%=": "COMPASS",
    
    "!": "LO1"
}
