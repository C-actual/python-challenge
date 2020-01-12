#Dependencies
import os
import csv

#Bring in CSV
csvpath = os.path.join('Resources','election_data.csv') #no '..' since resources is in same folder
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")
#    for row in csvreader:
#      print(row)


    print("Election Results")
    print("----------------------------------")

#* The total number of votes cast
    tot_vote_count = int(0)
    for row in csvreader:
        tot_vote_count = tot_vote_count + 1
    print(f"Total Votes: {tot_vote_count}")


#* A complete list of candidates who received votes
csvpath = os.path.join('Resources','election_data.csv') #no '..' since resources is in same folder
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    candidate_list = []
    next(csvreader)
    for row in csvreader:
        candidate = str(row[2])
        
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    #print(candidate_list)

#* The total number of votes each candidate won
csvpath = os.path.join('Resources','election_data.csv') #no '..' since resources is in same folder
with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    vote_count_results = []
    percentage_results= []
        
    for name in candidate_list:         
        candidate = name
        #print(candidate)
        csvpath = os.path.join('Resources','election_data.csv') #no '..' since resources is in same folder
        with open (csvpath, newline="") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
#loop through and add votes for candidate 
            vote_count = 0
            percentage = 0
            for row in csvreader:
                if candidate == str(row[2]):
                    vote_count = vote_count + 1 
            #print(vote_count)
                percentage = round(((vote_count / tot_vote_count)*100),3)
            print(f"{candidate}: {percentage}%  ({vote_count})")
            vote_count_results.append(vote_count)
            percentage_results.append(percentage)

    print("----------------------------------")

#* The winner of the election based on popular vote.
    
    results_dict = dict(zip(vote_count_results,candidate_list))
    #print(results_dict)    

    max_votes = max(vote_count_results)
    winner = {results_dict[max_votes]}
    print(f"Winner: {winner}")
    
    print("----------------------------------")

# Export to file 
# I didn't figure this part out ... missed 2 of 3 python lectures and ran out of time looking for it in course materials

# output_one = (f"{candidate_list[1]}  {percentage_results[1]} ({vote_count_results[1]}) ")
# output_two = (f"{candidate_list[2]}  {percentage_results[2]} ({vote_count_results[2]}) ")
# output_three = (f"{candidate_list[3]}  {percentage_results[3]} ({vote_count_results[3]}) ")
# output_four = (f"{candidate_list[4]}  {percentage_results[4]} ({vote_count_results[4]}) ")

# output_path = os.path.join('output.csv')
# with open(output_path, "w", newline="") as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=",")
#     csvwriter.writerow("Election Results:")
#     csvwriter.writerow("----------------------------")
#     csvwriter.writerow(f"Total Votes: {tot_vote_count}")
#     csvwriter.writerow(f"{output_one}")
#     csvwriter.writerow(f"{output_two}")
#     csvwriter.writerow(f"{output_three}")
#     csvwriter.writerow(f"{output_four}")
#     csvwriter.writerow("----------------------------")
#     csvwriter.writerow(f"Winner: {winner}")
#     csvwriter.writerow("----------------------------")


