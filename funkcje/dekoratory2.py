def upper_case(func):
    def wew():
        result = func()
        return result.upper()

    return wew


def bold_decoration(func):
    def wew():
        result = func()
        return "\033[1m" + result + "\033[0m"

    return wew


@bold_decoration
@upper_case
def greeting():
    return "Hello World!"


print(greeting())
