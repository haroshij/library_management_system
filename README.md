# Система управление библиотекой

## Программа позволяет управлять библиотекой. Реализованы следующие действия:
1. Добавлять книги.
2. Удалять книги.
3. Искать книги.
4. Отображать список всех книг библиотеки.
5. Менять статус книги.

## Управление библиотекой осущетсвляется через консоль терминала:
1. На Windows необходимо вызвать программу через команду `python путь_к_файлу набор_аргументов_и_команд`.
2. После нажать клавишу Enter.

## Добавление книги
1. На место `набора_аргументов_и_команд` вводите `-с -ab`. Вместо `-ab` можно использовать также `addbook`, `add_book`.
2. Через пробел вводите следующие аргументы:
   - `-t название_книги`. Вместо `-t` можете использовать `--title`.
   - `-a автор_произведения`. Вместо `-a` можете использовать `--author`.
   - `-y год_издания`. Вместо `-y` можете использовать `--year`.
3. Пример: `$ python c:/main_program -c ab -a T.Testov -t Test -y 1999`.

**Важно**: *навзвание книги, имя автора вводятся без пробелов. При необходимости используйте символ нижнего подчёркивания*.


## Удаление книги
1. На место `набора_аргументов_и_команд` вводите `-c -db`. Вместо `-db` можно использовать также `delbook`, `del_book`, `deletebook`, `delete_book`.
2. Через пробел вводите ID книги:
   - `-i ID_книги`. Вместо `-i` можете использовать `--id`.
3. Пример: `$ python c:/main_program -c delbook --id 1239`.

## Поиск книги
1. На место `набора_аргументов_и_команд` вводите `-с -fb`. Вместо `-fb` можно использовать также `findbook`, `find_book`.
2. Через пробел вводите слово(-а) для поиска:
   - `-kw слово_для_поиска`. Вместо `-kw` можете использовать `--keyword`.

**Важно**: *ключевые слова вводятся без пробелов. При необходимости используйте символ нижнего подчёркивания*.

3. Пример: `$ python c:/main_program -c find_book -kw Eugeny_O`.

## Отображение списка всех книг
1. На место `набора_аргументов_и_команд` вводите `-c -vb`. Вместо `-vb` можно использовать также `viewbooks`, `view_books`, `viewbook`, `view_book`.
2. Пример: `$ python c:/main_program -c view_books`.

## Изменение статуса книги
1. На место `набора_аргументов_и_команд` вводите `-c -cs`. Вместо `-cs` можно использовать также `changestatus`, `change_status`.
2. Через пробел вводите следующие аргументы:
   - `-i ID_книги`. Вместо `-i` можете использовать `--id`.
   - `-s статус_книги`. Вместо `-s` можете использовать `--status`.

**Важно**: *есть только два возможных статуса книги: `выдана` и `в наличии`*.

3. Пример: `$ python c:/main_program -c change_status --id 2172 --status выдана`.
