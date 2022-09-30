# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

 1. Calculate the total number of votes cast.
 2. Get a complete list of candidates who received votes.
 3. Calcualte the total number of votes each candidate received.
 4. Calculate the percentage of votes each candidate won. 
 5. Determine the winner of the election based on popular vote.
 
 ## Resources
 - Data Source: election_results.csv
 - Software: Python 3.10, Visual Studio Code, 1.71.2
 
 ## Summary
 The analysis of the election show that:
  - There were 369,711 votes cast in the election.
  - The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

   - The candidate results were:
   
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
   
   - The winner of the election is:
   
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
   

   
 ## Challenge Overview

### Overview of Election Audit [^1]
The purpose of this analysis is to provide the election commission with a few additional data points to the complete the audit.
1. The voter turnout for each county.
2. The percentage of votes from each county out of the total.
3. The county with the highest turnout.

Snapshot of code that executes the row counts in order to provide the results in the Election Audit Results section.
![Mod4_Challenge_VoteCounts](https://user-images.githubusercontent.com/112449480/193173105-4ba14924-0010-496d-9c14-b8a2a54c5695.png)

### Election Audit Results
The outcome of the election:
- How many votes were cast in this congressional election?
  - Total Votes: 369,711

![Mod4_Challenge_TotalVotes](https://user-images.githubusercontent.com/112449480/193171259-1e2ad790-de30-4c4d-8904-0652b2c3d9eb.png)

- Breakdown of the number of votes and percentage of total votes for each county in the precinct.
  - County Votes:
    - Jefferson: 38,855 votes; 10.5%
    - Denver: 306,055 votes; 82.8%
    - Araoahoe: 24,801 votes; 6.7%

![Mod4_Challenge_CountyPercentage](https://user-images.githubusercontent.com/112449480/193172328-1192f06c-9e9e-4a62-94c7-5e4975f2c5c5.png)

- Which county had the largest number of votes
  - Denver

![Mod4_Challenge_LargestCounty](https://user-images.githubusercontent.com/112449480/193172396-5d6c8593-9491-497b-bcda-a2a0182f9c6d.png)

- Breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)

![Mod4_Challenge_CandidateVote-Percentage](https://user-images.githubusercontent.com/112449480/193172760-a49cd966-01af-4c91-bc4d-fd6958dccee1.png)

- Which candidate won the election, their vote count and their percentage of the total votes.
  - Winner: Diana Degette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%

![Mod4_Challenge_WinningCandidate](https://user-images.githubusercontent.com/112449480/193172836-0134042b-4631-47e8-83f4-87fa3228248f.png)

## Challenge Summary

### Election Audit Summary
In summary, the script developed for this local congressional election could be modified for other elections, such as mayoral elections, school student body president or gubernatorial election.  For example, the script could be modified to:
- Determine the votes by district
- Determine the votes by county by candidate
- Determine the percentage of total votes by county by candidate
- Determine the number of votes for each student candidate by grade level
    


[^1]: Utilize the Challenge description from Module 3 to assist in writing the Challenge Overview
