# #1
# def calculate(number_1, operation, number_2):
#     if operation == '+':
#         return number_1 + number_2
#     elif operation == '-':
#         return number_1 - number_2
#     elif operation == '*':
#         return number_1 * number_2
#     elif operation == '/':
#         if number_2 != 0:
#             return number_1 / number_2
#         else:
#             return "Помилка: ділення на нуль!"
#     else:
#         return "Невідома операція!"
#
#
# num_1 = float(input('Enter a number: '))
# oprtn = input('Enter an operation (+, -, *, /): ')
# num_2 = float(input('Enter another number: '))
#
# result = calculate(num_1, oprtn, num_2)
# print("Result:", result)
#2
# def is_palindrome(word: str) -> bool:
#     if word == word[::-1]:
#         return True
#     else:
#         return False
#
# w = input('Enter a word: ')
#
# print(is_palindrome(w))
#3
# def tags_html(input_text):
#     [tag, text] = input_text.split(' ', 1)
#
#     opening_tags = ["html", "head", "title", "style", "script", "body", "section", "nav", "article",
#                     "aside", "h1", "h2", "h3", "h4", "h5", "h6", "header", "footer", "address",
#                     "main", "p", "pre", "blockquote", "ol", "ul", "li", "dl", "dt", "dd",
#                     "figure", "figcaption", "div", "a", "em", "strong", "small", "s", "cite", "q",
#                     "dfn", "abbr", "ruby", "rt", "rp", "data", "time", "code", "var", "samp",
#                     "kbd", "sub", "sup", "i", "b", "u", "mark", "span", "ins", "del", "video",
#                     "audio", "map", "table", "caption", "colgroup", "tbody", "thead", "tfoot", "tr",
#                     "td", "th", "form", "fieldset", "legend", "label", "button", "select", "optgroup",
#                     "option", "textarea", "output", "progress", "meter", "details", "summary", "dialog",
#                     "template", "canvas", "slot"]
#
#     if tag.lower() in opening_tags:
#         return f"<{tag}>{text}</{tag}>"
#     else:
#         return text
#
#
# t = input('Enter a text: ')
#
# print(tags_html(t))
#4
# import math
#
# def num_is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# num = int(input('Введіть число: '))
#
# print(num_is_prime(num))
#5
def count_vowels_consonants(text):
    vowels = "aeiouAEIOUаеєиіїоуюяАЕЄИІЇОУЮЯ"
    count_vowels = 0
    count_consonants = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                count_vowels += 1
            else:
                count_consonants += 1

    return count_vowels, count_consonants


t = input("Введіть текст: ")

vowels, consonants = count_vowels_consonants(t)
print("Голосних:", vowels)
print("Приголосних:", consonants)




