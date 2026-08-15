# 05_collections.py
# Collections: Specialized container datatypes in Python

from collections import Counter, namedtuple, deque, defaultdict

def main():
    print("--- Collections Module ---")
    
    # 1. Counter: A dict subclass for counting hashable objects
    print("\n1. Counter:")
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    word_counts = Counter(words)
    print(f"Word counts: {word_counts}")
    print(f"Most common word: {word_counts.most_common(1)}")

    # 2. namedtuple: Factory function for creating tuple subclasses with named fields
    print("\n2. namedtuple:")
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(11, y=22)
    print(f"Point: {p}")
    print(f"Accessing by name (p.x, p.y): {p.x}, {p.y}")

    # 3. deque: List-like container with fast appends and pops on either end
    print("\n3. deque (Double-ended queue):")
    queue = deque(["Alice", "Bob", "Charlie"])
    queue.append("David")      # Add to right
    queue.appendleft("Eve")    # Add to left
    print(f"Queue after additions: {queue}")
    queue.pop()                # Remove from right
    queue.popleft()            # Remove from left
    print(f"Queue after removals: {queue}")

    # 4. defaultdict: Dict subclass that calls a factory function to supply missing values
    print("\n4. defaultdict:")
    # Using list as the default_factory to group items
    students_by_grade = defaultdict(list)
    students_by_grade["A"].append("Alice")
    students_by_grade["B"].append("Bob")
    students_by_grade["A"].append("Charlie")
    # 'C' does not exist yet, but it will automatically create an empty list and append 'David'
    students_by_grade["C"].append("David")
    
    for grade, students in students_by_grade.items():
        print(f"Grade {grade}: {students}")

if __name__ == "__main__":
    main()
