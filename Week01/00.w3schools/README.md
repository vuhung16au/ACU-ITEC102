# Week 01 — Python Refresher via W3Schools

Welcome to Week 1! This section provides a refresher on core Python concepts using [W3Schools](https://www.w3schools.com/python/). Work through each topic in order, running the examples in your preferred environment (Google Colab, VS Code, or Docker).

---

## Topics

### 1. Run "Hello World" in Python

Get started by running your very first Python program.

- 🔗 [Python Getting Started](https://www.w3schools.com/python/python_getstarted.asp)

```python
print("Hello, World!")
```

---

### 2. Python Statements

Learn how Python reads and executes code line by line.

- 🔗 [Python Statements](https://www.w3schools.com/python/python_statements.asp)

**Key concepts:**
- Multi-line statements using `\` or implicit continuation inside brackets
- Indentation as a block delimiter (not just style!)

---

### 3. Variables

Understand how to store and name data in Python.

- 🔗 [Python Variables](https://www.w3schools.com/python/python_variables.asp)

```python
name = "Alice"
age = 20
is_student = True
print(name, age, is_student)
```

**Key concepts:**
- Dynamic typing — no need to declare a type
- Variable naming rules (case-sensitive, no spaces)
- Multiple assignment: `x, y, z = 1, 2, 3`

---

### 4. Numbers

Explore the different numeric types in Python.

- 🔗 [Python Numbers](https://www.w3schools.com/python/python_numbers.asp)

```python
x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex

print(type(x), type(y), type(z))
```

**Key concepts:**
- `int`, `float`, `complex`
- Conversion functions: `int()`, `float()`, `complex()`
- The `random` module for random numbers

---

### 5. Operators

Learn how to perform operations on values and variables.

- 🔗 [Python Operators](https://www.w3schools.com/python/python_operators.asp)

```python
# Arithmetic
print(10 + 3)   # 13
print(10 ** 2)  # 100 (power)
print(10 // 3)  # 3 (floor division)
print(10 % 3)   # 1 (modulo)

# Comparison
print(10 > 3)   # True
print(10 == 10) # True

# Logical
print(True and False)  # False
print(True or False)   # True
```

**Key concepts:**
- Arithmetic, Assignment, Comparison, Logical, Identity (`is`), Membership (`in`), Bitwise operators

---

### 6. Lists

Work with one of Python's most versatile data structures.

- 🔗 [Python Lists](https://www.w3schools.com/python/python_lists.asp)

```python
fruits = ["apple", "banana", "cherry"]

# Access
print(fruits[0])    # apple
print(fruits[-1])   # cherry (last item)

# Modify
fruits.append("mango")
fruits.remove("banana")
print(fruits)

# Slicing
print(fruits[1:3])

# Loop
for fruit in fruits:
    print(fruit)
```

**Key concepts:**
- Lists are ordered, changeable, and allow duplicate values
- Common methods: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `len()`
- List comprehension: `squares = [x**2 for x in range(10)]`

---

## ✅ Verification

After completing all topics, you should be able to write a short Python script that:

1. Prints "Hello, World!"
2. Declares variables of different types
3. Performs arithmetic and comparison operations
4. Creates and manipulates a list

```python
# Mini-challenge
name = "ITEC102"
scores = [85, 92, 78, 95, 88]
average = sum(scores) / len(scores)
print(f"Hello, {name}!")
print(f"Scores: {scores}")
print(f"Average score: {average:.2f}")
```

---

## 📚 Additional Resources

- [W3Schools Python Tutorial (Full)](https://www.w3schools.com/python/)
- [Python Official Docs](https://docs.python.org/3/)
