# verify a credit card number using the Luhn formula
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    # Add the odd digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Double the even digits and add the digits of the result
    sum_of_even_digits = 0

    # Get the even digits
    even_digits = card_number_reversed[1::2]

    # Double the even digits and add the digits of the result
    for digit in even_digits:
        number = int(digit) * 2
        # If the result is a two digit number, add the digits of the result
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # If the sum of the odd digits and the sum of the even digits is a multiple of 10, the card number is valid
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()  # Call the main function

