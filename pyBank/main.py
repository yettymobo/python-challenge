#   import os library to standardize file path across various os , cs library to open and close csv files, datetime library to convert date string to date format
import os
import csv
from datetime import datetime

#   Define file path for source file
file_path = os.path.join('Resources', 'budget_data.csv')

# create empty strings to be populated later
month_list = []
profitloss_list = []
profitlossdelta_list = []
newdate_list = []


#   open source csv file as read only and specify how file is delimited and extract applicable data to lists before closing
with open(file_path, 'r') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ',')

    header = next(csv_reader)

    for row in csv_reader:
        month_list.append(row[0])
        profitloss_list.append(int(row[1]))

# Steps to ensure profit/Loss list is ordered correctly in preparation for calculating monthly change - Date formatting, tuple conversion of both lists, sorting zipped lists
for i in month_list:
    newdate_list.append(datetime.strptime(i, '%b-%Y' ))

zipped_lists = zip(newdate_list, profitloss_list)
sorted_zipped_lists = sorted(zipped_lists)
sorted_profit_loss_list = [element for _, element in sorted_zipped_lists]
   
#   Calculate the total number of months 
months_count = len(month_list)

#   Calculate the total profit
total = sum(profitloss_list)


#   Calculate monthly change over the period and append in new list
for i, j in zip(sorted_profit_loss_list[0::], sorted_profit_loss_list[1::]):
    profitlossdelta_list.append(j-i)
#   Since the first value has no change calculation, insert 0 in o index of list. This is in preparationof creating a dictionary
profitlossdelta_list.insert(0, 0)
    
#   Now that we know the monthly change over the period, calculate the Greatest decrease, greatest increase, and average change from the list
lowest = min(profitlossdelta_list)
highest = max((profitlossdelta_list))
avg_change = '${:,.2f}'.format(sum(profitlossdelta_list)/ (months_count - 1))

# Create dictionary key for profit/loss change list in order to extract the corressponding months for the min and max values
dictionary_results = dict(zip(month_list, profitlossdelta_list))

#   Define the keys list and values list
key_list = list(dictionary_results.keys()) 
val_list = list(dictionary_results.values()) 

#   Derive the dates from the dictionary lists
lowest_date = (key_list[val_list.index(lowest)]) 
highest_date = (key_list[val_list.index(highest)])

# Define variable that will contain string to print to terminal and text file
results = (
    f"```text\n"
    f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {months_count}\n"
    f'Total: ${total}\n'
    f'Average Change: {avg_change}\n'
    f'Greatest Increase in Profits: {highest_date} (${highest})\n'
    f'Greatest Decrease in Profits: {lowest_date} (${lowest})\n'
    f' ```\n'
)

#   print to terminal
print(results)

#   print to text file
output_path = os.path.join('Analysis', 'financial_results.txt')
with open(output_path, 'w') as txt_file:
    txt_file.write(results)


