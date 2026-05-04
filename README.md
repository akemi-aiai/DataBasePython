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

## Commands

| Command | Description |
|---|---|
| `create_table users name:str age:int is_active:bool` | Create a new table with typed fields |
| `insert into users values ("Alice", 28, true)` | Insert a new record |
| `select from users` | Display all records |
| `select from users where age = 28` | Display records by condition |
| `update users set age = 29 where name = "Alice"` | Update matching records |
| `delete from users where age = 29` | Delete matching records |
| `info users` | Display table information |


### Examples:

1) create_table users name:str age:int is_active:bool
2) insert into users values ("lock", 28, true)
3) select from users
4) update users set age = 28 where name = "lock"
5) delete from users where age = 28
6) info users
