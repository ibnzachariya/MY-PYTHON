"""
Census App for Minna, Niger State
Author: Abdulfatai
Description:
A simple census application that displays population, tribes,
weather conditions, and towns in Minna. It also posts updates
to an API (JSONPlaceholder).
"""

import requests

# Base API URL
API_URL = "https://jsonplaceholder.typicode.com"

# Hardcoded census data for Minna
census_data = {
    "population": "500,000 (approx.)",
    "tribes": ["Nupe", "Gwari", "Hausa", "Fulani", "Yoruba"],
    "weather": "Hot climate, average 34°C, rainy season May–October",
    "towns": ["Bosso", "Chanchaga", "Tunga", "Kpakungu", "Fadikpe"]
}

def display_census():
    """Display census data for Minna."""
    print("📊 Minna Census Data\n")
    print(f"Population: {census_data['population']}")
    print(f"Tribes: {', '.join(census_data['tribes'])}")
    print(f"Weather: {census_data['weather']}")
    print(f"Towns: {', '.join(census_data['towns'])}\n")

def post_update(category, new_value):
    """
    Post updated census info to API.
    Simulated using 'posts' endpoint.
    """
    payload = {
        "title": f"Update to {category}",
        "body": new_value,
        "userId": 1
    }
    response = requests.post(f"{API_URL}/posts", json=payload)
    return response.json()

def census_app():
    """Main census app function."""
    display_census()

    choice = input("Do you want to add new data? (yes/no): ").lower()
    if choice == "yes":
        category = input("Which category (tribes/towns/weather/population)? ")
        new_value = input(f"Enter new {category}: ")

        result = post_update(category, new_value)
        print(f"✅ Update submitted! Server response ID: {result['id']}\n")

    print("🎉 Census App Finished. Thank you!")

# Run the app
if __name__ == "__main__":
    census_app()
