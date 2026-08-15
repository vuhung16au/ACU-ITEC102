# 02_tuples.py
# Tuples: Ordered and immutable sequences

def main():
    print("--- Tuples ---")
    # Creating a tuple
    coordinates = (10.5, 20.3)
    print(f"Coordinates: {coordinates}")
    
    # Accessing elements (Ordered)
    x = coordinates[0]
    y = coordinates[1]
    print(f"X: {x}, Y: {y}")
    
    # Tuples are immutable, so we cannot do this:
    # coordinates[0] = 15.0  # This would raise a TypeError
    
    # Unpacking a tuple
    # lattitude, longitude = coordinates
    lat, lon = (-33.856608, 151.215272)
    print(f"Opera House - Latitude: {lat}, Longitude: {lon}")
    
    # Returning multiple values from a function using tuples
    def get_user_info():
        return ("Alice", 25, "developer")
        
    name, age, profession = get_user_info()
    print(f"User: {name}, Age: {age}, Profession: {profession}")

if __name__ == "__main__":
    main()
