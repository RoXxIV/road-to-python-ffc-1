# Purpose: Demonstrate the use of list comprehension in Python
def convert_to_snake_case(pascal_or_camel_cased_string):

    # convert to snake case by adding an underscore before each capital letter
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    # join the list of characters into a string
    return ''.join(snake_cased_char_list).strip('_')

# main function
def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

if __name__ == '__main__':
    main()  # Call the main function