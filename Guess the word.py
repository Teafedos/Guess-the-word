import time

score = 0


def home_phrase(score):
  phrases = ["Архиватор", "Будапешт", "Бульдозер", "Бобслей",
             "Каракатица", "Пиявка", "Единорог", "Москва",
             "Сушилка", "Корабль", "Атмосфера", "Леонардо ди Каприо",
             "Герцог", "География", "Конструктор", "Губка Боб квадратные штаны"]
  if score <= len(phrases):
    return phrases[score]
  else:
    return "Game end"


def game_in_words(score):
  phrase = home_phrase(score)
  err = 0
  new_word = ""
  for i in phrase:
    if i == " " or i == "!" or i == "?" or i == "." or i == "," or i == "-":
      new_word += i
    else:
      new_word += "*"
  new_word = list(new_word)
  print("".join(new_word))
  x = str(input("Введите букву:\n"))
  while True:
    if x.lower() in phrase or x.upper() in phrase:
      if x.lower() in new_word or x.upper() in new_word:
        print(f"Буква {x} уже есть в слове {''.join(new_word)}")
        x = input("Введите букву")
      else:
        for j in range(len(phrase)):
          if phrase[j] == x.lower() or phrase[j] == x.upper():
            new_word[j] = phrase[j]
        if phrase == "".join(new_word):
          print(f"Вы отгадали, это слово: {phrase}")
          print("1. Дальше\n2. Выход\n")
          y = int(input("Ваш выбор:"))
          if y == 1:
            if home_phrase(score+1) == "Game end":
              return "К сожалению, вы прошли все слова."
            else:
              score += 1
              return game_in_words(score)
          elif y == 2:
            return "Пока пока"
        else:
          print("".join(new_word))
          x = input("Введите букву:")
    else:
      print("Не угадали!")
      err += 1
      if err == 6:
        return "К сожалению, вы проиграли..."
      else:
        print(f"Вы можете ошибиться еще {6-err} раза")
        x = input("Введите букву:")
  

print(game_in_words(score))
time.sleep(120)