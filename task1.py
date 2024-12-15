import doctest


class Bottle:
    def init(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Бутылка"

        :param capacity_volume: Объем бутылки
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> bottle = Bottle(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем бутылки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_bottle(self) -> bool:
        """
        Функция которая проверяет является ли бутылка пустой

        :return: Является ли бутылка пустой

        Примеры:
        >>> bottle = Bottle(500, 0)
        >>> bottle.is_empty_bottle()
        """
        ...

    def add_water_to_bottle(self, water: float) -> None:
        """
        Добавление воды в бутылку.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бутылке, то вызываем ошибку

        Примеры:
        >>> bottle = Bottle(500, 0)
        >>> bottle.add_water_to_bottle(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def remove_water_from_bottle(self, estimate_water: float) -> None:
        """
        Извлечение воды из бутылки.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в бутылке,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> bottle = Bottle(500, 500)
        >>> bottle.remove_water_from_bottle(200)
        """
        ...


if name == "main":
    doctest.testmod()  # тестирование примеров, которые находятся в документации