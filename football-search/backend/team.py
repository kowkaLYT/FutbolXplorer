import pandas as pd
from api import make_request


def search_team(name):
    params = {"search": name}
    return make_request("teams", params)


def choose_team(teams):
    if not teams:
        print("Команд не знайдено.")
        return None
    print("\nЗнайдено команди:")

    team_data = []
    for idx, team in enumerate(teams, start=1):
        name = team["team"]["name"]
        country = team["team"]["country"]
        city = team.get("venue", {}).get("city", "Невідомо")
        team_data.append([idx, name, country, city])

    df = pd.DataFrame(team_data, columns=["№", "Назва", "Країна", "Місто"])
    print(df)
    while True:
        try:
            choice = int(input("Виберіть номер команди: "))
            if 1 <= choice <= len(teams):
                return teams[choice - 1]
            else:
                print("Некоректний номер.")
        except ValueError:
            print("Введіть число.")


def show_team_details(team):
    info = team["team"]
    venue = team.get("venue", {})

    print("\n=== Детальна інформація про команду ===")
    print(f"Назва: {info['name']}")
    print(f"Код: {info.get('code', 'Невідомо')}")
    print(f"Країна: {info['country']}")
    print(f"Місто: {venue.get('city', 'Невідомо')}")
    print(f"Рік заснування: {info.get('founded', 'Невідомо')}")
    print(f"Стадіон: {venue.get('name', 'Невідомо')}")
    print(f"Місткість: {venue.get('capacity', 'Невідомо')}")
    print(f"Покриття: {venue.get('surface', 'Невідомо')}")
    print(f"Логотип: {info['logo']}")