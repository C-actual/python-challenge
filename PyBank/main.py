#PyBank main.py
#* Your task is to create a Python script that analyzes the records to calculate each of the following:

#Import dependencies
import os
import csv

#Pull in and Read CSV
csvpath = os.path.join('Resources','budget_data.csv') # Removed '..' since resources is in same folder
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#    print(csvreader)

#    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

#    for row in csvreader:
#      print(row)
   
    print("Financial Analysis")
    print("---------------------------")




# * The total number of months included in the dataset
#Pull in and Read CSV
csvpath = os.path.join('Resources','budget_data.csv') # Removed '..' since resources is in same folder
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')   
    
    #Clear Var and skip header row
    months = int(0)
   
    next(csvreader)
    for row in csvreader:
      months = months + 1   
    print(f"Total Months:{months}")



#* The net total amount of "Profit/Losses" over the entire period
#Pull in and Read CSV
csvpath = os.path.join('Resources','budget_data.csv') # Removed '..' since resources is in same folder
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')   
    
    #Clear Var and skip header row
    running_total = int(0)
    next(csvreader)

    for row in csvreader:
      running_total = running_total + int(row[1])     
    print(f"Total: ${running_total}")
    TM_OP = str(f"Total: ${running_total}")






#* The average of the changes in "Profit/Losses" over the entire period
#Pull in and Read CSV
csvpath = os.path.join('Resources','budget_data.csv') # Removed '..' since resources is in same folder
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')   
    
    #Set vars
    average = int(0)
    this_num = int(0)
    last_num = int(867884)  #This is a hack b/c I couldn't figure out how to reference the right  
                            #number to start, it always referenced the very last number in the file... whoops
    change = int(0)
    monthly_change_list =[]

    #To start on correct line
    next(csvreader)
    next(csvreader)
  
    for row in csvreader:
      this_num = int(row[1])
      change = this_num - last_num
      monthly_change_list.append(change)
#      print(change)
      last_num = this_num

    average = round(sum(monthly_change_list)/len(monthly_change_list),2)
    print(f"Average Change: ${average}")
    AC_OP = str(f"Average Change: ${average}")
    
  






#* The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(monthly_change_list)
    greatest_increase_month =str("text")

#Pull in and Read CSV
csvpath = os.path.join('Resources','budget_data.csv') # Removed '..' since resources is in same folder
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')   
    
    #Set vars
    this_num = int(0)
    last_num = int(867884)  #This is a hack b/c I couldn't figure out how to reference the right  
                            #number to start, it always referenced the very last number in the file... whoops
    change = int(0)

    #To start on correct line
    next(csvreader)
    next(csvreader)
  
    for row in csvreader:
      this_num = int(row[1])
      change = this_num - last_num
      if change == greatest_increase:
        greatest_increase_month = str(row[0])
      last_num = this_num
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    GI_OP = str(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")



#* The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(monthly_change_list)
    greatest_decreaes_month =str("text")

#Pull in and Read CSV
csvpath = os.path.join('Resources','budget_data.csv') # Removed '..' since resources is in same folder
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')   
    
    #Set vars
    this_num = int(0)
    last_num = int(867884)  #This is a hack b/c I couldn't figure out how to reference the right  
                            #number to start, it always referenced the very last number in the file... whoops
    change = int(0)

    #To start on correct line
    next(csvreader)
    next(csvreader)
  
    for row in csvreader:
      this_num = int(row[1])
      change = this_num - last_num
      if change == greatest_decrease:
        greatest_decrease_month = str(row[0])
      last_num = this_num
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
    GD_OP = str(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


#* As an example, your analysis should look similar to the one below
 # ```text
  #Financial Analysis
  #----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results. """
    output_path = os.path.join('output.csv')
    with open(output_path, "w", newline="") as csvfile:
      csvwriter = csv.writer(csvfile, delimiter=',')
      csvwriter.writerow([TM_OP])
      csvwriter.writerow([AC_OP])
      csvwriter.writerow([GI_OP])
      csvwriter.writerow([GD_OP])

      
      