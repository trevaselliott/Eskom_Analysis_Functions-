# Eskom group 8:

This collection of several functions allow for the creation of a insightfull statistics, data cleaning . this creates the ability  to extract meaningfull insight into the current eskom problem: 

See note book for addional exmple: group 08 EskomProject.ipyb

required packages: numpy and pandas 

The Data is from:
Electricification by province (EBP):'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
Twitter Data: 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'

The functions are as follows and provide the following statistics and or data cleanup: 
function 1:  
    summary: statistics on Electricification by province (EBP){ 'mean', 'median', 'std', 'var', 'min', and 'max'}
    
 Function 2: 
    summary: five number summary of each of the respective proviences Electricification
    
 Function 3: 
    summary: The function takes a list of tweet dates, times strings 'yyyy-mm-dd hh:mm:ss' and changes the format to 'yyyy-mm-dd hh'
 
 Function 4: 
    summary: The functions extracts the hastags from the tweets in the twitter dataframe and creates a new table with an extracted          hashtags column 
    
Function 5: 
    summary: This function counts the number of tweets per day from the twitter dataframe and creates a datframe with the respective dates and corresponding count 
    
Function 6: 
    summary: This function takes the twitter dataframe specfically the tweets column and splits the tweets into a list of words and appends the column
    
Function 7: 
    summary:  Takes in the twitter dataframe and creates a new column called stop words that has extracted the specfic words mentioned 
              in the dictionary 'stop words'
              
              
 
 
