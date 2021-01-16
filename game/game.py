number = 23

running = True

while running:
    guess = int(input('Введите целое число Welcome: '))

    if guess == number:
        print('Поздравляю вы угадали, хотя и не выиграли не какого приза:')
        running = False # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Тебе сопутствует удача')
    # Здесь можете выполнить всё что вам ещё нужно

print('Это было сильно, The END:')