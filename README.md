# Знакомство с языком Python (семинары)
Урок 8. Работа с файлами

Реализация телефонного справочника.


## Пример работы программы:
```
Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

1
filename <phonebook.txt>

Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

2
#    |Фамилия             |Имя                 |Телефон             |Описание
-----+--------------------+--------------------+--------------------+--------------------
1    |Иванов              |Иван                |111                 |описание Иванова
2    |Петров              |Петр                |222                 |описание Петрова
3    |Васичкина           |Василиса            |333                 |описание Васичкиной
4    |Питонов             |Антон               |777                 |умеет в Питон
5    |Питонов             |Антон               |777                 |умеет в Питон
6    |Сидроров            |Сидор               |12345               |Товарищ Сидоров

Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

3
lastname Питонов
#    |Фамилия             |Имя                 |Телефон             |Описание
-----+--------------------+--------------------+--------------------+--------------------
1    |Питонов             |Антон               |777                 |умеет в Питон
2    |Питонов             |Антон               |777                 |умеет в Питон

Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

3
lastname Иванов
#    |Фамилия             |Имя                 |Телефон             |Описание
-----+--------------------+--------------------+--------------------+--------------------
1    |Иванов              |Иван                |111                 |описание Иванова

Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

4
number 111
#    |Фамилия             |Имя                 |Телефон             |Описание
-----+--------------------+--------------------+--------------------+--------------------
1    |Иванов              |Иван                |111                 |описание Иванова

Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

4
number 12345
#    |Фамилия             |Имя                 |Телефон             |Описание
-----+--------------------+--------------------+--------------------+--------------------
1    |Сидроров            |Сидор               |12345               |Товарищ Сидоров

Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

5
new data Сидоров,Олег,766,Брат Сидора
данные абонента Сидоров,Олег,766,Брат Сидора добавлены в телефонный справочник


Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

2
#    |Фамилия             |Имя                 |Телефон             |Описание
-----+--------------------+--------------------+--------------------+--------------------
1    |Иванов              |Иван                |111                 |описание Иванова
2    |Петров              |Петр                |222                 |описание Петрова
3    |Васичкина           |Василиса            |333                 |описание Васичкиной
4    |Питонов             |Антон               |777                 |умеет в Питон
5    |Питонов             |Антон               |777                 |умеет в Питон
6    |Сидроров            |Сидор               |12345               |Товарищ Сидоров
7    |Сидоров             |Олег                |766                 |Брат Сидора

Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

8

Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

7
lastname Иванов
данные абонента Иванов удалены из телефонного справочника


Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

2
#    |Фамилия             |Имя                 |Телефон             |Описание
-----+--------------------+--------------------+--------------------+--------------------
1    |Петров              |Петр                |222                 |описание Петрова
2    |Васичкина           |Василиса            |333                 |описание Васичкиной
3    |Питонов             |Антон               |777                 |умеет в Питон
4    |Питонов             |Антон               |777                 |умеет в Питон
5    |Сидроров            |Сидор               |12345               |Товарищ Сидоров
6    |Сидоров             |Олег                |766                 |Брат Сидора

Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

9
Enter row number 6
Enter target filename tmp.txt

Выберите необходимое действие:
 1. Загрузить данные справочника из текстового формата
 2. Отобразить весь справочник
 3. Найти абонента по фамилии
 4. Найти абонента по номеру телефона
 5. Добавить абонента в справочник
 6. Изменить данные абонента в справочнике
 7. Удалить абонента из справочника
 8. Сохранить справочник в текстовом формате
 9. Копировать данные в другой файл
 0. Закончить работу

0
```
