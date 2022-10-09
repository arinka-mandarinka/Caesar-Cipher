# Возвращает расшифрованный символ с учетом 
# выхода за пределы заданного алфавита.
def get_encrypted_char(c, sh, alphabet):
    return alphabet[(alphabet.index(c) + sh) % len(alphabet)] 

# Доступные алфавиты.
latinLowerCase = list(map(chr, range(ord('a'), ord('z') + 1)))
latinUpperCase = list(map(chr, range(ord('A'), ord('Z') + 1)))
сyrillicLowerCase = list(map(chr, range(ord('а'), ord('я') + 1)))
cyrillicUpperCase = list(map(chr, range(ord('А'), ord('Я') + 1)))

strToEncrypt = input('Введите строку для шифрования/расшифрования шифром Цезаря: ')

# Проверка при вводе числа.
while True:
    try:
        sh = int(input('Введите сдвиг (цифру): '))
    except:
        print('Сдвиг введен неверно! Попробуйте ещё раз...')
        continue
    break

# Анализируем каждый символ заданной строки 
# и определяем на вхождение в доступные алфавиты.
encryptedStr = []
for c in strToEncrypt:
    if c in latinLowerCase:
        encryptedStr.append(get_encrypted_char(c, sh, latinLowerCase))
    elif c in latinUpperCase:
        encryptedStr.append(get_encrypted_char(c, sh, latinUpperCase))
    elif c in сyrillicLowerCase:
        encryptedStr.append(get_encrypted_char(c, sh, сyrillicLowerCase))
    elif c in cyrillicUpperCase:
        encryptedStr.append(get_encrypted_char(c, sh, cyrillicUpperCase))
    else:
        encryptedStr.append(c)

# Выводим список преобразованный в строку.
print(''.join(encryptedStr))

