import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# Распределение именных данных по правильным колонкам
# for row in contacts_list:
#   name_lists = " ".join(row[:3]).split()
#   if len(name_lists) == 3:
#     row[0], row[1], row[2] = name_lists
#   elif len(name_lists) == 2:
#     row[0], row[1], row[2] = name_lists[0], name_lists[1], ''
#   elif len(name_lists) == 1:
#     row[0], row[1], row[2] = name_lists[0], '', ''
#   else:
#     row[0], row[1], row[2] = '', '', ''
# Редактируем телефонные номера
pattern = r"(\+7|8)( )?(\()?495(\))?( |-)?(\d+)( |-)?(\d+)( |-)?(\d+)( (\()?(доб\. \d+)(\))?)?"
replacement = r"+7(495)\6-\8-\10 \13"
updated_numbers = []
for row in contacts_list:
  result = re.sub(pattern, replacement, (row[5]))
  updated_numbers = updated_numbers.append(result)
print(updated_numbers)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
# for row in contacts_list:
#   print(row)