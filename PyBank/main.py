#Import the Modules/CSV files
import pathlib
import csv

#Use module to open csv file location
budget_path = pathlib.Path('Resources/budget_data.csv')

#Open as csvfile
with open(budget_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Variables
    months = next(csvreader)
    
    months_count = 0
    profit = 0
    profit_change_sum = 0
    Profit_list = []
    profit_change = []
    date = []

    #For loop to iterate through each month
    for row in csvreader:
        #Count the number of Months
        months_count += 1

        #Sum the profit/loss
        profit += int(row[1])
    
        #Calculate the change each month
        Profit_list.append(int(row[1]))

        #Capturing Dates Only
        date.append(row[0])


    for i in range(1, len(Profit_list)):
        profit_change.append(Profit_list[i]-Profit_list[i-1])
        profit_change_sum += profit_change[i-1]
    

    #Average the change over the total months captured
    avg_profit = profit_change_sum/(months_count-1)
    
    #Find the Greatest increase in profit
    g_inc = Profit_list[0]
    g_dec = Profit_list[0]
    for i in range (1, len(date)):
        if int(g_inc) < int(Profit_list[i]):
            g_inc = Profit_list[i]

          #Find the month associated with the greatest profit 
            g_inc_date = date[i]

        #Find the Greatest decrease in loss
        elif int(g_dec) > int(Profit_list[i]): 
            g_dec = Profit_list[i-1]

            #Find the month associated with the greatest loss
            g_dec_date = date[i-1]


#Print out the message

Line_1 = "Financial Analysis"
Line_2 = "-----------------------"
Line_3 = f"Total Months: {months_count}"
Line_4 = f"Average Change: ${avg_profit}"
Line_5 = f"Greatest Increase in Profits: {g_inc_date} ({g_inc})"
Line_6 = f"Greatest Decrease in Profits: {g_dec_date} ({g_dec})"

print (Line_1,"\n",Line_2,"\n",Line_3,"\n",Line_4,"\n",Line_5,"\n",Line_6, sep="")

#Create text file fo analysis
output_path = pathlib.Path('Analysis/Financial_Analysis.txt')

with open(output_path, 'w') as output:
    output.write("{}\n{}\n{}\n{}\n{}\n{}\n".format(Line_1, Line_2, Line_3, Line_4, Line_5, Line_6))