#Import relevant modules
import os
import csv

Total_Votes = 0
Counter = 0
Name_List = []
Cand_Name = ""
Cand_Votes = []
Percent_Votes = []
Max_Index = 0
Vote_Winner = ""
Max_VC = 0

with open("/Users/matthewvicario/Python_Challenge.git/PyPoll/Resources/election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csv.reader(csvfile):
        if Counter > 0:
            Total_Votes += 1
            Cand_Name = row[2]
            if Cand_Name in Name_List:
                Cand_Name_index = Name_List.index(Cand_Name)
                Cand_Votes[Cand_Name_index] = Cand_Votes[Cand_Name_index] + 1
            else:
                Name_List.append(Cand_Name)
                Cand_Votes.append(1)
        Counter += 1   
    for x,y in enumerate(Name_List):
        Percent_Line = round(Cand_Votes[x]/Total_Votes * 100, 3)
        Percent_Votes.append(Percent_Line)
        if Cand_Votes[x] > Max_VC:
            Max_VC = Cand_Votes[x]
            Max_Index = x
            Vote_Winner = Name_List[Max_Index] 
    

###FORMAT DATA TO PRINT
print("Election Results")
print("--------------------------------")
print("Total Votes: " + str(Total_Votes))
print("--------------------------------")
for x in range(len(Name_List)):
    print(f'{Name_List[x]} : {Percent_Votes[x]}% ({Cand_Votes[x]})')
print('-------------------------')
print(f'Election Winner: {Vote_Winner}')
print('-------------------------')
 


###OUTPUT
output_file = os.path.join("/Users/matthewvicario/Python_Challenge.git/PyPoll/Analysis/election_data.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    datafile.write('Election Results\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Total Votes: {Total_Votes}\n')
    for x in range(len(Name_List)):
        datafile.write(f'{Name_List[x]} : {Percent_Votes[x]}% ({Cand_Votes[x]})\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Election Winner: {Vote_Winner}\n')
    datafile.write('-------------------------\n')