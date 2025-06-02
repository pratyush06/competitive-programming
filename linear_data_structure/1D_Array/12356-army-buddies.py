#TLE try to imporve solution

while True:
    no_of_solders, loss_reports = map(int, input().split())
    list_of_solders = list(range(1, no_of_solders+1))
    if no_of_solders==0 and loss_reports==0:
        break
    for i in range(loss_reports):
        L, R = map(int, input().split())

        surviving_solders = []
        left_surviving_solders = '*'
        surviving_solders = list_of_solders[:list_of_solders.index(L)]
        if len(surviving_solders)>0:
            left_surviving_solders = surviving_solders[0]
        
        right_surviving_solders = '*'
        right = list_of_solders[list_of_solders.index(R)+1:]
        if len(right)>0:
            right_surviving_solders = list_of_solders[list_of_solders.index(R)+1:][0]                
        surviving_solders+=right
        print(f"{left_surviving_solders} {right_surviving_solders}")
        list_of_solders = surviving_solders
        if len(list_of_solders) == 0:
            break
    
    print('-')