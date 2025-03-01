class Post:
    """
    Базовый класс для представления публикации в социальной сети.

    Атрибуты:
        author_ (str): Автор публикации.
        content_ (str): Содержимое публикации.
        __status (str): Статус публикации (по умолчанию "Draft"). Это приватный атрибут, чтобы пользователь не мог
        его изменять.

    Ошибки:
        TypeError: Если `author_` не является строкой.
        ValueError: Если `content_` не является строкой.
    """
    def __init__(self, author_: str, content_: str, __status = "Draft"):
        """
        Инициализирует объект Post.

        Аргументы:
            author_ (str): Автор публикации.
            content_ (str): Содержимое публикации.
            __status (str, optional): Статус публикации. По умолчанию "Draft".
        """
        if not isinstance(author_, str):
            raise TypeError("Имя автора должно быть типа str")
        self.author_ = author_  # Автор

        if not isinstance(content_, str):
            raise ValueError("Содержимое публикации должно быть типа str")
        self.content_ = content_  # Содержимое

    def __str__(self):
        """
        Возвращает строковое представление объекта Post:
            str: Строковое представление объекта Post.
        """
        return f'Автор "{self.author_}", содержимое: "{self.content_}"'

    def __repr__(self):
        """
        Возвращает строковое представление объекта Post для отладки:
            str: Строковое представление объекта Post для отладки.
        """
        return f"Post(author_={self.author_}, content_='{self.content_}')"

    def publish(self):
        """
        Устанавливает статус публикации как "Published".
        """
        self.__status = "Published"

    def delete(self):
        """
        Устанавливает статус публикации как "Deleted".
        """
        self.__status = "Deleted"

class TextPost(Post):
    """
    Класс для представления текстового поста, наследуется от класса Post.

    Атрибут:
        text (str): Текст поста.
    """
    def __init__(self, author_: str, text: str):
        """
        Инициализирует объект TextPost.

        Аргументы:
            author_ (str): Автор поста.
            text (str): Текст поста.
        """
        super().__init__(author_, text, __status = "Draft")

    def __str__(self):
        """
        Возвращает строковое представление объекта TextPost:
            str: Строковое представление объекта TextPost.
        """
        return f'Автор "{self.author_}", текст поста: "{self.content_}"'

    def __repr__(self):
        """
        Возвращает строковое представление объекта TextPost для отладки:
            str: Строковое представление объекта TextPost для отладки.
        """
        return f"{self.__class__.__name__}(author_={self.author_}, text={self.content_})"

class VideoPost(Post):
    """
    Класс для представления видео поста, наследуется от класса Post.

    Атрибуты:
        duration (float): Длительность видео поста.
    """
    def __init__(self, author_: str, content_: str, duration: float):
        """
        Инициализирует объект VideoPost.

        Аргументы:
            author_ (str): Автор поста.
            content_ (str): Описание видео.
            duration (float): Длительность видео поста.
        """
        super().__init__(author_, content_, __status = "Draft")
        self.duration = duration  # Длительность видео

    def __str__(self):
        """
        Возвращает строковое представление объекта VideoPost:
            str: Строковое представление объекта VideoPost.
        """
        return f'Автор "{self.author_}", описание видео: "{self.content_}". Длительность: "{self.duration}"'

    def __repr__(self):
        """
        Возвращает строковое представление объекта VideoPost для отладки:
            str: Строковое представление объекта VideoPost для отладки.
        """
        return (f"{self.__class__.__name__}(author_={self.author_}, content_={self.content_},"
                f" duration={self.duration})")