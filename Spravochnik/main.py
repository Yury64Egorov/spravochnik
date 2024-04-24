class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, last_name, first_name, phone_number, city, middle_name=None):
        contact = {
            'Фамилия': last_name,
            'Имя': first_name,
            'Отчество': middle_name,
            'Номер телефона': phone_number,
            'Город': city
        }
        self.contacts.append(contact)
        print("Контакт успешно добавлен.")

    def edit_contact(self, index, field, new_value):
        if index < len(self.contacts):
            self.contacts[index][field] = new_value
            print("Контакт успешно отредактирован.")
        else:
            print("Контакта с таким индексом не существует.")

    def view_contacts(self):
        if self.contacts:
            for index, contact in enumerate(self.contacts):
                print(f"Контакт {index + 1}:")
                for key, value in contact.items():
                    print(f"{key}: {value}")
                print()
        else:
            print("Телефонная книга пуста.")

    def delete_contact(self, index):
        if index < len(self.contacts):
            del self.contacts[index]
            print("Контакт успешно удален.")
        else:
            print("Контакта с таким индексом не существует.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for contact in self.contacts:
                for key, value in contact.items():
                    file.write(f"{key}: {value}\n")
                file.write('\n')
        print("Контакты успешно сохранены в файле.")

def main():
    phonebook = Phonebook()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить контакт")
        print("2. Редактировать контакт")
        print("3. Просмотреть контакты")
        print("4. Удалить контакт")
        print("5. Сохранить контакты в файл")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество (необязательно): ")
            phone_number = input("Введите номер телефона: ")
            city = input("Введите город: ")
            phonebook.add_contact(last_name, first_name, phone_number, city, middle_name)

        elif choice == '2':
            index = int(input("Введите индекс контакта для редактирования: "))
            field = input("Введите поле для редактирования: ")
            new_value = input("Введите новое значение: ")
            phonebook.edit_contact(index - 1, field, new_value)

        elif choice == '3':
            phonebook.view_contacts()

        elif choice == '4':
            index = int(input("Введите индекс контакта для удаления: "))
            phonebook.delete_contact(index - 1)

        elif choice == '5':
            filename = input("Введите название файла для сохранения (с расширением .txt): ")
            phonebook.save_to_file(filename)

        elif choice == '6':
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
