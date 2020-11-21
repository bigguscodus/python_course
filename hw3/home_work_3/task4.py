def is_armstrong(number: int) -> bool:
    number_by_digits = [int(digit) for digit in str(number)]
    return (
        sum(map(lambda digit: digit ** len(number_by_digits), number_by_digits))
        == number
    )
