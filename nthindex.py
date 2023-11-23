# Write a Python program to remove the nth index character from a nonempty string.

# Solution: 

def remove_nth_char(input_string, n):

    if not input_string or n < 0 or n >= len(input_string):
        return "Invalid input"

    result_string = input_string[:n] + input_string[n + 1:]

    return result_string