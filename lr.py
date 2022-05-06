from collections import defaultdict
from queue import Queue
import string

epsilon = '#'

n = int(input('Enter the number of production rules: '))

memo = defaultdict(list)

start_symbol = ''
print('Enter the production rules:')
for i in range(n):
    inp = input()
    left, _, right = inp.partition('->')
    left = left.strip()
    right = right.strip()
    lexemes = right.split('|')
    if i == 0:
        start_symbol = left
        # Augmenting the grammer
        memo[start_symbol + "'"].append(start_symbol)
    for l in lexemes:
        memo[left].append(l)

for key in memo:
    memo[key] = ['.' + i for i in memo[key]]

def display(memo):
    for key, values in memo.items():
        for val in values:
            print(key, '->', val)


state = 0
print('\nState I%d => '%(state))
display(memo)

q = Queue()
q.put(0)

temp = defaultdict(lambda: defaultdict(list))
next_state = defaultdict(lambda: defaultdict())

for key, values in memo.items():
    for v in values:
        temp[0][key].append(v)

while True:
    prev = q.get()
    s = []
    for key, values in temp[prev].items():
        for l in values:
            closure = l.find('.')
            if closure < len(l) - 1:
                l = list(l)
                l[closure], l[closure+1] = l[closure+1], l[closure]
                l = ''.join(l)
                closure += 1
                found = 0
                for i in range(state):
                    for k, v in temp[i].items():
                        for j in v:
                            if k == key and l == j:
                                found = i
                if not found:   
                    if l[closure-1] not in s:         
                        state += 1
                    q.put(state)
                    temp[state][key].append(l)
                    if closure <= len(l) - 2:
                        indx = closure + 1
                        for v in memo[l[indx]]:
                            temp[state][l[indx]].append(v)
                            
                    s.append(l[closure-1])
                    next_state[prev][l[closure-1]] = state
                else:
                    next_state[prev][l[closure-1]] = found
    if q.empty():
        break
    
for i in range(state):
    for key, value in next_state[i].items():
        print('\nGoto (I%d, %s)' % (i, key))
        for k, v in temp[value].items():
            for l in v:
                print(k, '->', l)



    

        


            


         

        
