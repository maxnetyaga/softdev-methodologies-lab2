from copy import deepcopy


type char = str


class List:
    @staticmethod
    def check_char(char):
        if type(char) != str or len(char) != 1:
            raise ValueError("Element must be a character")

    def __init__(self, *chars) -> None:
        for char in chars:
            List.check_char(char)

        self._data = list(chars)

    def __str__(self) -> str:
        return "".join(self._data)

    def length(self) -> int:
        '''Операція визначення довжини списку.

        Якщо список непорожній, то ця операція повинна повертати кількість елементів у списку.
        Якщо список порожній, то ця операція повинна повертати 0.
        '''
        return len(self._data)

    def get(self, index: int) -> char:
        '''Операція отримання елементу списку на довільній позиції.

        У випадку передачі некоректного значення позиції (наприклад, від’ємне число, або число, більше за індекс
        останнього елементу списку) метод повинен генерувати виключну ситуацію.
        '''
        if index < 0:
            raise IndexError()

        return self._data[index]

    def append(self, element: char) -> None:
        '''Операцію додавання елементу в кінець списку.'''
        List.check_char(element)

        self._data.append(element)

    def extend(self, elements: "List") -> None:
        '''Операцію розширення списку.

        Метод приймає інший список та додає до поточного списку усі елементи останнього.
        При цьому подальші зміни в другий список не повинні впливати на перший.
        '''
        self._data.extend(elements._data)

    def delete(self, index: int) -> char:
        '''Операцію видалення елементу зі списку на вказаній позиції.

        Метод повинен повертати значення того елементу, який видаляється.
        Нумерація елементів списку починається з 0.
        У випадку передачі некоректного значення позиції (наприклад, від’ємне число, або число, більше за індекс
        останнього елементу списку) метод повинен генерувати виключну ситуацію
        '''
        if index < 0:
            raise IndexError()
    
        return self._data.pop(index)

    def deleteAll(self, element: char) -> None:
        '''Операцію видалення елементів зі списку за значенням.

        Метод видаляє зі списку усі елементи, які за значенням відповідають шуканому.
        У випадку передачі елемента, який у списку відсутній, жодні зміни до списку не застосовуються.
        '''
        List.check_char(element)

        self._data = [x for x in self._data if x != element]

    def clone(self) -> "List":
        '''Операція копіювання списку.

        При виклику повинен створити копію поточного списку та повернути її.
        '''
        return deepcopy(self)

    def reverse(self) -> None:
        '''Операція обернення списку.

        Метод повинен змінити порядок елементів у поточному списку задом наперед.
        Елемент, що був останнім стане першим, передостаннім — другим, … а перший — останнім.
        '''
        self._data.reverse()

    def findFirst(self, element: char) -> int:
        '''Операція пошуку елемента за значенням з голови списку.

        Метод повинен знайти перший елемент у списку, що дорівнює шуканому та повернути його позицію.
        Нумерація елементів списку починається з 0.
        У випадку відсутності шуканого елемента у списку, метод повертає -1
        '''
        List.check_char(element)

        try:
            return self._data.index(element)
        except ValueError:
            return -1

    def findLast(self, element: char) -> int:
        '''Операція пошуку елемента за значенням з хвоста списку.

        Метод повинен знайти останній елемент у списку, що дорівнює шуканому та повернути його позицію.
        Нумерація елементів списку починається з 0.
        У випадку відсутності шуканого елемента у списку, метод повертає -1.
        '''
        List.check_char(element)

        try:
            return len(element) - 1 - self._data.index(element[::-1])
        except ValueError:
            return -1

    def clear(self) -> None:
        '''Операцію очищення списку.

        Метод видаляє усі елементи списку.
        '''
        self._data.clear()
