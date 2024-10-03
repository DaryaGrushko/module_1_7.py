#Практическое задание по теме: "Словари и множества"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print('-------Дано-------')
print('Список оценок всех учеников', grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print('Множество имен всех учеников', students)

print('-------Задание-------')
print('Вычислить средний бал каждого ученика')

print('-------Решение-------')
students = list(students)
print('Преобразуем множество имен всех учеников в список', students)
students_sort=sorted(students)
print('Сортируем список учеников в алфавитном порядке', students_sort)
print('Вычисляем средний бал и по ключу имени записываем в словарь')
zhurnal = {}
for i in range(0, len(students)):
   zhurnal[students_sort[i]] = sum(grades[i])/len(grades[i])
   print ('Шаг - ', i, ', журнал ', zhurnal)

print ('\nСредний балл ученикоа', zhurnal)
