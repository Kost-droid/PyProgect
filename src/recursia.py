

def factorial (count: int, result_factorial = 1) -> int:
    if count == 0:
        return result_factorial
    return factorial(count - 1, result_factorial * count)


def factorial_triangle (count: int) -> int:
    if count == 1:
        return count
    return count * factorial_triangle (count - 1)

def revers (string: str, revers_result = '') -> str:
    if len (string) == 0:
        return revers_result
    revers_result  += string [-1]
    return revers(string [:-1], revers_result)

def recurs_sum (counts: list) -> int:
    if not counts:
        return 0
    return counts [0] + recurs_sum(counts [1:])


def main ():
    print (factorial_triangle (4))

main ()
