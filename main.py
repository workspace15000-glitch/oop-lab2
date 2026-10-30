from regex_checker import FloatValidator


def main() -> None:
    validator = FloatValidator()
    print("=== Проверка и поиск чисел с плавающей запятой ===")
    print("Примеры: -3.14, .5, 5., 1e-3. Десятичный разделитель — точка.")

    while True:
        print("\n1 Проверить число | 2 Поиск в тексте | 3 Поиск в файле | 0 Выход")
        try:
            choice = input("Выбор: ").strip()
            if choice == "0":
                return
            if choice == "1":
                value = input("Введите число: ").strip()
                if validator.is_valid(value):
                    print("Корректное число с плавающей запятой")
                else:
                    print("Некорректная запись числа")
            elif choice == "2":
                text = input("Введите текст: ")
                found = validator.validate_text(text)
                print("Найденные числа:", ", ".join(found) if found else "нет")
            elif choice == "3":
                filepath = input("Путь к файлу UTF-8: ").strip()
                found = validator.validate_file(filepath)
                print("Найденные числа:", ", ".join(found) if found else "нет")
            else:
                print("Нет такого пункта меню")
        except (OSError, UnicodeError) as error:
            print(f"Ошибка чтения файла: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nВыход.")
            return


if __name__ == "__main__":
    main()
