from pfpf import infix_to_postfix, infix_to_prefix

OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+': 1, '-': 1, '*': 2, '/': 2}


def generate3AC(pos):
    print("\n### THREE ADDRESS CODE GENERATION ###")
    exp_stack = []
    t = 1
    for i in pos:
        if i not in OPERATORS:
            exp_stack.append(i)
        else:
            print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')   
            exp_stack = exp_stack[:-2]
            exp_stack.append(f't{t}')
            t += 1

def Quadruple(pos):
    stack = []
    t = 1
    for i in pos:
        if i not in OPERATORS:
            stack.append(i)
        else:
            print("{:^4}| {:^4} | {:^4} | t{}".format(i, stack[-2], stack[-1], t))
            stack = stack[:-2]
            stack.append(f't{t}')
            t += 1

def Triple(pos):
    stack = []
    t = 1
    for i in pos:
        if i not in OPERATORS:
            stack.append(i)
        else:
            print("{:^4}| {:^4} | {} ".format(i, stack[-2], stack[-1]))
            stack = stack[:-2]
            stack.append(f'({t})')
            t += 1
            
pt = {}

expres = input("INPUT THE EXPRESSION: ")
pre = infix_to_prefix(expres)
pos = infix_to_postfix(expres)
generate3AC(pos)
print("\nThe Quadruple Representation:")
print(" OP | ARG 1 | ARG 2 | RESULT ")
Quadruple(pos)
print("\nThe Triple Representation:")
print(" OP | ARG 1 | ARG 2 ")
Triple(pos)
