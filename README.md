### Команды для работы с данными:

- `insert into <таблица> values (<значение1>, <значение2>, ...)` - добавить запись
- `select from <таблица>` - показать все записи
- `select from <таблица> where <условие>` - показать записи по условию
- `update <таблица> set <столбец>=<значение> where <условие>` - обновить записи
- `delete from <таблица> where <условие>` - удалить записи
- `info <таблица>` - информация о таблице

### Пример использования:

create_table users name:str age:int is_active:bool
insert into users values ("Sergei", 28, true)
select from users
update users set age = 29 where name = "Sergei"
delete from users where age = 28
info users
