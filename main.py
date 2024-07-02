import re
from pprint import pprint
from collections import defaultdict
import csv


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
# Распределение именных данных по правильным колонкам
for row in contacts_list:
  name_lists = " ".join(row[:3]).split()
  if len(name_lists) == 3:
    row[0], row[1], row[2] = name_lists
  elif len(name_lists) == 2:
    row[0], row[1], row[2] = name_lists[0], name_lists[1], ''
  elif len(name_lists) == 1:
    row[0], row[1], row[2] = name_lists[0], '', ''
  else:
    row[0], row[1], row[2] = '', '', ''
# Редактируем телефонные номера
pattern = r"(\+7|8)( )?(\()?495(\))?( |-)?(\d{3})( |-)?(\d{2})( |-)?(\d{2})(( )?(\(| )?((доб\.) (\d+))(\))?)?"
replacement = r"+7(495)\6-\8-\10\12\15\16"
updated_numbers = []

for row in contacts_list:
  result = re.sub(pattern, replacement, (row[5]))
  row[5] = result
# Объединение дублирующихся записей
# Создаем словарь, где ключ - это кортеж (фамилия, имя), а значение - список остальных данных
data_dict = defaultdict(list)

for row in contacts_list:
    key = (row[0], row[1])  # Фамилия и имя
    value = row[2:]  # Остальные данные

    # Если ключ уже есть в словаре, обновляем данные
    if key in data_dict:
        for i, item in enumerate(value):
            if item and not data_dict[key][i]:
                data_dict[key][i] = item
    else:
        data_dict[key] = value

# Преобразуем словарь обратно в список для вывода
updated_contacts_list = []
for key, value in data_dict.items():
    updated_contacts_list.append(list(key) + value)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(updated_contacts_list)
# for row in contacts_list:
#   print(row)