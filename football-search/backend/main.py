from team import search_team, choose_team, show_team_details
from player import search_player, choose_player, show_player_details, search_player_seasons

def main():
    while True:
        print("\nГоловне меню:")
        print("1. Пошук команди")
        print("2. Пошук гравця")
        print("3. Вийти")
        
        choice = input("Виберіть опцію: ")
        
        if choice == "1":
            team_name = input("Введіть назву команди: ").strip()
            team_result = search_team(team_name)
            if team_result:
                selected_team = choose_team(team_result)
                if selected_team:
                    show_team_details(selected_team)
            else:
                print("Команду не знайдено.")
                
        elif choice == "2":
            player_name = input("Введіть ім'я гравця: ").strip()
            player_result = search_player(player_name)
            
            if player_result:
                selected_player = choose_player(player_result)
                if selected_player:
                    player_id = selected_player["player"]["id"]  
                    player_season_data = search_player_seasons(player_id)  
                    if player_season_data:
                        show_player_details(selected_player)
                    else:
                        print("Інформація про сезон не знайдена.")
            else:
                print("Гравця не знайдено.")
                
        elif choice == "3":
            print("Вихід")
            break
            
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
