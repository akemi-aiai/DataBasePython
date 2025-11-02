#!/usr/bin/env python3

import json
import os


def load_metadata(filepath="db_meta.json"):
    """Загружает метаданные из JSON файла."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_metadata(data, filepath="db_meta.json"):
    """Сохраняет метаданные в JSON файл."""
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_table_data(table_name, data_dir="data"):
    """Загружает данные таблицы из JSON файла."""
    os.makedirs(data_dir, exist_ok=True)
    filepath = os.path.join(data_dir, f"{table_name}.json")

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_table_data(table_name, data, data_dir="data"):
    """Сохраняет данные таблицы в JSON файл."""
    os.makedirs(data_dir, exist_ok=True)
    filepath = os.path.join(data_dir, f"{table_name}.json")

    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
