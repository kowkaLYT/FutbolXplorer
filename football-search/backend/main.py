import requests
import pandas as pd

API_KEY = "c4998ba00908904056dca85a90b1b28d"


def search_team(name):
    url = "https://v3.football.api-sports.io/teams"
    headers = {"x-apisports-key": API_KEY, "Content-Type": "application/json"}
    params = {"search": name}

    print(f"\nЗапит до API: {url} з параметрами {params}")
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("response") or None

    print(f"Помилка {response.status_code}: {response.text}")
    return None


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


def main():
    search_option = input("Введіть ім'я команди: ").strip()
    team_result = search_team(search_option)

    if team_result:
        selected_team = choose_team(team_result)
        if selected_team:
            show_team_details(selected_team)
    else:
        print("Команду не знайдено.")


if __name__ == "__main__":
    main()
