# imports of packages to be used in functions
 
import pandas as pd
import numpy as np

# Data loading and preprocessing. Electricification by province (EBP) data


ebp_df = pd.read_csv('https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv')

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.head()

# Twitter data
twitter_df = pd.read_csv('https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv', index_col= None)
twitter_df.head()
 
# Important Variables (Do not edit these!)

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

### START FUNCTION ONE 
def dictionary_of_metrics(items):
    """
    Calculates the mean,median,standard deviation,variance,minumum value and maximum value
    
    Args:
        items(list):list object containing numerical values.
    
    Returns:
        dictionary: mean,median,standsrd deviation,variance,minumun value, and maximum value.
        
    Examples:
        >>> dictionary_of_metrics([2,4,6,8,10])
          dictionary_of_metric={'max': 10,
                                'mean': 6.0,
                                'median': 6.0,
                                'min': 2,
                                'standard deviaion': 2.82,
                                'variance': 8.0}
    """                            
    mean = np.mean(items)
    median = np.median(items)
    std = np.std(items, ddof=1)
    var = np.var(items,ddof =1)
    min = np.min(items)
    max= np.max(items)
    
    dictionary_of_metrics = {'mean': round (mean,2),
               'median': round (median,2),
               'var': round (var,2),
               'std': round (std,2),
               'min': round (min,2),
               'max': round (max,2)}
    
    return dictionary_of_metrics
### END FUNCTION ONE 

### START FUNCTION TWO
def five_num_summary(items):

    '''
    summary: five number summary of each of the respective proviences Electricification
    
    Args: list of the Electricification by province (EBP) per year items(string) = column header associated to the respective provience 
    
    returns:creates a dictionairy of a five number summary ('25%': 'q1','50%':'median','75%':'q3')
    
    Egs:
         five_num_summary(gauteng) == {
                                        'max': 39660.0,
                                      'median': 24403.5,
                                         'min': 8842.0,
                                         'q1': 18653.0,
                                         'q3': 36372.0
                                                          }
    '''
    x = pd.DataFrame(items, columns=['values'])
    item_stat = x.describe()
    item_stat_label = item_stat.rename(index= {'25%': 'q1','50%':'median','75%':'q3'})
    five_sum = item_stat_label.loc[['min','q1','median','q3','max']]
    five_sum_dict = five_sum.to_dict()
    
    return five_sum_dict['values']  
### END FUNCTION  TWO

### START FUNCTION THREE
def date_parser(dates):

    '''
    summary: The function takes a list of tweet dates times strings and changes the format as stated below
    
    args:  list is formatted as 'yyyy-mm-dd hh:mm:ss'. arg type (string) dates 
    
    return: a list of strings where each element in the list is returned as a list that contains only the date in the 'yyyy-mm-dd' format.
    
    Egs: date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
    
    """
    '''
    return [i.split(' ')[0] for i in dates]
### END FUNCTION THREE

### START FUNCTION FOUR
def extract_municipality_hashtags(df):

    '''    
    summary: The functions extracts the hashtags from the tweets in the twitter dataframe and creates a new column with the hashtags from the corresponding tweets in list form
    
    Args: The twitter dataframe type(DataFrame)
    
    return: a new twitter dataframe with a hashtags columns listing the hashtages of the correspeonding tweets 
    
    egs: see note book for more comprehesive look 
    
    Tweeet: column
     value:   '#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPENDS PLANNED ELECTRICITY SUPPLY INTERRUPTIONS TO \nMANGAUNG METROPOLITAN
    hashtag: column
     value:   [#ESKOMFREESTATE, #MEDIASTATEMENT] 
    

    '''
   
    for city_key in mun_dict.keys():
        
        df.loc[df['Tweets'].str.contains(pat = city_key),'municipality'] = mun_dict[city_key]
        
        df.loc[df['Tweets'].str.contains(pat = '#'),'hashtags'] = list(pd.Series(df['Tweets'].str.extractall('(#w+)').unstack().values.tolist()).apply(lambda x :
                                                                                                                                                      [y.lower() for y in x if str(y) != 'nan']))
    return df
### END FUNCTION FOUR

### START FUNCTION FIVE
def number_of_tweets_per_day(df):

    '''
    summary: This function counts the number of tweets per day from the twitter dataframe 
    
    Args: The input is a dataframe  (twitter dataframe)
    
    return: It returns a new df with a date index labled dates and a column of the number of tweets per date
    
    Egs:
    	                  Tweets
            Date	
       2019-11-20	      18  
       2019-11-21	      11
       2019-11-22	      25
       2019-11-23	      19
       2019-11-24	      14
       2019-11-25      	20
       2019-11-26	      32
       2019-11-27	      13
       2019-11-28      	32
       2019-11-29	      16
    
    '''
  
  
    df['Date'] = [i.split(' ')[0] for i in df['Date']]
    
    return df.groupby('Date').count()
### END FUNCTION FIVE

### START FUNCTION SIX
def word_splitter(df):

    '''  
    summary: this function takes (dataframe) the twitter dataframe specfically the tweets column and splits the tweets into a list of words 
    
    Args:  a dataframe in this case the twitter df 
    
    Return: new column added to the orginal dataframe with a list of individual words sperated where seperated by a spaces
    
    Egs: See notebook 
    
    
    '''
    df['Split Tweets'] = df['Tweets'].str.lower().str.split() #Tokenization
    
    return df
### END FUNCTION SIX

### START FUNCTION SEVEN
def stop_words_remover(df):

    '''
    summary:  Takes in the twitter dataframe and creates a new column called stop words that has extracted the specfic words mentioned 
              in the dictionary 'stop words'
    
    Args: The twitter df
    
    return: the new twitter df with an appended column called 'with out stop words' that have values, lists of strings not containing the 
            stop words listed in the dictionary. see notebook for tabulated example 
    
    egs:
    stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"] == 
    ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'supply', 'interruption', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit']
    '''
    df['Without Stop Words']= df['Tweets'].str.lower().str.split() #Tokenization as in func 6
    
    df['Without Stop Words']= df['Without Stop Words'].apply(lambda x : [i for i in x if i not in stop_words_dict['stopwords']])
    
    return df
### END FUNCTION SEVEN
