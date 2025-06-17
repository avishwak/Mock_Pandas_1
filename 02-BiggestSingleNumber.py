# Problem  2: Biggest single number (https://leetcode.com/problems/biggest-single-number/)

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    biggest_num = my_numbers.groupby('num').filter(lambda x: len(x) ==1 ).max()
    return pd.DataFrame(biggest_num, columns=['num'])

# silution 2

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame to keep only rows where 'num' appears exactly once
    single_numbers = my_numbers[my_numbers.duplicated('num', keep=False) == False]
    max_number = single_numbers['num'].max()
    return pd.DataFrame({'num': [max_number]})

# solution 3
def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:

    counts = my_numbers['num'].value_counts()
    single_numbers = counts[counts == 1].index
    if single_numbers.empty:
        return pd.DataFrame({'num': [None]})
    max_single_number = max(single_numbers)
    return pd.DataFrame({'num': [max_single_number]})