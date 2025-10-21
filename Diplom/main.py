from Diplom.PeopleDatabase import People
from Diplom.Person import Person


def main():
    db = People()

    while True:
        print("\n=== МЕНЮ ===")
        print("1. Додати людину")
        print("2. Пошук людини")
        print("3. Зберегти у файл")
        print("4. Завантажити з файлу")
        print("0. Вихід")
        print("=" * 13)

        choice = input("Зробить ваш вибір: ")

        if choice == "1":
            try:
                first_name = input("Ім'я: ")
                middle_name = input("Прізвище (необов'язково, для пропуску нажати Enter): ")
                last_name = input("По-батькові (необов'язково, для пропуску нажати Enter): ")
                birth_date = input("Дата народження: ")
                death_date = input("Дата смерті (необов'язково, для пропуску нажати Enter): ")
                gender = input("Стать (ч/ж): ")

                person = Person(first_name, middle_name, last_name, birth_date, death_date, gender)
                db.add_person(person)
                print("Людину додано успішно!")
            except Exception as e:
                print(f"Помилка: {e}")

        elif choice == "2":
            request = input("Введіть текст для пошуку: ")
            result = db.find_person(request)
            if result:
                for person in result:
                    print(person)
            else:
                print("Нічого не знайдено.")

        elif choice == "3":
            filename = input("Вкажіть назву файлу (наприклад data.json): ")
            db.save_person(filename)
            print("Дані збережено.")

        elif choice == "4":
            filename = input("Вкажіть назву файлу (наприклад data.json): ")
            db.load_person(filename)

        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main()
