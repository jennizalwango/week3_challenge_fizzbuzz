


def fizzbuzz(listA ,listb):
    answer = sum(listA) + sum(listb)
    print(answer)
    if answer % 3 == 0 and answer % 5 == 0:
        return "fizzbuzz "
    elif answer % 3 == 0:
        return "fizz"
    elif answer % 5 == 0:
        return "buzz"
    else:
        return "sum of lists not divisible by 5 or 3"


result = fizzbuzz(listA=[1,2,4,5,7.5,12],listb=[1,4,5,5,7.5,6])
print(result)
result2 = fizzbuzz(listA=[4,5,6,7,9,2],listb=[4,6,8,1,3,])
print(result2)