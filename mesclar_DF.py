import pandas as pd

# Basic Syntax for Merging DataFrames
# We use the merge() function provided by pandas to combine DataFrames. This function combines two DataFrames and returns a captured DataFrame based on a common or shared column. Here's a general example:

# merged_df = df1.merge(df2, on="common_column", how="inner")

# In this example, abstract df1 and df2 are merged based on a shared or common column. The argument how="inner" denotes this as an inner merge.

# Let's look at specific examples and unpack the four types of merges: inner join, outer join, left join, and right join.

# Dataset
# For this lesson, we will use the following dataset, stored in two separated dataframes:

df_books = pd.DataFrame({
     "Book_ID": [1, 2, 3, 4, 5],
     "Book_Title": ['Gatsby', 'Mockingbird', '1984', 'Catcher', 'LOTR'],
     "Author_ID": [101, 102, 103, None, 112],
     "Genre": ['Fiction', 'Fiction', 'Fiction', 'Fiction', 'Fantasy']
 })

# creating the DataFrame for Authors
df_authors = pd.DataFrame({
    "Author_ID": [101, 102, 103, 104, 105],
    "Author_Name": ['F. Fitzgerald', 'H. Lee', 'G. Orwell', 'J. Salinger', 'J. Tolkien'],
    "Nationality": ['American', 'American', 'British', 'American', 'British']
})

# Two important things to note: The author with Author_ID=112 is missing in the df_authors dataframe The book named Catcher in the df_books dataframe misses info about its author

# Inner Join
# An inner join includes rows where there is a match in both DataFrames. Here's how you can perform an inner join:

# Merge the dataframes - inner merge
merged_df = df_books.merge(df_authors, on="Author_ID", how="inner")
print(merged_df)
'''Output:
   Book_ID   Book_Title  Author_ID    Genre    Author_Name Nationality
0        1       Gatsby      101.0  Fiction  F. Fitzgerald    American
1        2  Mockingbird      102.0  Fiction         H. Lee    American
2        3         1984      103.0  Fiction      G. Orwell     British
'''

# The resultant DataFrame will have only rows with common Author_ID in both dataframes, so we don't include books where author information is missing or undefined.

# Outer Join
# An outer join includes all the rows from both DataFrames and fills NaN for missing values:

# Merge - outer merge
merged_df = df_books.merge(df_authors, on="Author_ID", how="outer")
print(merged_df)
'''Output:
   Book_ID   Book_Title  Author_ID    Genre    Author_Name Nationality
0      1.0       Gatsby      101.0  Fiction  F. Fitzgerald    American
1      2.0  Mockingbird      102.0  Fiction         H. Lee    American
2      3.0         1984      103.0  Fiction      G. Orwell     British
3      4.0      Catcher        NaN  Fiction            NaN         NaN
4      5.0         LOTR      112.0  Fantasy            NaN         NaN
5      NaN          NaN      104.0      NaN    J. Salinger    American
6      NaN          NaN      105.0      NaN     J. Tolkien     British
'''

# All data from both dataframes is included. For any missing data, it has NaN. Note how it includes all the books, even if they miss the author info, and all the authors, even if there is no book info for them.

# Left Join
# A left join includes all rows from the first DataFrame and fills NaN for missing values in the second DataFrame:

# Merge - left merge
merged_df = df_books.merge(df_authors, on="Author_ID", how="left")
print(merged_df)
'''Output:
   Book_ID   Book_Title  Author_ID    Genre    Author_Name Nationality
0        1       Gatsby      101.0  Fiction  F. Fitzgerald    American
1        2  Mockingbird      102.0  Fiction         H. Lee    American
2        3         1984      103.0  Fiction      G. Orwell     British
3        4      Catcher        NaN  Fiction            NaN         NaN
4        5         LOTR      112.0  Fantasy            NaN         NaN
'''

# After a left merge, the resultant DataFrame includes all books, even if they miss the author info.

# Right Join
# A right join includes all rows from the second DataFrame, in reverse to a left join. Here's an example of a right join:

merged_df = df_books.merge(df_authors, on="Author_ID", how="right")
print(merged_df)
'''Output:
   Book_ID   Book_Title  Author_ID    Genre    Author_Name Nationality
0      1.0       Gatsby      101.0  Fiction  F. Fitzgerald    American
1      2.0  Mockingbird      102.0  Fiction         H. Lee    American
2      3.0         1984      103.0  Fiction      G. Orwell     British
3      NaN          NaN      104.0      NaN    J. Salinger    American
4      NaN          NaN      105.0      NaN     J. Tolkien     British
'''

# After a right merge, the resultant DataFrame includes all authors, even if there is no book information for them.