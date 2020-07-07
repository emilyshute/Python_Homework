#Import relevant modules
import os
import csv

#Establish all variables
Total_Months = 0
Net_Total = 0
Counter = 0
G_Profit = 0
G_Date = ""
Prev_Profit = 0
Curr_Profit = 0
Diff_Profit = 0
D_Profit = 0
D_Date = ""
Total_Diff = 0 

#Declare CSV path
with open("/Users/matthewvicario/Python_Challenge.git/PyBank/Resources/Budget_Data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Begin looping through rows
    for row in csv.reader(csvfile):
        #If counter is not zero then....
        if Counter != 0:
            #Add a month for everyrow for our total months
            Total_Months += 1
            Net_Total += int(row[1])
            Prev_Profit = Curr_Profit
            Curr_Profit = int(row[1])
            if Counter > 1:

                Diff_Profit = Curr_Profit - Prev_Profit
                Total_Diff += Diff_Profit

                if Diff_Profit > G_Profit:
                    G_Profit = Diff_Profit
                    G_Date = row[0]

                elif Diff_Profit < D_Profit:
                    D_Profit = Diff_Profit
                    D_Date = row[0]

        Counter += 1

         
######  Format the Analysis
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: " + str(Total_Months))
    print("Total: $" + str(Net_Total))
    print("Average  Change: $" + str(round(Total_Diff / (Total_Months -1),2)))
    print("Greatest Increase in Profits: " + G_Date + " $" + str(G_Profit))
    print("Greatest Decrease in Profits: " + D_Date + " $" + str(D_Profit))


###OUTPUT
output_file = os.path.join("/Users/matthewvicario/Python_Challenge.git/PyBank/Analysis/budget_data.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    datafile.write('Budget Data\n')
    datafile.write('Financial Analysis\n')
    datafile.write('-----------------------------------\n')
    datafile.write(f'Total Months: {Total_Months}\n')
    datafile.write(f'Total: ${Net_Total}\n')
    datafile.write(f'Average  Change: ${round(Total_Diff / (Total_Months -1),2)}\n')
    datafile.write(f'Greatest Increase in Profits: {G_Date}  ${G_Profit}\n')
    datafile.write(f'Greatest Decrease in Profits: {D_Date}  ${D_Profit}\n')

    


