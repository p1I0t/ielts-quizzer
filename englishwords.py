import random 
words_to_learn = {
    "внедрение": "implementation",
    "масштабируемость": "scalability",
    "универсальность": "versatility",
    "избыточность": "redundancy",
    "эффективность": "efficiency",
    "неоднозначный": "ambiguous",
    "последовательный": "consistent",
    "жизнеспособный": "viable",
    "уязвимость": "vulnerability",
    "поддерживаемый": "maintainable"
}
N = 5
words_to_ask = random.sample(list(words_to_learn.keys()),N)
for current_word in words_to_ask:
     print(f"Какой перевод у слова: {current_word}?")
     correct_answer = words_to_learn[current_word]
     attempts = 0
     max_attempts = 3
     while attempts < max_attempts:
          user_input = input(f"Попытка {attempts + 1}. Введите правильный ответ: ")
          if user_input == correct_answer:
               print("Правильно!")
               break
          else:
              attempts += 1
              print(f"Неверно. Осталось попыток: {max_attempts - attempts}")
              if attempts == max_attempts:
                  print("Вы исчерпали все попытки.")