# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#Initialize Program Data
TotalNoVotesCast = 0
maxpos = 0
VoterID = []
County = []
Candidate = []
ListOfCandidate = []
ListOfCandidateCount = []

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

    #Pop the first element of all lists as they are the title and will not match the data set
    VoterID.pop(0)
    County.pop(0)
    Candidate.pop(0)
    
    #Calculate total number of voters from the CSV file
    print(f"Election Results")
    print(f"-------------------------------")
    print(f"Total Votes: {len(VoterID)}")
    print(f"-------------------------------")
    
    #Find the unique list of voting candidates
    for element in Candidate:
        if element not in ListOfCandidate:
            ListOfCandidate.append(element)
    
    
    #Calculating the total votes per candidate and the percentage of vote
    for candidate in ListOfCandidate:
        print(f"{candidate}  {round((Candidate.count(candidate)/len(VoterID)*100), 2)}%   {Candidate.count(candidate)}")
        ListOfCandidateCount.append(Candidate.count(candidate))
        
    print(f"-------------------------------")
    
    #Finding the winning candidate
    maxpos = ListOfCandidateCount.index(max(ListOfCandidateCount)) 
    print(f"Winner: {ListOfCandidate[maxpos]}")
    
    
    # Writing the output to a CSV file
    # Specify the file to write to
    output_path = os.path.join("..", "output", "OutputOfPyPoll.csv") 

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        csvwriter.writerow(['Total Votes:', len(VoterID)])
        
        # Write the next rows
        for candidate in ListOfCandidate:
            csvwriter.writerow([candidate, round((Candidate.count(candidate)/len(VoterID)*100), 2), Candidate.count(candidate)])
    
        # Write the next row
        csvwriter.writerow(['Winner:', ListOfCandidate[maxpos]])
        
    
    
    

   
   
    
