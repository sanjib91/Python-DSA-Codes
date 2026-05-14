def valid_brackets(s: str) -> bool:
    stack = []
    mapped_pairs = {')':'(', '}':'{',']':'['}
    count = 0

    for char in s:
        if char in '({[':
            stack.append(char)

        elif char in ')}]':
            if stack and stack[-1] == mapped_pairs[char]:
                stack.pop(); count += 1
            else:
                return False , count

    return not stack, count

tests =  [
    '{{{]]}}}',
    '(((())))',
    '{{[[[]]]]]}}',
    '{([])}'
]


for i in tests:
    result = valid_brackets(i)
    print(f"{i} seems to be {result}")