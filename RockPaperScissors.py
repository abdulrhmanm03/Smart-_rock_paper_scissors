import random



played_after = {"r": {"r": 1, "p": 1, "s": 1, "t": 3}, "p": {"r": 1, "p": 1, "s": 1, "t": 3}, "s": {"r": 1, "p": 1, "s": 1, "t": 3}}

def addafter(xi, x, dict):
    dict[x]["t"] += 1 
    dict[xi][x] += 1
    
def choice(r,p,s,t):  
    wp = (r/t)*100
    ws = (p/t)*100
    wr = (s/t)*100
    return random.choices(['r', 'p', 's'], weights = (wr, wp, ws))[0]
          
xi = D = L = W = 0

while True:
    x = ''  
    
    while True:
        print(" ")
        x = input("'r' for rock, 'p' for paper, 's' for sissor, 'x' to close: ")
        print(" ")
        x = x.lower().strip()
        if x in ['r', 'p', 's', 'x']:
            break
        print("enter a valid input")
    
    if x == 'x':
        break
    
    if not xi:
        y = random.choice(['r', 'p', 's'])
        xi = x
        played_after[x]["t"] += 1
    else:
        y = choice(played_after[xi]['r'], played_after[xi]['p'], played_after[xi]['s'], played_after[xi]["t"])
        addafter(xi, x, played_after)
        xi = x       
    
    if x == y :
        print('    draw')
        print("-------------")
        D +=1    
    else :
        if (x == 'r' and y == 'p') or (x == 'p' and y == 's') or (x == 's' and y == 'r'):
            print('  You Loss')
            print("-------------")
            L +=1       
        else :
            print('  You Win')
            print("-------------")
            W +=1    

print("---------------------------------")
print(f"      W: {W} || D: {D} || L: {L}")  
print("---------------------------------")                             
 