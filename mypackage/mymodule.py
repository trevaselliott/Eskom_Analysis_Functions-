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

    '''Returns a dictionary of the five number summary
       Takes in a list of integers, items
       Round all numeric values to two decimal places
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

    '''Takes dates variable (created at the top), which is a list of dates represented as strings
       Date is in 'yyyy-mm-dd' and hh:mm:ss format
       Returns only the date in 'yyyy-mm-dd' format
    '''
    return [i.split(' ')[0] for i in dates]
### END FUNCTION THREE

### START FUNCTION FOUR
def extract_municipality_hashtags(df):

    ''' Takes in a pandas dataframe 
        Extract the municipality from a tweet using the mun_dict
        Insert the result into a new column named 'municipality' in the same dataframe
        Use the entry np.nan when a municipality is not found
        Extract a list of hashtags from a tweet into a new column named 'hashtags' in the same dataframe
        Use the entry np.nan when no hashtags are found
        Returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet
    '''
   
    for city_key in mun_dict.keys():
        
        df.loc[df['Tweets'].str.contains(pat = city_key),'municipality'] = mun_dict[city_key]
        
        df.loc[df['Tweets'].str.contains(pat = '#'),'hashtags'] = list(pd.Series(df['Tweets'].str.extractall('(#w+)').unstack().values.tolist()).apply(lambda x :
                                                                                                                                                      [y.lower() for y in x if str(y) != 'nan']))
    return df
### END FUNCTION FOUR

### START FUNCTION FIVE
def number_of_tweets_per_day(df):

    '''Calculates the number of tweets that were posted per day
       Takes a pandas dataframe as input
       The index of the new dataframe is named Date
       The column of the new dataframe is named 'Tweets', corresponding to the date and number of tweets, respectively
       Date object is formated as yyyy-mm-dd
       Return a new dataframe, grouped by daY, with the number of tweets for that day.
    '''
    df['Date'] = [i.split(' ')[0] for i in df['Date']]
    
    return df.groupby('Date').count()
### END FUNCTION FIVE

### START FUNCTION SIX
def word_splitter(df):

    ''' Splits the sentences in a dataframe's column into a list of the separate words 
        and place the result into a new column named 'Split Tweets'
        The resulting words are lowercases!
        Takes a pandas dataframe as an input
        DataFrame contain a column, named 'Tweets'
        Modify the input dataframe directly
        Return the modified dataframe.   
    '''
    df['Split Tweets'] = df['Tweets'].str.lower().str.split() #Tokenization
    
    return df
### END FUNCTION SIX

### START FUNCTION SEVEN
def stop_words_remover(df):

    ''' Removes english stop words from a tweet
        Takes a pandas dataframe as input
        Tokenise the sentences according to the definition in function 6
        Remove all stop words in the tokenised list
        Stopwords are defined in the stop_words_dict variable defined at the top
        Resulting tokenised list is placed in a column named "Without Stop Words"
        Modify the input dataframe
        Return the modified dataframe
    '''
    df['Without Stop Words']= df['Tweets'].str.lower().str.split() #Tokenization as in func 6
    
    df['Without Stop Words']= df['Without Stop Words'].apply(lambda x : [i for i in x if i not in stop_words_dict['stopwords']])
    
    return df
### END FUNCTION SEVEN
