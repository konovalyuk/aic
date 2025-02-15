import re

def extract_placeholders(file_path):
    """Извлекает значения {{ ... }} из HTML-шаблона."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return re.findall(r"{{\s*(\w+)\s*}}", content)
