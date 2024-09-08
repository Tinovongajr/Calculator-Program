# Calculator Program

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Supported Operators](#supported-operators)
- [Function List](#function-list)
- [Example Usage](#example-usage)
- [Error Handling](#error-handling)
- [Cloning and Contribution](#cloning-and-contribution)
- [License](#license)

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

## Function List

- **`validate_expression(expression)`**  
  Validates the expression for any syntax errors or invalid characters.

- **`Calculate()`**  
  Evaluates the expression in Reverse Polish Notation (RPN).

- **`reverseString(text)`**  
  Reverses a string (used internally for stack management).

- **`clearx()`**  
  Resets the calculator by clearing the expression, stack, and RPN list.

- **`convertToRPN()`**  
  Converts an infix expression to Reverse Polish Notation.

- **`evaluate()`**  
  Manages the full process from validating to calculating the result.

- **`main()`**  
  Entry point of the program that interacts with the user.

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
- **ZeroDivisionError**: Thrown when there is an attempt to divide by zero.
- **SyntaxError**: Raised when the expression is syntactically incorrect.
- **ValueError**: Occurs when the expression contains invalid characters or incorrect operator placement.

## Cloning and Contribution

### Cloning the repository
To clone the repository, use the following command:
```bash
git clone <repository-url>
```

### Contribution
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request with a detailed explanation of your changes.

## License
This project is licensed under the MIT License. You can view the full license [here](https://opensource.org/licenses/MIT).
