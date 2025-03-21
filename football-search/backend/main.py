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


def show_teams(teams):
    if not teams:
        print("Команда не знайдена.")
        return

    team_data = []
    for team in teams:
        info, venue = team["team"], team.get("venue", {})
        team_data.append(
            [
                info["id"],
                info["name"],
                info.get("code", "Невідомо"),
                info["country"],
                venue.get("city", "Невідомо"),
                info.get("founded", "Невідомо"),
                venue.get("name", "Невідомо"),
                venue.get("capacity", "Невідомо"),
                venue.get("surface", "Невідомо"),
                info["logo"],
            ]
        )

    df = pd.DataFrame(
        team_data,
        columns=[
            "ID",
            "Назва",
            "Код",
            "Країна",
            "Місто",
            "Рік заснування",
            "Стадіон",
            "Місткість стадіону",
            "Тип покриття",
            "Логотип",
        ],
    )
    df = df.fillna("Невідомо")
    print(df)


def main():
    search_query = input("Введіть ім'я команди: ").strip()
    team_result = search_team(search_query)

    if team_result:
        print("\nКоманда знайдена:")
        show_teams(team_result)
    else:
        print("Команда не знайдена.")


if __name__ == "__main__":
    main()
