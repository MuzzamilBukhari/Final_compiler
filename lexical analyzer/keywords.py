def match_keywords(word : str):
    if word in keywords.keys():
        return keywords[word]
    return None

keywords = {
    "numberHai": "DT",
    "enumHai": "enum",
    "booleanHai": "DT",
    "charHai": "DT",
    "stringHai": "String",
    "jabTak": "while",
    "leAao": "import",
    "agar": "if",
    "warna": "else",
    "warnaAgar": "elif",
    "wapisDo": "return",
    "sachHai": "bool_const",
    "jhootHai": "bool_const",
    "basRukjao": "flowControl",
    "agyBarho": "flowControl",
    "voidHai": "void",
    "dikhaao": "print",
    "yahaSe": "from",
    "naya": "new",
    "khaali": "null_const",
    "aaneDo": "input",
    "jamaat": "class",
    "ehamHissa": "interface",
    "hai": "extend",
    "nafizkro": "implement",
    "riskLo": "try",
    "errorPakro": "catch",
    "yetoHoga": "finally",
    "hissaHai": "instanceof",
    "ye": "pointer",
    "mustaqil": "static",
    "bareSahab": "super",
    "mehfooz": "AM",
    "zaati": "AM",
    "awami": "AM",
    "hatmi": "final"
}
