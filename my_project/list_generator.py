#List generator upto range
def list_generator(n):
    stack = []
    for i in range(1, n+1):
        stack.append(i)

    return stack

print(list_generator(100))        