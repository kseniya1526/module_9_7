def is_prime(func):
    def wrapper(a,b,c):
        original_result = func(a,b,c)
        if original_result > 1:
            for i in range(2,original_result -1):
                if original_result % i == 0:
                    print('Составное')
                    break
            else:
                print('Простое')
        else:
            print('Это не простое и не составное число')
        return original_result
    return wrapper


@is_prime
def sum_three(a,b,c):
    summa = int(a + b + c)
    return summa


result = sum_three(2, 3, 6)
print(result)

