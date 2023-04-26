def bad_open(file_path, mode):
    """Некорректная функция открытия файла"""
    raise Exception


def open_and_close_file(file_path):
    """Открывает и закрывает файл

    Args:
        file_path: путь до файла
    """
    with open('./description.md', 'r') as f:
        f.close()
