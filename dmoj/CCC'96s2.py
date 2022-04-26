queries = int(input())

for _ in range(queries):
    integer = int(input())

    while (integer > 11):
        lastdigit = integer % 10
        integer = integer // 10
        integer -= lastdigit
        print(integer)
    
    if integer == 11:
        print(f"The number {integer} is divisible by 11.\n")
    
    else:
        print(f"The number {integer} is not divisible by 11.\n")