# Import Modules
import re

def arithmetic_arranger(problems):

    # Calculate the length of problems
    n = len(problems)
    if (n > 5):
      return "Error: Too many problems."

    # Set Up Variables
    first = ""
    second = ""
    lines = ""
    my_sum_x = ""
    my_string = ""

    # Apply for loop
    for problem in problems:
      if (re.search("[^\s0-9.+-]",problem)):
        if (re.search("[/]",problem) or re.search("[*]",problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."

      first_number = problem.split(" ")[0]
      operator = problem.split(" ")[1]
      second_number = problem.split(" ")[2]
      if (len(first_number) >= 5 or len(second_number) >= 5):
        return "Error: Numbers cannot be more than four digits."

      my_sum = ""

      # Check for + or -
      if (operator=="+"):
        my_sum = str(int(first_number) + int(second_number))
      elif (operator=="-"):
        my_sum = str(int(first_number) - int(second_number))

      my_length = max(len(first_number), len(second_number)) + 2
      top = str(first_number).rjust(my_length)
      bottom = operator + str(second_number).rjust(my_length - 1)
      line = ""
      res = str(my_sum).rjust(my_length)

      # Add dashes in line
      for s in range(my_length):
        line += "-"

      # Apply Formatting
      if problem != problems[-1]:
        first += top + "    "
        second += bottom + "    "
        lines += line + "    "
        my_sum_x += res + "    "
      else:
        first += top
        second += bottom
        lines += line
        my_sum_x += res

    # Check for solve status
    if solve:
        my_string = first + "\n" + second + "\n" + lines + "\n" + my_sum_x
    else:
        my_string = first + "\n" + second + "\n" + lines
    return my_string
    
