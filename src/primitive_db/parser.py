#!/usr/bin/env python3

import shlex


def parse_where_condition(where_clause):
    """
    Парсит условие WHERE в словарь.

    Пример: "age = 28" -> {'age': 28}
    Пример: "name = 'Sergei'" -> {'name': 'Sergei'}
    """
    if not where_clause:
        return None

    try:
        # Разбиваем на части
        parts = shlex.split(where_clause)

        if len(parts) != 3 or parts[1] != '=':
            raise ValueError("Некорректный формат условия WHERE")

        column = parts[0]
        value = parse_value(parts[2])

        return {column: value}
    except Exception as e:
        raise ValueError(f"Ошибка разбора условия WHERE: {e}")


def parse_set_clause(set_clause):
    """
    Парсит условие SET в словарь.

    Пример: "age = 29" -> {'age': 29}
    Пример: "name = 'Ivan'" -> {'name': 'Ivan'}
    """
    updates = {}

    try:
        # Разбиваем по запятым для множественных SET
        assignments = set_clause.split(',')

        for assignment in assignments:
            parts = shlex.split(assignment.strip())

            if len(parts) != 3 or parts[1] != '=':
                raise ValueError("Некорректный формат условия SET")

            column = parts[0]
            value = parse_value(parts[2])
            updates[column] = value

        return updates
    except Exception as e:
        raise ValueError(f"Ошибка разбора условия SET: {e}")


def parse_value(value_str):
    """Парсит строковое значение в соответствующий тип."""
    # Убираем кавычки если есть
    cleaned_value = value_str.strip()
    if (cleaned_value.startswith('"') and cleaned_value.endswith('"')) or \
       (cleaned_value.startswith("'") and cleaned_value.endswith("'")):
        return cleaned_value[1:-1]

    # Убираем запятые в конце (проблема с shlex)
    if cleaned_value.endswith(','):
        cleaned_value = cleaned_value[:-1]

    # Пробуем преобразовать в int
    try:
        return int(cleaned_value)
    except ValueError:
        pass

    # Пробуем преобразовать в bool
    if cleaned_value.lower() == 'true':
        return True
    elif cleaned_value.lower() == 'false':
        return False

    # Оставляем как строку
    return cleaned_value


def parse_values(values_str):
    """Парсит список значений в скобках."""
    # Убираем скобки и разбиваем
    values_str = values_str.strip()
    if values_str.startswith('(') and values_str.endswith(')'):
        values_str = values_str[1:-1]

    try:
        # Разбиваем с учетом кавычек
        parts = shlex.split(values_str)
        values = []

        for part in parts:
            # Убираем запятые которые shlex мог оставить
            clean_part = part.rstrip(',')
            values.append(parse_value(clean_part))

        return values
    except Exception:
        # Fallback: простой split по запятым
        parts = values_str.split(',')
        values = []

        for part in parts:
            clean_part = part.strip()
            values.append(parse_value(clean_part))

        return values
