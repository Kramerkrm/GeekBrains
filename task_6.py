while True:
    day = 1
    start_km = float(input('Результат первого дня: '))
    final_km = float(input('Ваш желаемый результат: '))
    if start_km <= 0 or final_km < 0:
        print('Результат должен быть больше нуля')
    else:
        while start_km < final_km:
            start_km += start_km * 0.1
            day += 1

        print(f'Вы добьетесь резульатат за {day} дней!')
        break