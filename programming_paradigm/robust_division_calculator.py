def safe_divide(numerator, denominator):
    try:
        return float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except ValueError:
        return "Invalid input!"