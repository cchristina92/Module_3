import csv
import os

# Set file path 
file_path = os.path.join("C:\Users\cchri\Desktop\Data Analyst Bootcamp\Homework\Module 3\Module_3\PyBank\Resources\budget_data.csv")

# Set text output
text_path = os.path.join("analysis", "analysis_results.txt")

# Variables
total_months = 0
net_total = 0
prev_profit_loss = 0
total_changes = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

# Read the CSV file
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Header row
    header = next(csvreader)
    
    # Loop through each row 
    for row in csvreader:
        # Update the total number of months
        total_months += 1
        
        # Get the profit/loss value for the current row
        current_profit_loss = int(row[1])
        
        # Calculate net total
        net_total += current_profit_loss
        
        # Calculate change in profit/loss
        if total_months > 1:
            change = current_profit_loss - prev_profit_loss
            total_changes += change
            
            # Check if the change is the greatest increase or decrease
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]
        
        
        prev_profit_loss = current_profit_loss

# Calculate average change
average_change = total_changes / (total_months - 1)

# Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month[0]} (${greatest_decrease[1]})\n")

print(output)

# Export to text file
with open(text_path, "w") as txt_file:
    txt_file.write(output)

