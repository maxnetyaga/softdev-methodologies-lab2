type char = str


def check_char(char):
    if type(char) != str or len(char) != 1:
        raise ValueError("Element must be a character")


class _ListNode:
    def __init__(self, value: char, next: "_ListNode | None" = None) -> None:
        check_char(value)
        self.value = value
        self.next = next


class List:
    def __init__(self, *chars) -> None:
        if not chars:
            self.clear()
            return

        for char in chars:
            check_char(char)

        self._head = _ListNode(chars[0])
        self._tail = self._head

        cur_node = self._head
        for char in chars[1:]:
            cur_node.next = _ListNode(char)
            cur_node = cur_node.next
            self._tail = cur_node

        # Cyclic list
        self._tail.next = self._head

        self._length = len(chars)

    def __str__(self) -> str:
        if not self._head:
            return ""

        result = ""

        cur_node = self._head
        while True:
            assert cur_node

            result += cur_node.value

            cur_node = cur_node.next
            if cur_node is self._head:
                break

        return result

    def __eq__(self, value: "List") -> bool:
        return (isinstance(value, List)
                and str(self) == str(value))

    def length(self) -> int:
        '''Операція визначення довжини списку.

        Якщо список непорожній, то ця операція повинна повертати кількість елементів у списку.
        Якщо список порожній, то ця операція повинна повертати 0.
        '''
        return self._length

    def _get_node(self, index: int) -> _ListNode:
        if index < 0 or index >= self.length():
            raise IndexError()

        cur_node = self._head
        cur_node_i = 0
        while True:
            assert cur_node

            if cur_node_i == index:
                return cur_node

            cur_node = cur_node.next
            cur_node_i += 1

    def get(self, index: int) -> char:
        '''Операція отримання елементу списку на довільній позиції.

        У випадку передачі некоректного значення позиції (наприклад, від’ємне число, або число, більше за індекс
        останнього елементу списку) метод повинен генерувати виключну ситуацію.
        '''
        return self._get_node(index).value

    def append(self, element: char) -> None:
        '''Операцію додавання елементу в кінець списку.'''
        check_char(element)

        if not self._head:
            self._head = _ListNode(element)
            self._tail = self._head
            self._tail.next = self._head

        else:
            assert self._tail

            self._tail.next = _ListNode(element)
            self._tail = self._tail.next
            self._tail.next = self._head

        self._length += 1

    def extend(self, elements: "List") -> None:
        '''Операцію розширення списку.

        Метод приймає інший список та додає до поточного списку усі елементи останнього.
        При цьому подальші зміни в другий список не повинні впливати на перший.
        '''
        for i in range(elements.length()):
            self.append(elements.get(i))

    def delete(self, index: int) -> char:
        '''Операцію видалення елементу зі списку на вказаній позиції.

        Метод повинен повертати значення того елементу, який видаляється.
        Нумерація елементів списку починається з 0.
        У випадку передачі некоректного значення позиції (наприклад, від’ємне число, або число, більше за індекс
        останнього елементу списку) метод повинен генерувати виключну ситуацію
        '''
        if index < 0 or index >= self.length():
            raise IndexError()

        assert self._tail

        node_to_delete = self._get_node(index)
        node_to_delete_prev = self._get_node(index-1) if index != 0 else None

        if node_to_delete is self._head:
            self._head = node_to_delete.next
            self._tail.next = self._head
        elif node_to_delete is self._tail:
            assert node_to_delete_prev
            node_to_delete_prev.next = self._head
            self._tail = node_to_delete_prev
        else:
            assert node_to_delete_prev
            node_to_delete_prev.next = node_to_delete.next

        self._length -= 1

        return node_to_delete.value

    def delete_all(self, element: char) -> None:
        '''Операцію видалення елементів зі списку за значенням.

        Метод видаляє зі списку усі елементи, які за значенням відповідають шуканому.
        У випадку передачі елемента, який у списку відсутній, жодні зміни до списку не застосовуються.
        '''
        check_char(element)

        cur_node = self._head
        cur_node_i = 0
        while True:
            assert cur_node

            if cur_node.value == element:
                self.delete(cur_node_i)
                cur_node_i -= 1

            cur_node = cur_node.next
            cur_node_i += 1
            if cur_node is self._head:
                break

    def clone(self) -> "List":
        '''Операція копіювання списку.

        При виклику повинен створити копію поточного списку та повернути її.
        '''
        clone = List()
        for i in range(self.length()):
            clone.append(self.get(i))

        return clone

    def reverse(self) -> None:
        '''Операція обернення списку.

        Метод повинен змінити порядок елементів у поточному списку задом наперед.
        Елемент, що був останнім стане першим, передостаннім — другим, … а перший — останнім.
        '''
        if not self._head or not self._head.next:
            return

        prev_node = None
        cur_node = self._head
        first_node = self._head

        while True:
            assert cur_node

            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

            if cur_node == first_node:
                break

        first_node.next = prev_node
        self._head = prev_node

    def find_first(self, element: char) -> int:
        '''Операція пошуку елемента за значенням з голови списку.

        Метод повинен знайти перший елемент у списку, що дорівнює шуканому та повернути його позицію.
        Нумерація елементів списку починається з 0.
        У випадку відсутності шуканого елемента у списку, метод повертає -1
        '''
        check_char(element)

        for i in range(self.length()):
            if self.get(i) == element:
                return i

        return -1

    def find_last(self, element: char) -> int:
        '''Операція пошуку елемента за значенням з хвоста списку.

        Метод повинен знайти останній елемент у списку, що дорівнює шуканому та повернути його позицію.
        Нумерація елементів списку починається з 0.
        У випадку відсутності шуканого елемента у списку, метод повертає -1.
        '''
        check_char(element)

        last_index = -1
        for i in range(self.length()):
            if self.get(i) == element:
                last_index = i

        return last_index

    def clear(self) -> None:
        '''Операцію очищення списку.

        Метод видаляє усі елементи списку.
        '''
        self._head = None
        self._tail = None
        self._length = 0
