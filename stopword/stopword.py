from pathlib import Path
from tools import utils

def init() -> str:
    with open(Path(__file__).parent.resolve() / 'stopwords.txt', 'r', encoding='utf-8') as file:
        content = ','.join(line.strip() for line in file)
    return content
     

        
