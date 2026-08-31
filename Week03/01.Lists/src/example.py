# Lists: Ordered, Mutable Data


def main():
    # Creating and modifying a list
    aussie_cities = ["Sydney", "Melbourne", "Brisbane"]
    print(f"Initial list: {aussie_cities}")

    # Adding an item (Append adds to the end)
    aussie_cities.append("Perth")
    print(f"After appending: {aussie_cities}")

    # Removing an item
    aussie_cities.remove("Melbourne")
    print(f"After removing Melbourne: {aussie_cities}")

    # Sorting alphabetically
    aussie_cities.sort()
    print(f"My travel itinerary: {aussie_cities}")


if __name__ == "__main__":
    main()
