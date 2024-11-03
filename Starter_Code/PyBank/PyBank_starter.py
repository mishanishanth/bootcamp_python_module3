# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_profit_loss=None

# Add more variables to track other necessary financial data
profit_loss_change=[]
associated_dates=[]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    

    # Track the total and net change
   
    # Process each row of data
    for row in reader:
        dates=row[0]
        profit_loss=int(row[1])
        # Track the total
        total_net=total_net + profit_loss
        total_months=total_months+1

        # Track the net change
        if previous_profit_loss is not None:
             
                change = profit_loss-previous_profit_loss
                
                profit_loss_change.append(change)
                associated_dates.append(dates)

        previous_profit_loss=profit_loss    
            
    
    
        # Calculate the greatest increase in profits (month and amount)
greatest_profit_increase=max(profit_loss_change)  
greatest_profit_date=associated_dates[profit_loss_change.index(greatest_profit_increase)] 

        # Calculate the greatest decrease in losses (month and amount)
greatest_profit_decrease=min(profit_loss_change)
greatest_loss_date=associated_dates[profit_loss_change.index(greatest_profit_decrease)]


# Calculate the average net change across the months

average_change=sum(profit_loss_change)/(total_months-1)

# Generate the output summary


# Print the output
print(f"""
            financial summary
        *****************
            Total Months:{total_months}
            Total:  ${total_net}
            Average Change: ${average_change}
            Greatest Increase in Profits: {greatest_profit_date} $({greatest_profit_increase})
            Greatest decrease in Profits: {greatest_loss_date} $({greatest_profit_decrease})
            """)

#Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"Total Months:{total_months}\n")
    txt_file.write(f"Total:${total_net}\n")
    txt_file.write(f"Average Change:${average_change}\n")
    txt_file.write(f"Greatest Increase in profits:{greatest_profit_date} $({greatest_profit_increase})\n")
    txt_file.write(f"Greatest decrease in profits:{greatest_loss_date}$({greatest_profit_decrease})\n")
                   
