from devops_lab1.lib import add, subtract, multiply


def main():
    """Демонструє роботу функцій з модуля lib."""

    a = 10
    b = 5

    print("Додавання:", add(a, b))
    print("Віднімання:", subtract(a, b))
    print("Множення:", multiply(a, b))


if __name__ == "__main__":
    main()