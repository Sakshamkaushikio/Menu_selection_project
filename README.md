# Simple Food Order Program

A simple beginner-friendly Python project that uses the **`random` module** and **`match` / `case`** statements to simulate a basic food ordering system.

## About the Project

The program asks the user to choose a food item:

* **1 → Burger**
* **2 → Pizza**
* **3 → Pasta**

After the user makes a choice, the program displays the selected food along with a randomly generated **order number between 1 and 20**.

If the user enters anything other than `1`, `2`, or `3`, the program displays a message asking them to enter a valid input.

## Concepts Used

This project was created to practice basic Python concepts, including:

* `import random`
* `random.randint()`
* `input()` for taking user input
* `match` and `case`
* f-strings
* Basic pattern matching
* Handling invalid input with `case _`

## Example

```text
Enter 1 for Burger, 2 for Pizza or 3 for Pasta: 2

You ordered a Pizza, Order number- 14
```

Another example:

```text
Enter 1 for Burger, 2 for Pizza or 3 for Pasta: 5

Please enter a valid input
```

## How It Works

The program generates a random order number using:

```python
random.randint(1, 20)
```

The user's choice is then checked using `match` and `case`:

```python
case "1"  → Burger
case "2"  → Pizza
case "3"  → Pasta
case _    → Invalid input
```

## How to Run

Make sure Python is installed on your computer.

Run the program from the terminal:

```bash
python main.py
```

## Purpose

This is a beginner Python practice project created to understand the **`random` module**, **`match` / `case`**, user input, and basic program flow.
