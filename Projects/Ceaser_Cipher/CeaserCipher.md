# Caesar Cipher (Python)

## Description

This project is a beginner-friendly Python implementation of a simple Caesar cipher. The program encrypts a user-entered message by shifting each character a fixed number of positions using Python's built-in `ord()` and `chr()` functions.

This project demonstrates one of the earliest and most well-known encryption techniques while helping me understand the fundamentals of text manipulation and basic cryptography concepts.

## Purpose

I created this project to practice:

* User input (`input()`)
* Variables
* `for` loops
* String manipulation
* The `ord()` function
* The `chr()` function
* Basic encryption concepts

## Features

* Accepts a message from the user.
* Encrypts the message using a fixed shift value.
* Displays the encrypted output.
* Demonstrates a simple substitution cipher.

## Requirements

* Python 3.x

No external libraries are required.

## How to Use

1. Open the Python script.
2. Run the program.
3. Enter a message when prompted.
4. The program encrypts the message using the predefined shift value.
5. The encrypted message is displayed on the screen.

## How It Works

The script uses a shift value of **3**. Each character in the message is converted to its ASCII/Unicode value using `ord()`, increased by the shift value, and then converted back into a character using `chr()`.

For example:

```
Original: ABC
Shift:    3
Result:   DEF
```

## Note

This project is intended for educational purposes to demonstrate the basic idea behind a Caesar cipher. It is **not** secure for protecting sensitive information. Modern encryption uses much stronger algorithms and security techniques.

---

Created as part of my Python learning journey and GitHub portfolio.
