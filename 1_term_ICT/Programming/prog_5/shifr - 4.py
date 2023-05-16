'''
Написать программу «Шифровальщик». Функция шифрования принимает 2 аргумента: строку, которую нужно зашифровать, и ключ
шифрования, и возвращает строку, зашифрованную путем применения функции «^» (XOR) над символами строки с ключом.
В программе предусмотреть грамотное взаимодействие с пользователем.
	* Пользователь вводит строку и ключ, в ответ получает зашифрованные символы;
	* Написать также функцию расшифровки, которая по зашифрованной строке и ключу восстанавливает исходную строку.
'''

alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюabcdefghijklmnoprstuvwxyАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮABCDEFGHIJKLMNOPRSTUVWXY .,:/\|-+=_'

def crypt(text, key):
    cr_text = ''
    for i in text:
         cr_text = cr_text + chr(ord(i) ^ int(key))  # ord преобразовывает символ в номер, а chr наоборот
    return cr_text

def decrypt(cr_text, key):
    return crypt(cr_text, key)

def txt():
    print('---------------------------------------------------')
    text = input('Введите текст: ')
    key = input('Введите ключ шифрования (число): ')
    for k in key:
        if k in alf:
            print('Ошибка! Неправильный ввод.')
            break
    else:
        print('---------------------------------------------------')
        print('Зашифрованный текст:', crypt(text, int(key)))
        print('Расшифрованный текст:', decrypt(crypt(text, key), int(key)))
        main()

def main():

    print('---------------------------------------------------\n'
          'Действие:\n'
          '1 - Зашифровать/расшифровать текст\n'
          'Q - Выход из программы\n')

    ans = input('Введите действие: ')
    if ans != '':
        for k in ans:
            if k in alf:
                print('Ошибка! Неправильный ввод.')
                main()
                break

        if ans == 'q' or ans == 'Q':
            print('---------------------------------------------------')
            print('Был произведен выход из программы.')
            exit(0)
        elif int(ans) == 1:
            txt()
        else:
            print('Ошибка! Неправильный ввод.')
            main()
    else:
        print('Ошибка! Неправильный ввод.')
        main()

main()