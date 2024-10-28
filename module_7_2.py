def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding = 'UTF-8')
    strings_positions = {}
    stroka_number = 1
    for value in strings:
        strings_positions[stroka_number, file.tell()] = value
        file.write(value + '\n')
        stroka_number += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)