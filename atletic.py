'''
python script for acquiring championship points and telling the winner
0-39 groups
40-49 sum up
50-59 winners
'''

# declare team vector
team = [0] * 70

# run through vector
for i in range(0, 40):
    # exclude teams index from loop
    if i % 4 != 0:
        team[i] = int(input(
            "Input how many gold, silver, bronze medal in sequence each team received, if not received type 0"))
        # search for gold medals indexes
        if i % 4 == 1 or i == 1:
            # update gold medals points (3 points each gold medal)
            team[i] = team[i] * 3
        # search for gold medals indexes
        if i % 4 == 2 or i == 2:
            # update silver medals points (2 points each gold medal)
            team[i] = team[i] * 2
        # bronze medals does not need to have points converted (1 point each bronze medal)

# sum up points from team vector
for k in range(0, 40, 4):
    # integer division to remove step 4 from above loop, and sum up each team points
    team[k//4 + 40] = team[k+1] + team[k+2] + team[k+3]

print(team)
#find winner
win = team[40]
for w in range(41, 50):
    if team[w] > team[w-1]:
        win = team[w]
    elif team[w] == team [w-1]:
        team[w+10] = 1
        
'''      
for d in range(50, 59):
    if team[d] == team[d+1]:
        if team[d-49] > team[]
'''   

#check vector for equals ones
for d in range(50, 60):
    for f in range(50, 60):
        if team[d] == team[f] and d != f:
            #test gold
            if team[d-49] > team[(4*f-1)-199]:
                print(f"Winenr team is: {team[d-49]}")
            elif team[d-49] 










        
        
        
    
