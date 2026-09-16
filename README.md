graph TD
    A["📦 DevOps_Lab1<br/>Python Package v0.1.0"] --> B["🗂️ Структура проекту"]
    
    B --> C["📄 src/devops_lab1/"]
    
    C --> D["__init__.py<br/>main function"]
    C --> E["lib.py<br/>Математичні функції"]
    C --> F["main.py<br/>Точка входу"]
    
    D --> D1["main(): None<br/>Print greeting"]
    
    E --> E1["add(a, b)<br/>Сума чисел"]
    E --> E2["subtract(a, b)<br/>Різниця чисел"]
    E --> E3["multiply(a, b)<br/>Добуток чисел"]
    
    F --> F1["Імпорт функцій<br/>з lib.py"]
    F --> F2["main()<br/>Демонстрація функцій"]
    
    F1 --> F3["add, subtract,<br/>multiply"]
    
    F2 --> F4["Параметри: a=10, b=5"]
    F4 --> F5["Виведення результатів:<br/>print додавання<br/>print віднімання<br/>print множення"]
    
    F5 --> G["📊 Вихід<br/>Додавання: 15<br/>Віднімання: 5<br/>Множення: 50"]
    
    style A fill:#4A90E2,color:#fff
    style G fill:#7ED321,color:#fff
    style E fill:#F5A623,color:#fff
    style F2 fill:#BD10E0,color:#fff
