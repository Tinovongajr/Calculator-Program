# Calculator Application

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple calculator application built with Python and Tkinter, supporting basic arithmetic operations and following the order of operations.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Implementation Details](#implementation-details)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division
- Exponentiation (power) operation
- Decimal point support
- Parentheses for grouping expressions
- Error handling for invalid expressions
- Conversion of infix notation to Reverse Polish Notation (RPN) for calculation

## Requirements

- Python 3.x
- Tkinter library (usually comes pre-installed with Python)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Tinovongajr/Calculator.git
   ```
2. Navigate to the project directory:
   ```
   cd Calculator
   ```

## Usage

Run the application using Python:

```
python main.py
```

The calculator GUI will appear. Use it as follows:

- Click number buttons (0-9) to input numbers
- Use operation buttons (+, -, *, /) for arithmetic operations
- Use '^' for exponentiation
- Use parentheses '(' and ')' to group expressions (input via keyboard)
- Press '=' to calculate the result
- Click 'Clear' to reset the calculator

## Error Handling

The calculator handles various errors, including:
- Division by zero
- Invalid expressions (e.g., consecutive operators, mismatched parentheses)
- Syntax errors

Error messages will be displayed in the calculator's display area.

## Implementation Details

- Uses the Shunting Yard algorithm to convert infix notation to Reverse Polish Notation (RPN)
- Performs calculations using the RPN expression
- GUI built with Tkinter for a simple, intuitive interface

## Limitations

- No direct input for negative numbers (subtraction works as expected)
- No GUI buttons for parentheses or exponentiation (supported in backend)

## Contributing

Contributions are welcome! Here are some ways you can contribute:

1. Report bugs
2. Suggest new features
3. Submit pull requests

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to all contributors who have helped shape this project
- Inspired by basic calculator applications and a desire to understand RPN

---

For any questions or support, please open an issue in the GitHub repository.
