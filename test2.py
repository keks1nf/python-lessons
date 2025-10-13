def count_characters(text):
  """
  Підраховує повторювані символи у введеному рядку.

  Args:
    text: Введений рядок.

  Returns:
    Словник, де ключами є символи, а значеннями - їхня кількість.
  """
  char_counts = {}  # Створюємо порожній словник для зберігання підрахунків
  for char in text:
    if char in char_counts:
      char_counts[char] += 1  # Збільшуємо лічильник, якщо символ вже є
    else:
      char_counts[char] = 1  # Додаємо символ у словник з лічильником 1
  return char_counts

# Введені дані
input_string = "the quick brown fox jumps over the lazy dog"

# Викликаємо функцію та виводимо результат
result = count_characters(input_string)
print(result)