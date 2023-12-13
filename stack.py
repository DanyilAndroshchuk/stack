"""
1 Валідні дужки

Дано рядок s, який містить лише символи '(', ')', '{', '}','[', ']', визначити, чи введений рядок дійсний.
Рядок введення дійсний, якщо:
- Відкриті дужки повинні бути закриті
однотипними дужками.
- Відкриті дужки повинні бути закриті в
правильному порядку.
- Кожна закрита дужка має відповідну відкриту дужку такого ж типу.
Приклад 1:
Input: s = "()" Output: true
Приклад 2:
Input: s = "()[]{}" Output: true
Приклад 3:
Input: s = "(]" Output: false
Обмеження:
1<= s.length <= 10 000
s consists of parentheses only '()[]{}'
"""


def is_valid(s):
    if not (1 <= len(s) <= 10000):
        return False

    stack = []
    brackets_dict = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets_dict.values():
            stack.append(char)
        elif char in brackets_dict.keys():
            if not stack or stack.pop() != brackets_dict[char]:
                return False
        else:
            return False

    return not stack


# ex1 = "()"
# ex2 = "()[]{}"
# ex3 = "(()"
#
# print(is_valid(ex1))
# print(is_valid(ex2))
# print(is_valid(ex3))

# ______________________________________________________________________________________________________________________

"""
2 Обхід бінарного дерева в порядку (Inorder Traversal)

Враховуючи root бінарного дерева, поверніть упорядкований обхід (Inorder Traversal) значень його вузлів.
Приклад 1:
(1)->(2)->(3)

Input: root = [1, null,2,3] Output: [1,3,2]
Приклад 2:
Input: root = [] Output: []
Приклад 3:
Input: root = [1] Output: [1]
Обмеження:
Кількість вузлів у дереві знаходиться в діапазоні [0, 100].
-100 <= Node.val <= 100
"""


class TreeNode:
    # Конструктор класу TreeNode для створення вузла бінарного дерева.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(nodes):
    # Функція для побудови бінарного дерева зі списку вузлів.
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    current_index = 1

    while current_index < len(nodes):
        current_node = queue.pop(0)

        if nodes[current_index] is not None:
            current_node.left = TreeNode(nodes[current_index])
            queue.append(current_node.left)

        current_index += 1

        if current_index < len(nodes) and nodes[current_index] is not None:
            current_node.right = TreeNode(nodes[current_index])
            queue.append(current_node.right)

        current_index += 1

    return root


def inorder_traversal(root):
    # Функція для виконання упорядкованого обходу бінарного дерева в порядку Inorder.
    def inorder_recursive(node, result):
        if node:
            inorder_recursive(node.left, result)
            result.append(node.val)
            inorder_recursive(node.right, result)

    result = []
    inorder_recursive(root, result)
    return result


# Тестимо:
# s1 = [1, None, 2, 3]
# s2 = []
# s3 = [1]
#
# print(inorder_traversal(build_tree_from_list(s1)))
# print(inorder_traversal(build_tree_from_list(s2)))
# print(inorder_traversal(build_tree_from_list(s3)))

# ______________________________________________________________________________________________________________________
"""
3 Мінімальний стек

Створіть стек, який підтримує надсилання, висунення, початок і отримання мінімального елемента в постійному часі.
Реалізуйте клас MinStack:
MinStack() ініціалізує обʼєкт стека.
void push(int val) переміщує елемент val у стек.
void pop() видаляє елемент у верхній частині стека.
int top() отримує верхній елемент стека.
int getMin() отримує мінімальний елемент у стеку.
Ви повинні реалізувати рішення з 0(1) часовою складністю для кожної функції.

Приклад:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"] [[],[-2],[0],[-3],[],[],[],[]] 
Output
[null,null,null,null,-3,null,0,-2]
Пояснення:
MinStack minStack = new MinStack();
minStack.push(-2); 
minStack.push(0);
minStack.push(-3); 
minStack.getMin(); //
return -3 minStack.pop(); minStack.top(); // 
return 0 minStack.getMin(); // 
return -2

Обмеження:
• Методи pop, top i getMin операцій будуть завжди викликані в не пустому стеку
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            popped_val = self.stack.pop()
            if popped_val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]


def min_stack(operations, operands):
    min_st = None
    output = []

    for operation, value in zip(operations, operands):
        if operation == "MinStack":
            min_st = MinStack()
            output.append(None)
        elif operation == "push":
            min_st.push(value[0])
            output.append(None)
        elif operation == "pop":
            if min_st.stack:
                min_st.pop()
            output.append(None)
        elif operation == "top":
            if min_st.stack:
                output.append(min_st.top())
            else:
                output.append(None)
        elif operation == "getMin":
            if min_st.min_stack:
                output.append(min_st.get_min())
            else:
                output.append(None)

    return output


# Тестимо:
# stack_operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
# stack_operands = [[], [-2], [0], [-3], [], [], [], []]
#
# print(min_stack(stack_operations, stack_operands))

# ______________________________________________________________________________________________________________________

"""
4 Реалізуйте чергу використовуючи стеки

Реалізуйте чергу FIFO, використовуючи лише два стеки. Реалізована черга повинна підтримувати всі функції звичайної 
черги (push, peek, pop і empty).

Реалізуйте клас MyQueue:

void push(int x) Переміщує елемент x у кінець черги.
int pop() Вилучає елемент з початку черги та повертає його.
int peek() Повертає елемент на початку черги.
boolean empty() Повертає true, якщо черга порожня, і false в іншому випадку.

Помітки:
Ви повинні використовувати лише стандартні операції стека, що означає, що дійсними є лише операції push to top, peek/pop 
from top, size та i empty.
Залежно від вашої мови, стек може не підтримуватися нативно. Ви можете імітувати стек, використовуючи список або чергу 
(черга з двома кінцями), якщо ви використовуєте лише стандартні операції стека.

Приклад:
Input["MyQueue", "push", "push", "peek", "pop", "empty"] [[], [1], [2], [], [], []]
Output[null, null, null, 1, 1, false]

Пояснення:
MyQueue myQueue = new MyQueue(); myQueue.push(1); // queue is: [1] myQueue.push(2); // queue is: [1, 2] (leftmost is 
front of the queue) myQueue.peek(); // return 1 myQueue.pop(); // return 1, queue is [2] myQueue.empty(); // 
return false

Обмеження:
1 <= x <= 9
Максимально 100 викликів буде зроблено на push, pop, peek, іs_empty.
Всі виклики на pop і peek є дійсними.
"""


class MyQueue:
    def __init__(self):
        # Ініціалізація об'єкта черги.
        self.stack_push = []
        self.stack_pop = []

    def push(self, x):
        # Переміщення елемента x у кінець черги.
        if 1 <= x <= 9 and len(self.stack_push) < 100:
            self.stack_push.append(x)
        else:
            raise ValueError("Invalid input for push operation")

    def pop(self):
        # Вилучення елемента з початку черги та повернення його
        self.ensure_pop_stack_has_elements()
        if self.stack_pop:
            return self.stack_pop.pop(0)
        else:
            raise ValueError("Queue is empty")

    def peek(self):
        # Повертає елемент на початку черги.
        self.ensure_pop_stack_has_elements()
        if self.stack_pop:
            return self.stack_pop[0]
        else:
            raise ValueError("Queue is empty")

    def empty(self):
        # Повертає True, якщо черга порожня, і False в іншому випадку
        return not self.stack_push and not self.stack_pop

    def ensure_pop_stack_has_elements(self):
        # Переміщення елементів з основного стеку в допоміжний стек, якщо допоміжний стек порожній.
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.insert(0, self.stack_push.pop())


def my_queue(operations, operands):
    m_queue = None
    output = []

    for key, value in zip(operations, operands):
        if key == "MyQueue":
            m_queue = MyQueue()
            output.append(None)
        elif key == "push":
            m_queue.push(value[0])
            output.append(None)
        elif key == "pop":
            output.append(m_queue.pop())
        elif key == "peek":
            output.append(m_queue.peek())
        elif key == "empty":
            output.append(m_queue.empty())

    return output


# Тестимо:
# queue_operations = ["MyQueue", "push", "push", "peek", "pop", "empty"]
# queue_operands = [[], [1], [2], [], [], []]
#
# print(my_queue(queue_operations, queue_operands))

# ______________________________________________________________________________________________________________________

"""
5 Декодувати рядок

Дано закодований рядок, повернути його декодований рядок.

Правило кодування таке: k[encoded_string], де encoded_string у квадратних дужках повторюється рівно k разів. Зверніть увагу, що k гарантовано буде додатним цілим числом.

Ви можете припустити, що вхідний рядок завжди дійсний; немає зайвих пробілів, квадратні дужки правильно сформовані тощо. Крім того, ви можете припустити, що вихідні дані не містять жодних цифр і що цифри призначені лише для тих повторюваних чисел, k. Наприклад, не буде таких вхідних даних, як 3a або 2[4].

Тестові випадки генеруються таким чином, що довжина результату ніколи не перевищуватиме 100 000.

Приклад 1:
Input: s = "3[a]2[bc]" 
Output: "aaabcbc"

Приклад 2:
Input: s = "3[acc]" 
Output: "accaccacc"

Приклад 3:
Input: s = "2[abc]3[cd]ef" 
Output: "abcabccdcdcdef"

Обмеження:
1 <= s.length <= 30
s складається з малих англійських літер, цифр і квадратних дужок '[]'.
s гарантовано є дійсним введенням.
Усі цілі числа в s знаходяться в діапазоні [1, 300].
"""


def decode_s(s):
    stack = []
    current_number = 0
    current_string = ""

    for char in s:
        if not (1 <= len(s) <= 30 and char.isalnum() or char in '[]'):
            raise ValueError("Invalid input")

        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0
        elif char == ']':
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * min(num, 300)
        else:
            current_string += char

    return current_string


# Тестимо
# s1 = "3[a]2[bc]"
# s2 = "3[acc]"
# s3 = "2[abc]3[cd]ef"
# print(decode_s(s1))
# print(decode_s(s2))
# print(decode_s(s3))


# ______________________________________________________________________________________________________________________

"""
6 Оцініть зворотну польську нотацію

Вам надається масив маркерів рядків, який представляє арифметичний вираз у зворотній польській нотації.
Оцініть вираз. Повертає ціле число, яке представляє значення виразу.

Зауважте, що:

Дійсні оператори «+», «-», «*» і «/».
Кожен операнд може бути цілим числом або іншим виразом.
Ділення між двома цілими числами завжди скорочується до нуля.
Ділення на нуль не буде.
Вхідні дані представляють дійсний арифметичний вираз у зворотній полірованій нотації.
Відповідь і всі проміжні обчислення можуть бути представлені у вигляді 32-розрядного цілого числа.

Приклад 1:
Input: tokens = ["2","1","+","3","*"] 
Output: 9 
Пояснення: ((2 + 1) * 3) = 9

Приклад 2:
Input: tokens = ["4","13","5","/","+"] 
Output: 6 
Пояснення: (4 + (13 / 5)) = 6

Приклад 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] 
Output: 22 
Пояснення: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = ((10 * (6 / (12 * -11))) + 17) + 5 = ((10 * (6 / -132)) + 17) + 5 = 
((10 * 0) + 17) + 5 = (0 + 17) + 5 = 17 + 5 = 22

Обмеження:
1 <= tokens.length <= 104
tokens[i] – це або оператор: «+», «-», «*», або «/», або ціле число в діапазоні [-200, 200].
"""


def pol_notice(tokens):
    stack = []
    if 1 <= len(tokens) <= 104:
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                num = int(token)
                if -200 <= num <= 200:
                    stack.append(num)
                else:
                    raise ValueError("Operand out of range [-200, 200]")
            elif token in {'+', '-', '*', '/'}:
                if len(stack) < 2:
                    raise ValueError("Insufficient operands for operator {}".format(token))
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ValueError("Division by zero")
                    result = int(a / b)
                stack.append(result)
            else:
                raise ValueError("Invalid token: {}".format(token))
    else:
        raise ValueError("Invalid token length. Must be from 1 to 104")

    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Invalid expression: Too many operands")


# Тестимо
# tokens1 = ["2", "1", "+", "3", "*"]
# tokens2 = ["4", "13", "5", "/", "+"]
# tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# print(pol_notice(tokens1))  # Виведе: 9
# print(pol_notice(tokens2))  # Виведе: 6
# print(pol_notice(tokens3))  # Виведе: 22

# ______________________________________________________________________________________________________________________

"""
7. Найдовші дійсні дужки

Дано рядок, що містить лише символи "(" і ")", повертає довжину найдовших дійсних (правильно сформованих) дужок підрядок.
Приклад 1:
Input: s = "(()" 
Output: 2 
Пояснення: найдовший дійсні дужки підрядок це "()".
Приклад 2:
Input: s = ")()())" 
Output: 4 
Пояснення: найдовший дійсні дужки підрядок це "()()".
Приклад 3:
Input: s = "" Output: 0
Обмеження:
0<= s.length <= 3 * 104
s[i] це '(' чи ')'.
"""


def longest_valid_brackets(s):
    if len(s) < 0 or len(s) > 3 * 104:
        raise ValueError('Length of input must be from 0 to 3*104')
    if len(s) != 0:
        if '(' not in s or ')' not in s:
            raise ValueError("Input must include only '(' and ')'")
    valid_parentheses = []

    for i in range(len(s)):
        if s[i] == '(' and i < len(s) - 1 and s[i + 1] == ')':
            valid_parentheses.extend([i, i + 1])

    return len(valid_parentheses)


# Тестимо
# s1 = "(()"
# s2 = ")()())"
# s3 = ""
# print(longest_valid_brackets(s1))
# print(longest_valid_brackets(s2))
# print(longest_valid_brackets(s3))


