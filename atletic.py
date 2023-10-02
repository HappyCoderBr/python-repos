'''
python script for acquiring championship points and telling the winner
0-39 groups
40-49 sum up
50-59 winners
60-69 golds
70-79 silvers
80-89 bronzes
96-99 counters
'''

####     INDEXES: 0-69  ###
# declare team vector
team = [0] * 100
print(team)
print("\n")


###     INDEXES: 0-39 "GROUPS" INTS     ###
# run through vector
for i in range(0, 40):
    # exclude teams index from loop
    if i % 4 != 0:
        team[i] = 39-i
        # search for gold medals indexes
        if i % 4 == 1 or i == 1:
            # update gold medals points (3 points each gold medal)
            team[i] = team[i] * 3
        # search for gold medals indexes
        if i % 4 == 2 or i == 2:
            # update silver medals points (2 points each gold medal)
            team[i] = team[i] * 2
        # bronze medals does not need to have points converted (1 point each bronze medal)
print(team)
print("\n")


####    INDEXES: 40-49 "SUM UP" INTS     ###
# sum up points from GROUPS {s=sum up}
for s in range(0, 40, 4):
    # integer division to remove step 4 from above loop, and sum up each team points
    team[s//4 + 40] = team[s+1] + team[s+2] + team[s+3]
print(team)
print("\n")

# find the winner {wp=winner point}
WINNER_POINT = team[40]
for wp in range(40, 50):
    # only 1 winner
    if team[wp] > WINNER_POINT:
        WINNER_POINT = team[wp]


###     INDEXES: 50-59 "WINNERS" BINARY     ###
# add 1 to team[50-59] if there is more than 1 winner {wt=winner team}
for wt in range(40, 50):
    if team[wt] == WINNER_POINT:
        # creates INDEXES: 50-59 to assign if each of the 10 teams won
        team[wt+10] = 1
        # creates at SPECIAL INDEX:99 a counter for how many winners
        team[99] = team[99] + 1

# check if there is only one winner {ow=only winner}
if team[99] == 1:
    for ow in range(50, 60):
        if team[ow] == 1:
            print(f"The Winner Was: TEAM {ow - 50 + 1}")
# if there is more than 1 point winner: check gold winners
if team[99] != 1:
    # define what is the 1st winner index in order {fw=first winner, fwi=first winner index}
    for fw in range(50, 60):
        if team[fw] == 1:
            fwi = fw
            break

    # check medals {cgm=check gold medals}
    # define the first MORE_GOLD,SILVER,BRONZE for comparison purposes
    MORE_GOLDS = team[1]
    MORE_SILVERS = team[2]
    MORE_BRONZES = team[3]
    # checking for gold medals @ "WINNERS"
    for cgm in range(fw, 59):
        # making sure to only compare the winners (==1)
        if team[cgm] == 1:
            # associate 50-59 with initials groups indexes for medals
            # comparing gold medals between teams
            if team[(4 * (cgm + 1)) - 199] > team[(4 * cgm) - 199]:
                MORE_GOLDS = team[(4 * (cgm + 1)) - 199]

    ###     INDEXES: 60-69 "GOLD WINNERS" BINARY    ###
    # add 1 to team[60-69] if there is more than 1 gold winner {agw=add gold winners}
    for agw in range(fw, 60):
        if team[(4 * agw) - 199] == MORE_GOLDS:
            team[agw + 10] = 1
            # creates @ SPECIAL INDEX:98 a counter for how many gold medal finalists
            team[98] = team[98] + 1
    # check if there is only one gold medal finalist {gf=gold finalists}
    if team[98] == 1:
        for gf in range(60, 70):
            if team[gf] == 1:
                print(f"The Winner Was: TEAM {gf - 60 + 1}")
    # if there is more than one gold medal winner: check silver medal winners
    if team[98] != 1:
        # checking for silver medals {csm=check silver medals}
        for csm in range(60, 70):
            # making sure only gold medals top winners are compared
            if team[csm] == 1:
                # associate 60-69 with initials groups indexes for medals
                if team[4 * (csm + 1) - 242] > MORE_SILVERS:
                    MORE_SILVERS = team[4 * (csm + 1) - 242]
        ###     INDEXES:70-79 "SILVER WINNERS" BINARY     ###
        # add 1 to team[70-79] if there is more than 1 silver winner {asw=add silver winners}
        for asw in range(60, 70):
            if team[(4 * asw) - 238] == MORE_SILVERS:
                team[asw + 10] = 1
                # creates @ SPECIAL INDEX:97 a counter for how many silver medal finalists
                team[97] = team[97] + 1
        # check if there is only one silver medal finalist {sf=silver finalists}
        if team[97] == 1:
            for sf in range(70, 80):
                if team[sf] == 1:
                    print(f"The Winner Was: TEAM {sf - 70 + 1}")
        # if there is more than one silver medal winner: check bronze medal winners
        if team[97] != 1:
            # checking for bronze medal winners {cbm=check bronze medal}
            for cbm in range(70, 80):
                # making sure only silver medals top winners are compared
                if team[cbm] == 1:
                    # associate 70-79 with initials groups indexes for medals
                    if team[4 * (cbm + 1) - 281] > MORE_BRONZES:
                        MORE_BRONZES = team[4 * (cbm + 1) - 281]
            # add 1 to team[80-89] if there is more than 1 bronze winner {abw=add bronze winners}
            for abw in range(70, 80):
                if team[4 * (abw + 1) - 281] == MORE_BRONZES:
                    team[abw + 10] = 1
                    # creates @ SPECIAL INDEX:97 a counter for how many silver medal finalists
                    team[96] = team[96] + 1
            # check if there is only one silver medal finalist {bf=bronze finalists}
            if team[96] == 1:
                for bf in range(80, 90):
                    if team[bf] == 1:
                        print(f"The Winner Was: TEAM {team[bf - 70] + 1}")

            # if more than one team have the same amount of bronze medals, there is a draw!
            if team[96] != 1:
                print("There is a DRAW!")
