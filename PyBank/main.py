import csv 
import os

# Set the file path and text output
file_path = os.path.join("Resources", "budget_data.csv")
text_path = os.path.join("analysis", "analysis_results.txt")

# Variables
total_months = 0
net_total = 0
prev_profit_loss = 0
total_changes = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

# Read the CSV file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header
    header = next(csvreader)
    
    # Loop through each row 
    for row in csvreader:
        # Update the total number of months
        total_months += 1
        
        # Get the profit/loss value for the current row
        current_profit_loss = int(row[1])
        
        # Calculate the net total
        net_total += current_profit_loss
        
        # Calculate the change in profit/loss since the previous row
        if total_months > 1:
            change = current_profit_loss - prev_profit_loss
            total_changes += change
            
            # Check if the change is the greatest increase or decrease
            if change > greatest_increase[1]:
                greatest_increase[1] = change
                greatest_increase[0] = row[0]
            if change < greatest_decrease[1]:
                greatest_decrease[1] = change
                greatest_decrease[0] = row[0]
        
        # Set the current profit/loss as the previous profit/loss for the next iteration
        prev_profit_loss = current_profit_loss

# Calculate the average change
average_change = total_changes / (total_months - 1)

# Print the analysis
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease} ")

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[1]}\n"
    f"Greatest Decrease in Profits: {greatest_decrease[1]}\n")


# Export to text file
with open(text_path, "w") as txt_file:
    txt_file.write(output)
