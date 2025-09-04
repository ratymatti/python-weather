# Weather App (Python Console Application)

A simple Python console application that allows you to search for the current weather of any city using the [OpenWeatherMap API](https://openweathermap.org/api). The app also keeps a local search history using a JSON file.

---

## Features

- Search for current weather by city
- Display temperature and weather condition
- Save and view search history
- Uses variables, conditionals, loops, collections, file handling, modules, and external APIs
- Fetches JSON data from the internet
- Easy to extend and modify

---

## Requirements

- Python 3.8+  
- `requests` library  
- `python-dotenv` library  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ratymatti/python-weather.git
   cd weather_app


2. (Optional but recommended) Create a virtual environment:

    ```bash
    python -m venv venv
    ```

    Activate it:

    Windows:
    ```bash
    venv\Scripts\activate
    ```
    Mac/Linux:

    ```bash
    source venv/bin/activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```
4. Create a .env file in the project root:

    ```bash
   OPENWEATHER_API_KEY=your_actual_api_key_here
   ```
   You can get a free API key from OpenWeatherMap. Make sure the key is activated.

## Usage

Run the application

```bash
python main.py
```

You will see a menu:

```bash
=== Weather App ===
1. Search weather by city
2. Show search history
3. Exit

```

## Options

1. Search weather by city

    - Enter the name of the city you want the weather for.

    - The app will display temperature and weather condition.

    - The search will be saved in history.json.

2. Show search history

    - Displays all past searches with city name, temperature, and condition.

3. Exit

    - Exit the application.

## Files

- main.py – Main console interface

- weather_api.py – Handles API requests

- utils.py – Handles search history and file operations

- history.json – Stores past search history

- .env – Stores your private OpenWeatherMap API key (not included in repo)

- requirements.txt – Project dependencies

## Notes

- Ensure your .env file contains a valid OpenWeatherMap API key.

- The application gracefully handles empty or corrupted history.json files.

- You can extend the app to include more features, like weather icons, forecasts, or multiple units (Celsius/Fahrenheit).