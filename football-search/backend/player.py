import pandas as pd
from api import make_request

def search_player(name):
    params = {"search": name}
    return make_request("players/profiles", params)

def search_player_seasons(player_id):
    params = {"player": player_id}
    return make_request("players/seasons", params)

def choose_player(players):
    if not players:
        print("Гравців не знайдено.")
        return None
    print("\nЗнайдено гравців:")

    player_data = []
    for idx, player in enumerate(players, start=1):
        info = player["player"]
        name = info["name"]
        age = info.get("age", "Невідомо")
        nationality = info.get("nationality", "Невідомо")
        team = "Без команди"  
        player_data.append([idx, name, age, nationality, team])

    df = pd.DataFrame(player_data, columns=["№", "Ім'я", "Вік", "Національність", "Команда"])
    print(df)
    while True:
        try:
            choice = int(input("Виберіть номер гравця: "))
            if 1 <= choice <= len(players):
                return players[choice - 1]
            else:
                print("Некоректний номер.")
        except ValueError:
            print("Введіть число.")

def show_player_details(player):
    info = player["player"]
    
    print("\n=== Детальна інформація про гравця ===")
    print(f"Ім'я: {info['name']}")
    print(f"Повне ім'я: {info.get('firstname', 'Невідомо')} {info.get('lastname', '')}")
    print(f"Вік: {info.get('age', 'Невідомо')}")
    print(f"Національність: {info.get('nationality', 'Невідомо')}")
    print(f"Дата народження: {info.get('birth', {}).get('date', 'Невідомо')}")
    print(f"Країна народження: {info.get('birth', {}).get('country', 'Невідомо')}")
    print(f"Зріст: {info.get('height', 'Невідомо')}")
    print(f"Вага: {info.get('weight', 'Невідомо')}")
    print(f"Позиція: {info.get('position', 'Невідомо')}")
    print(f"Фото: {info.get('photo', 'Немає')}")

    player_id = info["id"]
    stats_response = get_player_statistics(player_id)
    if stats_response and stats_response.get("response"):
        stats = stats_response["response"][0]
        print("\n=== Статистика ===")
        print(f"Команда: {stats['team']['name']}")
        print(f"Ліга: {stats['league']['name']}")
        print(f"Позиція: {stats['games']['position']}")
        print(f"Ігри: {stats['games']['appearances']}")  
        print(f"Голи: {stats['goals']['total']}")
        print(f"Асисти: {stats['goals']['assists'] or 0}")
    else:
        print("\nСтатистика не доступна для цього гравця.")

def get_player_statistics(player_id):
    params = {"player": player_id, "season": 2023}
    return make_request("players", params)