# Calculator Program

## Overview
This is a simple calculator program that evaluates mathematical expressions using **Reverse Polish Notation (RPN)**. The program supports basic arithmetic operations such as addition, subtraction, multiplication, division, and exponentiation. 

## Features
- Validates expressions for syntax errors.
- Converts infix expressions (standard mathematical notation) into Reverse Polish Notation.
- Performs calculations using RPN for evaluation.

## Supported Operators
The program supports the following operators:
- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division)
- `^` (Exponentiation)

## Program Functions

### `validate_expression(expression)`
Validates the mathematical expression to ensure it has valid characters and structure.

- **Input:** String (`expression`)
- **Example:**
  ```python
  validate_expression("3 + 5 * 2")
  ```
- **Output:** Returns `True` if valid, raises an error if invalid.

### `Calculate()`
Performs the calculation using the generated RPN list.

- **Input:** None (operates on the global `RPNlist` and `stack`).
- **Example:** 
  ```python
  RPNlist = ['3', '5', '2', '*', '+']
  Calculate()
  ```
- **Output:** Updates the `stack` with the result.

### `reverseString(text)`
Reverses a given string. This function is used internally during the conversion of the operator stack.

- **Input:** String (`text`)
- **Example:**
  ```python
  reverseString("5+3")
  ```
- **Output:** `"3+5"`

### `clearx()`
Resets all global variables such as the expression, stack, and RPN list.

- **Input:** None
- **Example:**
  ```python
  clearx()
  ```
- **Output:** Clears global variables for the next calculation.

### `convertToRPN()`
Converts an infix expression (standard notation) into Reverse Polish Notation (RPN).

- **Input:** None (operates on the global `expression` variable).
- **Example:**
  ```python
  expression = "3 + 5 * 2"
  convertToRPN()
  ```
- **Output:** Updates the `RPNlist` with the RPN version of the expression.

### `evaluate()`
Runs the full process of validating, converting to RPN, and calculating the result.

- **Input:** None (operates on the global `expression` variable).
- **Example:**
  ```python
  expression = "3 + 5 * 2"
  evaluate()
  ```
- **Output:** Prints the RPN expression and the result.

### `main()`
The entry point of the program. Handles user input and runs the evaluation loop.

- **Input:** None
- **Example:**
  ```python
  main()
  ```
- **Output:** Interactively takes mathematical expressions from the user, evaluates them, and prints the results.

## Example Usage

```bash
Enter an expression : 3 + 5 * 2
RPN : ['3', '5', '2', '*', '+']
Answer : [13.0]

Enter an expression : 4 ^ 2 / 2
RPN : ['4', '2', '^', '2', '/']
Answer : [8.0]
```

## Error Handling
- The program throws appropriate errors for division by zero, invalid characters, and invalid expression structure (e.g., consecutive operators).

