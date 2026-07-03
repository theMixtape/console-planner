import json

file = 'planner.json'

def load_data():
    data = {}
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print("Файл не знайдено.")

    return data

def save_data(data):
    try:
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Помилка при збереженні даних: {e}")

def add(data):
    title = input(" Назва події ➜  ")
    date = input(" Дата події (YYYY-MM-DD) ➜  ")
    time = input(" Час події (HH:MM) ➜  ")
    desc = input(" Опис ➜  ")


    if data:
        next_id = str(max(int(k) for k in data.keys()) + 1)
    else:
        next_id = "1"

    data[next_id] = {
        "title": title,
        "date": date,
        "time": time,
        "description": desc
    }

    save_data(data)
    print(" ──────────────────────────────")
    print(" [!] Подію успішно додано.")
    print(" ──────────────────────────────")

def all(data):
    if not data:
        print("Подій немає.")
        return
    
    for eid, info in data.items():
        print(f" ID ➜ {eid}")
        print(f" Назва ➜ {info['title']}")
        print(f" Дата ➜ {info['date']}")
        print(f" Час ➜ {info['time']}")
        print(f" Опис ➜ {info['description']}")
        print(" ──────────────────────────────")
        input("\nНатисніть Enter, щоб продовжити.")
    
def delete(data):
    if not data:
        print("Подій немає.")
        return
    while True:
        eid = input("Введіть ID події для видалення ➜  ")

        if eid in data:
            break
        else:
            print(" [!] Такого ID не існує. Спробуйте ще раз.")
            print(" ──────────────────────────────")


    conf = input(f"Ви впевнені що хочете видалити подію N{eid} (так/ні) ➜ ")

    if conf == "так":
        try:
            if eid in data:
                del data[eid]
                save_data(data)
                print(" ──────────────────────────────")
                print(" [!] Подію успішно видалено.")
            else:
                print(" ──────────────────────────────")
                print(" [!] Подію не знайдено")
        except Exception as e:
            print(f"Виникла помилка! {e}")
    else:
        print(" [!] Видалення скасовано.")

ev = load_data()

while True:
    print("╭────────────────────────────────╮")
    print("│    Персональний планувальник   │")
    print("╰────────────────────────────────╯")
    print(" ────────────────────────────────")
    print("  [1] ➜  Додати подію")
    print("  [2] ➜  Переглянути всі події")
    print("  [3] ➜  Видалити подію")
    print("  [4] ➜  Вийти")
    print(" ────────────────────────────────")
    
    choice = input(" Виберіть пункт меню ➜  ")

    if choice == "1":
        print("\n ╭──────────────────────────────╮")
        print(" │       Нова подія             │")
        print(" ╰──────────────────────────────╯")
        add(ev)
        
    elif choice == "2":
        print("\n ╭──────────────────────────────╮")
        print(" │       Всі ваші події         │")
        print(" ╰──────────────────────────────╯")
        all(ev)
        
    elif choice == "3":
        print("\n ╭──────────────────────────────╮")
        print(" │       Видалення події        │")
        print(" ╰──────────────────────────────╯")
        delete(ev)
        
    elif choice == "4":
        print("\n ╭──────────────────────────────╮")
        print(" │  Програма завершує роботу.   │")
        print(" ╰──────────────────────────────╯")
        break
        
    else:
        print("\n [!] Некоректний вибір.")