# Python CLI Database Engine

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-Database%20Management-7C5CFF)
![CRUD](https://img.shields.io/badge/CRUD-Create%20%7C%20Read%20%7C%20Update%20%7C%20Delete-orange)
![Data Types](https://img.shields.io/badge/Data%20Types-int%20%7C%20str%20%7C%20bool-purple)
![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Management-60A5FA?logo=poetry&logoColor=white)
![Makefile](https://img.shields.io/badge/Makefile-Automation-lightgrey)
![Storage](https://img.shields.io/badge/Storage-JSON%20Files-green)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-lightgrey)

**DataBasePython** is a command-line database management system written in Python.

**Features**

1. Create and delete tables
2. Insert, read, update, and delete data
3. Supported data types: int, str, bool
4. Automatic ID generation
5. Pretty table output
6. Confirmation for dangerous operations


🎥 asciicast recording:
https://asciinema.org/a/Z5LxhUzXS2bDU7f25Yr30sSjv

**Data Commands**

- insert into <table> values (<value1>, <value2>, ...) -insert a record
- select from <table> —display all records
- select from <table> where <condition> -display records by condition
- update <table> set <column>=<value> where <condition> —update records
- delete from <table> where <condition> —delete records
- info <table> —display table information

**Usage Example**
1) create_table users name:str age:int is_active:bool
2) insert into users values ("lock", 28, true)
3) select from users
4) update users set age = 28 where name = "lock"
5) delete from users where age = 28
6) info users

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
