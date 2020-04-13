#Import the Modules/CSV files
import pathlib
import csv

#Use module to open csv file location
budget_path = pathlib.Path('Resources/budget_data.csv')

#Open as csvfile
with open(budget_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #For loop to iterate through each month
    months = next(csvreader)
    
    months_count = 0
    profit = 0
    profit_change_sum = 0
    Profit_list = []
    profit_change = []
    date = []

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
print ("Financial Analysis")
print ("-----------------------")
print (f"Total Months: {months_count}")
print (f"Average Change: ${avg_profit}")
print(f"Greatest Increase in Profits: {g_inc_date} ({g_inc})")
print(f"Greatest Decrease in Profits: {g_dec_date} ({g_dec})")


# output_path = pathlib('Analysis/Financial_Analysis.txt')

# with open(output_path, 'w') as f:
#     f.write("Hello World")