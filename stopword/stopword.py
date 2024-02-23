def init() -> str:
    str = ""
    with open('path/to/your/file.txt', 'r', encoding='utf-8') as file:
        str += f"{file.read()},"
    return str
        
