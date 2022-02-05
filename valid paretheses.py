from stack import Stack


def isValid(string, stack):
    for i in string:
        if i in '[{(':
            stack.push(i)
        elif i in ')}]':
            if stack.is_empty():
                return False
            else:
                if i == ']' and stack.peek() == '[':
                    stack.pop()
                elif i == '}' and stack.peek() == '{':
                    s.pop()
                elif i == ')' and stack.peek() == '(':
                    stack.pop()
                else:
                    return False
    if stack.is_empty():
        return True
    else:
        return False



s = Stack()
n = input()
print(isValid(n,s))
