'''python script for acquiring championship points and telling the winner'''

# declare team vector
team = [0] * 50

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
