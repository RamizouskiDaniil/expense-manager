expenses = []

def add_expense(expenses):
    expense = {}
    expense["category"] = input('Введите категорию расхода ')
    expense["amount"] = int(input('Введите сумму расхода '))
    expenses.append(expense)

def show_expenses(expenses):

    if expenses:

        for index, expense in enumerate(expenses):
            print(f'{index} Категория: {expense["category"]} Сумма: {expense["amount"]}')

    else:
        print('Расходов пока нету')

def total_expenses(expenses):
    total = 0

    if expenses:
        for expense in expenses:
            total += expense["amount"]

    return total

def biggest_expense(expenses):
    max_amount = float('-inf')

    if expenses:

        for index, expense in enumerate(expenses):
            if expense["amount"] > max_amount:
                max_amount = expense["amount"]
                biggest_number = index

        return expenses[biggest_number]

    else:
        print('Расходов пока нету ')

def lowest_expense(expenses):
    min_amount = float('inf')

    if expenses:

        for index, expense in enumerate(expenses):
            if expense["amount"] < min_amount:
                min_amount = expense["amount"]
                lowest_number = index

        return expenses[lowest_number]
    else:
        print('Расходов пока нету ')

def search_category(expenses):
    found_indexes = []
    category = input('Введите категорию которую хотите найти: ')

    for index, expense in enumerate(expenses):
        if expense["category"] == category:
            found_indexes.append(index)

    return found_indexes

def delete_expense(expenses):
    found_indexes = search_category(expenses)

    if found_indexes:
        print("Найденные расходы:")
        for i in found_indexes:
            exp = expenses[i]
            print(f"{i}. {exp['category']} - {exp['amount']}")

        choose_index = int(input('Введите индекс расхода, который хотите удалить: '))

        if choose_index in found_indexes:
            del expenses[choose_index]
        else:
            print("Неверный индекс")
    else:
        print('Категорий не найдено')

def change_expense(expenses):
    found_indexes = search_category(expenses)

    if found_indexes:
        print("Найденные расходы:")
        for i in found_indexes:
            exp = expenses[i]
            print(f"{i}. {exp['category']} - {exp['amount']}")

        choose_index = int(input('Введите индекс расхода, который хотите изменить: '))

        if choose_index in found_indexes:
            choose_change = int(input('1. Категория; 2. Сумма; 3. Оба поля: '))

            if choose_change == 1:
                expenses[choose_index]["category"] = input('Введите новую категорию: ')
            elif choose_change == 2:
                expenses[choose_index]["amount"] = int(input('Введите новую сумму: '))
            elif choose_change == 3:
                expenses[choose_index]["category"] = input('Введите новую категорию: ')
                expenses[choose_index]["amount"] = int(input('Введите новую сумму: '))
        else:
            print("Неверный индекс")
    else:
        print('Расходы не найдены')

def statistics(expenses):
    if expenses:
        print(f'Количество расходов - {len(expenses)}')
        total = total_expenses(expenses)
        print(f'Общий расход - {total}')
        print(f'Средний расход - {total/len(expenses)}')
        biggest_expense(expenses)
        lowest_expense(expenses)
    else:
        print('Расходов нету ')

def menu():
    print('Выберите что нужно сделать: ')
    print('1. Добавить расход')
    print('2. Показать все расходы')
    print('3. Показать общую сумму расходов')
    print('4. Найти самый большой расход')
    print('5. Найти самый маленький расход')
    print('6. Найти расходы по категории')
    print('7. Удалить расход')
    print('8. Изменить расход')
    print('9. Вывести общую статистику')
    print('10. Выйти из программы')

def main():
    while True:
        menu()
        choice = int(input())
        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            show_expenses(expenses)
        elif choice == 3:
            print(f'Общая сумма расходов - {total_expenses(expenses)}')
        elif choice == 4:
            print(f'Наибольший расход - {biggest_expense(expenses)}')
        elif choice == 5:
            print(f'Наименьший расход - {lowest_expense(expenses)}')
        elif choice == 6:
            search_category(expenses)
        elif choice == 7:
            delete_expense(expenses)
        elif choice == 8:
            change_expense(expenses)
        elif choice == 9:
            statistics(expenses)
        elif choice == 10:
            break
        else:
            print(f'Такого пункта не существует')



