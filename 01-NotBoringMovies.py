# Problem 1: Not boring movies (https://leetcode.com/problems/not-boring-movies/)

import pandas as pd
def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema[(cinema['id']%2!=0) & (~cinema['description'].str.contains('boring'))].sort_values(by=['rating'], ascending=False)
    return cinema