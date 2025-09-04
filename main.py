from weather_api import get_weather
from utils import load_history, save_history

def main():
    history = load_history()

    while True:
        print("\n=== Weather App ===")
        print("1. Search weather by city")
        print("2. Show search history")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            city = input("Enter city name: ").strip()
            if not city:
                print("City name cannot be empty!")
                continue

            weather = get_weather(city)
            if weather:
                print(f"\nWeather in {weather['city']}:")
                print(f"Temperature: {weather['temperature']}°C")
                print(f"Condition: {weather['condition']}")
                
                # Save to history
                history.append(weather)
                save_history(history)
            else:
                print("Could not retrieve weather data.")

        elif choice == "2":
            if not history:
                print("No search history yet.")
            else:
                print("\n=== Search History ===")
                for i, record in enumerate(history, start=1):
                    print(f"{i}. {record['city']} - {record['temperature']}°C - {record['condition']}")
        
        elif choice == "3":
            print("Exiting app. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
