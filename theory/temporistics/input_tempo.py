import re
import io
import os
import nltk
import pyperclip
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize

nltk.download('punkt')

folder_path = r"C:\Users\OlegP\Downloads\temporistics\temporistics.ru\PrettyNames"
neural_network_limit = 5000 # ліміт токенів для одного виклику нейромережі

# проходимо по всіх файлах у папці PrettyNames
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # ігноруємо папки та файли без розширення
    if os.path.isdir(file_path) or not filename.endswith(".html"):
        continue

    # відкриваємо файл та зчитуємо його вміст
    with io.open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

# створюємо об'єкт BeautifulSoup для парсінгу html
soup = BeautifulSoup(html, "html.parser")

# прибираємо меню з HTML-коду
skip_menu = soup.find("div", {"id": "skip-link"})
if skip_menu:
    skip_menu.decompose()

top_bg = soup.find("div", {"class": "top-bg"})
if top_bg:
    top_bg.decompose()

breadcrumb = soup.find("div", {"class": "breadcrumb"})
if breadcrumb:
    breadcrumb.decompose()

# витягуємо текст з html
text = soup.get_text(strip=True)

# токенізуємо текст почастинно
for i, part_text in enumerate(re.findall(r'\S.{0,4998}\S(?<=\w)', text)):
    tokens = word_tokenize(part_text)
    num_tokens = len(tokens)
    part_name = f"{filename}_part{i+1}"
    print(f"Файл {filename} містить {num_tokens} токенів у частині {i+1}")
    pyperclip.copy(part_text)
    input(f"Натисніть Enter, щоб вставити частину {i+1} ({part_name}) в буфер обміну та продовжити...")

