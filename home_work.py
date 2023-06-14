# На вход подается строка, все символы находятся в нижнем регистре и без пробелов. Напишите функцию, которая будет возвращать True, если строка является палиндромом и False, если строка палиндромом не является.
#
# Примечание: палиндром — это строка, которая читается одинаково как слева направо, так и справа налево
#
# ^-ЗАДАНИЕ-^


def GetPallindrome(str) -> bool:
        lst = []
        for i in str:
            lst.append(i)

        reversed_lst = []

        for i in reversed(lst):
            reversed_lst.append(i)

        if lst == reversed_lst:
            return True

        else:
            return False
