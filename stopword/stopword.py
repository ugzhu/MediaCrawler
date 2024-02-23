from pathlib import Path

def init() -> str:
    str = ""
    with open(Path(__file__).parent.resolve() / 'stopwords.txt', 'r', encoding='utf-8') as file:
        str += f"{file.read()},"
    return str
        
