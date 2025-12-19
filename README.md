## This project is a simple database management system written in Python. It allows you to create tables and add, update, delete, and read records via the command line.

It is recommended to use Poetry for dependency management.

**Features**

1. Create and delete tables
2. Insert, read, update, and delete data
3. Supported data types: int, str, bool
4. Automatic ID generation
5. Pretty table output
6. Confirmation for dangerous operations


🎥 asciicast recording:
https://asciinema.org/a/Z5LxhUzXS2bDU7f25Yr30sSjv

Data Commands

insert into <table> values (<value1>, <value2>, ...) — insert a record

select from <table> — display all records

select from <table> where <condition> — display records by condition

update <table> set <column>=<value> where <condition> — update records

delete from <table> where <condition> — delete records

info <table> — display table information

**Usage Example**
create_table users name:str age:int is_active:bool
insert into users values ("lock", 28, true)
select from users
update users set age = 28 where name = "lock"
delete from users where age = 28
info users
---

## Проект представляет собой простую систему работы с базой данных на Python. Позволяет создавать таблицы, добавлять, обновлять, удалять и читать записи через командную строку.

## Установка

Рекомендуется использовать [Poetry](https://python-poetry.org/) для управления зависимостями.

Склонируйте репозиторий:
   git clone https://github.com/akemi-aiai/antoshina-project2-25-555.git
   cd antoshina-project2-25-555

## Установите зависимости:
poetry install
или через make:
make install

## Запуск
make project


## Возможности

- Создание и удаление таблиц
- Добавление, чтение, обновление и удаление данных
- Поддержка типов данных: int, str, bool
- Автоматическая генерация ID
- Красивый табличный вывод
- Подтверждение опасных операций
- Кэширование запросов
- Логирование времени выполнения

## Демонстрация работы проекта

asciicast https://asciinema.org/a/Z5LxhUzXS2bDU7f25Yr30sSjv


### Команды для работы с данными:

- insert into <таблица> values (<значение1>, <значение2>, ...) - добавить запись
- select from <таблица> - показать все записи
- select from <таблица> where <условие> - показать записи по условию
- update <таблица> set <столбец>=<значение> where <условие> - обновить записи
- delete from <таблица> where <условие> - удалить записи
- info <таблица> - информация о таблице

### Пример использования:

1) create_table users name:str age:int is_active:bool
2) insert into users values ("lock", 28, true)
3) select from users
4) update users set age = 28 where name = "lock"
5) delete from users where age = 28
6) info users
