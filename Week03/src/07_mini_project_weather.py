# 07_mini_project_weather.py
# Mini Project – Simple Weather & Event Planner

def main():
    print("--- Simple Weather & Event Planner ---")
    
    # Dictionary storing weather forecasts for the week
    weather_forecast = {
        "Monday": "Sunny",
        "Tuesday": "Rainy",
        "Wednesday": "Cloudy",
        "Thursday": "Sunny",
        "Friday": "Rainy",
        "Saturday": "Sunny",
        "Sunday": "Windy"
    }
    
    # Sets storing days suitable for different types of events
    outdoor_events = {"Sunny", "Cloudy"}
    indoor_events = {"Rainy", "Windy", "Sunny", "Cloudy"}
    
    print("\nWeekly Forecast:")
    for day, weather in weather_forecast.items():
        print(f"{day}: {weather}")
        
    print("\nEvent Recommendations:")
    for day, weather in weather_forecast.items():
        recommendations = []
        if weather in outdoor_events:
            recommendations.append("Outdoor picnic")
            recommendations.append("Hiking")
        if weather in indoor_events:
            recommendations.append("Museum visit")
            recommendations.append("Board games at home")
            
        print(f"On {day} ({weather}): you could plan -> {', '.join(recommendations)}")

    # Using list comprehension to find all sunny days
    sunny_days = [day for day, weather in weather_forecast.items() if weather == "Sunny"]
    print(f"\nBest days for a beach trip (Sunny days): {', '.join(sunny_days)}")

if __name__ == "__main__":
    main()
