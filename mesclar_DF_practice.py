import pandas as pd

# creating the DataFrame for Books
df_publisher = pd.DataFrame({
    "Publisher_ID": [201, 202, None, 204, None],
    "Book_ID": [1, 2, 3, None, 5],
    "Publisher_Name": ['Penguin', 'HarperCollins', 'Hachette', None, 'Random House']
})

# creating the DataFrame for Books
df_books = pd.DataFrame({
     "Book_ID": [1, 2, 3, 4, 5],
     "Book_Title": ['Gatsby', 'Mockingbird', '1984', 'Catcher', 'LOTR']
 })

# Merge the dataframes - left merge
merged_df_left = df_books.merge(df_publisher, on="Book_ID", how="left")
print("After the left join:")
print(merged_df_left)

# Merge the dataframes - inner merge
merged_df_inner = df_books.merge(df_publisher, on="Book_ID", how="inner")
print("After the inner join:")
print(merged_df_inner)

# creating the DataFrame for Books
df_books = pd.DataFrame({
    "Book_ID": [id + 1 for id in range(6)],
    "Book_Title": ['The Secret Garden', 'The Little Prince', 'Harry Potter', 'Hobbit', 'LOTR', '1984'],
    "Author_ID": [201, 202, 203, 204, 205, None],
    "Genre": ['Fiction', 'Fiction', 'Fantasy', 'Fantasy', 'Fantasy', 'Fiction']
})

# creating the DataFrame for Authors
df_authors = pd.DataFrame({
    "Author_ID": [201, 202, 203, 204, 205],
    "Author_Name": ['Frances Hodgson Burnett', 'Antoine de Saint-Exupéry', 'J.K. Rowling', 'J.R.R. Tolkien', 'George Orwell'],
    "Nationality": ['British', 'French', 'British', 'British', 'British']
})

# We want to change the merge method such that all books, including those with missing author info, are included in the final merged DataFrame.
mod_merged_df = df_books.merge(df_authors, on="Author_ID", how="outer")
print(mod_merged_df)

df_book_units = pd.DataFrame({
    "Book_ID": [1, 2, 3, 4, 5],
    "Units_Sold": [5000, 3500, 12000, 8000, 4000]
})

df_book_info = pd.DataFrame({
    "Book_ID": [1, 2, 3, 4, 6],
    "Book_Title": ['Smart Investing', 'Financial Freedom', 'Retire Young', 'Money: Master the Game', 'Think Rich'],
})

merged_df = df_book_units.merge(df_book_info, on="Book_ID", how="inner")
print(merged_df)

df_books = pd.DataFrame({
     "Book_ID": [1, 2, 3, 4, 5],
     "Book_Title": ['Gatsby', 'Mockingbird', '1984', 'Catcher', 'LOTR'],
     "Author_ID": [101, 102, 103, None, 112],
     "Genre_ID": [1, 1, 3, 1, 2]
 })

df_genre = pd.DataFrame({
    "Genre_ID": [1, 2, 4],
    "Genre_Name": ['Fiction', 'Fantasy', 'Detective']
})

# TODO: Merge df_books and df_genre on the common "Genre" column. Include books that have information about their genre. Do not include genres that don't have any books.

merged_df = pd.merge(df_books, df_genre, on='Genre_ID', how='inner')
print(merged_df)

TODO: Define the dataframe df_books with columns: Book_ID, Book_Title, Author_ID, Genre

df_books = pd.DataFrame({
    "Book_ID": [101, 201, 301, 401, 501],
    "Book_Title": ['Harry Potter', 'Mockingbird', '1984', 'Catcher', 'LOTR'],
    "Author_ID": [1, 2, None, 4, None],
    "Genre": ['Ficção Infantil', 'Fiction', 'Fiction', 'Fiction', 'Fantasy']
})

# TODO: Define the dataframe df_authors with columns: Author_ID, Author_Name
df_authors = pd.DataFrame({
    "Author_ID": [1, 2, 3, 4, 5],
    "Author_Name": ['J.K. Rowling', 'H. Lee', 'G. Orwell', 'J. Salinger', 'J. Tolkien']
})
# TODO: Merge df_books and df_authors on the Author_ID, save the result in merged_books_df

merged_books_df = df_books.merge(df_authors, on="Author_ID", how="left")

# TODO: Print the merged dataframe

print(merged_books_df)

# The mission was to merge df_books with df_authors, ensuring we keep all the books, even if their author information is missing.