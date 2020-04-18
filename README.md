# Python-Challenge #
Data analysis on financial records and polls for election

## Bank Analysis ##

### Assumption ###
  * Cut off dates were constant for the record and there are no overlaps on expenditures or profits every month
  * Company was well past stabilization period where the monthly profit/loss can be compared

### Goal ###
  Create a Python script for analyzing the financial records a company given the profit/losses per month. 
  
### Method of Analysis ###
  Using python, open the company financial records in CSV file to access the monthly profit/loss data.
  
  While looping through each month, calcuate the change in profit/loss every next month, then print out the following results:
   * The total number of months included in the dataset
   * The net total amount of "Profit/Losses" over the entire period
   * The average of the changes in "Profit/Losses" over the entire period
   * The greatest increase in profits (date and amount) over the entire period
   * The greatest decrease in losses (date and amount) over the entire period
     
### Conclusion ###
  Within the 86 months of the analysis, company made a total profit of $38,382,578. Although the company made a profit, general trend of negative acerage change shows that it has been doing worse. Looking at the data more in depth, I can also see that the change value is very random and does not have a trend. This leads me believe that company is not dependent on season and that it has not found its stable source of income. The most profitable and least profitable months will not be at much of use for the overview of the company analysis. 
  
  If this was to be presented, I would do deeper analysis on months that were highly profitable and find the commonality the company should focus on.
  
  
## Poll Analysis ##

### Assumption ###
  * No Typos are made
  * There aren't dupplicates of voter ID
  * All candidates have different last name
  * Race is complete
  
### Goal ###
  Create a Python script to analyze the results of a voting between multiple candidates in a rural town. 
  
### Method of Analysis ###
  Using python, open the company poll records in CSV file to access the voting information.
  
  While looping through each iterations, count the followings:
    * The total number of votes cast
    * A complete list of candidates who received votes
    * The percentage of votes each candidate won
    * The total number of votes each candidate won
    * The winner of the election based on popular vote.
    
### Conclusion ###
  Following the assumption made, winner of this race is Khan. Khan won it by landslide of 63% and the next up candidate following by 20%
