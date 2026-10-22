# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    char_stack = []
    for char in S:
        if char in ['(', '[', '{']:
            char_stack.append(char)
        if char == ')':
            if char_stack and char_stack[-1] == '(':
                char_stack.pop()
            else: 
                return 0
        
        if char == ']':
            if char_stack and char_stack[-1] == '[':
                char_stack.pop()
            else: 
                return 0

        if char == '}':
            if char_stack and char_stack[-1] == '{':
                char_stack.pop()
            else: 
                return 0
        
    return int(len(char_stack) == 0)
            
