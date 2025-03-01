class Book():
  """ Базовый класс книги"""
  # атрибуты
  def __init__(self, name:str,author:str):
    self.__name = name
    self.__author = author
  # get, set


  @property
  def name(self):
    return self.__name
  @property
  def author(self):
    return self.__author

  #методы-описания
  def str(self):
    return f"Book name:{self.name}, author:{self.author}"

  def repr(self):
    return f"Book name:{self.name}({type(self.name)}), author:{self.author}({type(self.name)})"

class PaperBook(Book):
  """ Дочерний класс Бумажные книги"""
  def __init__(self, name:str, author:str, pages:int):
    if isinstance(pages, int):
      if pages>0:
        self._pages = pages
      else:
        raise ValueError("Количество страниц не может быть равно или меньше нуля!")
    else:
      raise TypeError("Количество страниц должно быть целым")
  def set_pages(self, pages: int):
    if isinstance(pages, int):
      if pages>0:
        self._pages = pages
      else:
        raise ValueError("Количество страниц не может быть равно или меньше нуля!")
    else:
      raise TypeError("Количество страниц должно быть целым")
  #методы-описания
  def str(self):
    return f"Book name:{self.name}, author:{self.author}. There are {self.pages} pages."

  def repr(self):
    return f"Book name:{self.name}({type(self.name)}), author:{self.author}({type(self.name)}, pages:{self.pages}({type(self.pages)})"


class AudioBook(Book):
  """ Дочерний класс Аудио-книги"""
  def __init__(self, name:str, author:str, duration:float):
    if isinstance(duration, float):
      if duration>0:
        self._duration = duration
      else:
        raise ValueError("Продолжительность записи аудио-книги не может быть равна или меньше нуля!")
    else:
      raise TypeError("Продолжительность записи аудио-книги - это число (тип float)")
  def set_duration(self, duration:float):
    if isinstance(duration, float):
      if duration>0:
        self._duration = duration
      else:
        raise ValueError("Продолжительность записи аудио-книги не может быть равна или меньше нуля!")
    else:
      raise TypeError("Продолжительность записи аудио-книги - это число (тип float)")
  #методы-описания
  def str(self):
    return f"Book name:{self.name}, author:{self.author}. The duration is {self.duration} m."

  def repr(self):
    return f"Book name:{self.name}({type(self.name)}), author:{self.author}({type(self.name)}, duration:{self.duration}({type(self.duration)})"

kolobok = PaperBook("Kolobok","UNT",10)
repka = AudioBook("Repka","UNT",5.5)
gusi_lebedi= Book("Gusi-lebedi","UNT")