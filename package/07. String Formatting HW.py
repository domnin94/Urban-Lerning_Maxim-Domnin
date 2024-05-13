
team1_num = 5
print('В команде Мастера кода участников: %s !' % (team1_num))

team2_num = 6
team3_num = 7
print('Итого сегодня в командах участников: %s и %s !' % (team2_num, team3_num))



score_2 = 42
print('Команда Волшебники данных решила задач: {} !'.format(score_2))

team1_time = 18015.2
print('Волшебники данных решили задачи за {} с !'.format(team1_time))



score1 = 40
score2 = 42
print(f'Команды решили {score1} и {score2} задач.')

challenge_result_1 = 'Победа команды Мастера кода!'
challenge_result_2 = 'Победа команды ВолшебникиДанных!'
score_1 = 23
score_2 = 26
team1_time = 56
team2_time = 54
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = challenge_result_1
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = challenge_result_2
else:
    result = 'Ничья!'
print(result)


tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg}с на задачу!')