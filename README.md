# Calculator

This is a simple calculator application built using Python and the tkinter library. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Usage

To use the calculator, simply run the `main.py` file. The calculator interface will appear, allowing you to enter your calculations.

### Calculation

To perform a calculation, enter your expression using the number buttons and the operation buttons. For example, to calculate 3 + 4, you would press the buttons for 3, +, and 4. The result will be displayed in the entry field.

### Clearing the Entry

To clear the entry field, press the 'C' button. This will remove all text from the entry field, allowing you to start a new calculation.

### Examples

Here are some example calculations you can perform using the calculator:

- 3 + 4 = 7
- 5 - 2 = 3
- 6 * 3 = 18
- 9 / 3 = 3

## Code Structure

The code for the calculator is organized into the following sections:

1. Import the necessary libraries: `import tkinter as tk` and `from tkinter import ttk`.
2. Define the `calculate` function, which takes the expression from the entry field, evaluates it using the `eval` function, and displays the result in the entry field. If there is an error in the expression, the function will display an error message.
3. Define the `clear_entry` function, which clears the entry field by deleting all text from it.
4. Define the `add_to_entry` function, which takes a symbol as an argument and appends it to the current text in the entry field.
5. Create the main window for the calculator and set its title.
6. Create the entry field and add it to the main window.
7. Create the number buttons and add them to the main window.
8. Create the operation buttons (addition, subtraction, multiplication, and division) and add them to the main window.
9. Create the 'C' button for clearing the entry field and add it to the main window.
10. Configure the main window to allow for resizing and adjust the size of the entry field and buttons accordingly.
11. Start the main event loop for the tkinter window.

## License

This calculator is licensed under the MIT License. You can find a copy of the license in the LICENSE file.
