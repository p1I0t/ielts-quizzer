import random 
import json
with open('words.json', 'r', encoding='utf-8') as f:
     words_to_learn = json.load(f)
N = 5
words_to_ask = random.sample(list(words_to_learn.keys()),N)
correct_on_first_try = 0
for current_word in words_to_ask:
     print(f"Какой перевод у слова: {current_word}?")
     correct_answer = words_to_learn[current_word]
     attempts = 0
     max_attempts = 3
     while attempts < max_attempts:
          user_input = input(f"Попытка {attempts + 1}. Введите правильный ответ: ")
          if user_input == correct_answer:
               print("Правильно!")
               if attempts == 0:
                    correct_on_first_try += 1
               break
          else:
              attempts += 1
              print(f"Неверно. Осталось попыток: {max_attempts - attempts}")
              if attempts == max_attempts:
                  print("Вы исчерпали все попытки.")
print("\n" + "="*30)
print(f"Тренировка окончена.")
print(f"Ваш результат: {correct_on_first_try} из {N} слов введено правильно с первой попытки.")
print("="*30)