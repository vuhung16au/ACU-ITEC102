# Sets: Unordered, Unique Items

def main():
    # Using a set to clean up messy, duplicate data
    messy_responses = ["Python", "Java", "Python", "C++", "Java", "Python"]
    print(f"Original messy data: {messy_responses}")
    
    unique_languages = set(messy_responses)
    print(f"Unique languages requested: {unique_languages}")

    # Adding to a set
    unique_languages.add("R")
    print(f"Updated languages after adding 'R': {unique_languages}")

if __name__ == "__main__":
    main()
