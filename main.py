import csv
import tabulate
import random

with open('books-en.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    tablereader = list(table)
    tablereader.pop(0)
    # Question 1, подсчитать количество записей в csv file
    NumberOfEntries = len(tablereader)
    print(f'1. количество записей  {NumberOfEntries}')

    # Question 2,Выдать количество записей, у которых в поле Название строка длиннее 30 символов.
    NamesLongerThan30 = 0
    for row in tablereader:
        if len(row[2]) > 30:
            NamesLongerThan30 += 1
    print(f'2. количество записей, у которых в поле Название строка длиннее 30 символов равно'
          f' {NamesLongerThan30}')

    # Question 3, Реализовать поиск книг по автору с ценами от 150 рублей
    Authors = [row[2] for row in tablereader]

    def bookSearch(author):
        BookList = [['название', 'цена']]
        if author in Authors:
            for row in tablereader:
                if ',' in row[6]:
                    row[6] = row[6].replace(',', '.')
                if row[2] == author and float(row[6]) >= 150:
                    BookList.append([row[1], row[6]])
            if len(BookList) != 0:
                BookTable = tabulate.tabulate(BookList, tablefmt='psql')
                print(f'3. книги, написанные этим автором {author}\n{BookTable}')
            else:
                print(f'У этого автора нет книг стоимостью от 150 рублей')
        else:
            print(f'этого автора не существует')

    authorName = input('3. введите имя автора: ')
    bookSearch(authorName)


    #Question 4
    random_files = []
    for i in range(20):
        random_files.append(tablereader[random.randint(0, NumberOfEntries)])
    print(f'20 randomly Selected entries\n{tabulate.tabulate(random_files)}')

    with open('Библиографическая Таблица.txt', 'w') as file:
        file.write(tabulate.tabulate(random_files))









