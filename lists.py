# Добавление элемента в конец списка (копирование при записи)
def add_element_last(array_, element_):
    new_array = array_.copy()
    new_array.append(element_)
    return new_array
