# Lab6
# Author: Daniel Flesch

## add in functions from test.py's test statements here to make the pytest work
def calculate_rectangle_area(width:float, height:float):

    return width * height

def calculate_hypotenuse(side_a:float, side_b:float):

    return (side_a**2 + side_b**2)**0.5

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def find_maximum(number1:float, number2:float) -> float:
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    else:
        print("Error input is either invalid or one is not greater than the other.")

def grade_calculator(grade_input):
    if grade_input >= 90 and grade_input <= 100:
        return "A"
    if grade_input >= 80 and grade_input < 90:
        return "B"
    if grade_input >= 70 and grade_input < 80:
        return "C"
    if grade_input >= 60 and grade_input < 70:
        return "D"
    if grade_input >= 50 and grade_input < 60:
        return "F"
    else:
        return "Invalid Score"

def main():
    pass


if __name__ == "__main__":
    main()
