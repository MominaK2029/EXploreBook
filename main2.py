import streamlit as st
import pandas as pd


st.title("Bookshelf Table")

Eightdf = pd.DataFrame({
    'Title': ["Little Women", "Anne of Green Gables", "A Tree Grows in Brooklyn", "Anne Frank: The Diary of a Young Girl", 'The Catcher in the Rye', "Lord of the Flies", "To Kill a Mockingbird", "From the Mixed-Up Files of Mrs. Basil E. Frankweiler", "A Wizard of Earthsea", "I'll Get There. It Better Be Worth the Trip"],
    'Author': ['Louisa May Alcott', 'L.M. Montgomery', 'Betty Smith', 'Anne Frank', 'J.D. Salinger', 'William Golding', 'Harper Lee', 'E.L. Konigsburg', 'Ursula K. Le Guin', 'John Donovan'],
    'Publish Date': ['1868', '1908', '1943', '1947', '1951', '1960', '50397', '50397', '50437', '50318'],
    'Publisher': [],
    'Genre': [],
    '# of Pages': [],
    'Goodreads Rating': [],
})
Ninedf = pd.DataFrame({
    'Title': ["J. Coughlin", "M. Calkins", "G. Dura", "T. Giaya", 'K. Lauritsen', "R. Magner", "B. Maynard", "M. McCook", "J. Mulcahy", "S. Snay"],
    'Author': ['C409', 'D423', 'B310', 'D420', 'C407', 'B312', 'C417', 'B210', 'D428', 'B212'],
    'Publish Date': ['17580', '50433', '50332', '50432', '50394', '50333', '50397', '50397', '50437', '50318'],
    'Publisher': [],
    'Genre': [],
    '# of Pages': [],
    'Goodreads Rating': [],
})
Twentydf = pd.DataFrame({
    'Title': ["J. Coughlin", "M. Calkins", "G. Dura", "T. Giaya", 'K. Lauritsen', "R. Magner", "B. Maynard", "M. McCook", "J. Mulcahy", "S. Snay"],
    'Author': ['C409', 'D423', 'B310', 'D420', 'C407', 'B312', 'C417', 'B210', 'D428', 'B212'],
    'Publish Date': ['17580', '50433', '50332', '50432', '50394', '50333', '50397', '50397', '50437', '50318'],
    'Publisher': [],
    'Genre': [],
    '# of Pages': [],
    'Goodreads Rating': [],
})


# 2. Add the search bar widget
# Use the [Streamlit text_input documentation](https://docs.streamlit.io/develop/api-reference/widgets/st.text_input) for more parameters.
search_query1 = st.text_input(int("Search Publish year", placeholder="Type here... ex: 1999"))


search_query = st.text_input("Search Genre", placeholder="Type here... ex: Horror")


# 3. Filter data based on input


if search_query1.strip().lower() > 1800:
    if search_query:
        # Filter for rows that contain the search string (case-insensitive)
        filtered_Eightdf = Eightdf[
            Eightdf['Science Teachers'].str.contains(search_query, case=False) |
            Eightdf['Location'].str.contains(search_query, case=False) |
            Eightdf['Extension'].str.contains(search_query, case=False)
        ]
        st.write(f"Results for '{search_query}':")
        st.dataframe(filtered_Eightdf, hide_index=True)
    else:
        st.write("Showing all records:")
        st.dataframe(Eightdf, hide_index=True)


elif search_query1.strip().lower() == "math":
    if search_query:
        #Filter for rows that contain the search string (case-insensitive)
        filtered_Ninedf = Ninedf[
            Ninedf['Math Teachers'].str.contains(search_query, case=False) |
            Ninedf['Location'].str.contains(search_query, case=False) |
            Ninedf['Extension'].str.contains(search_query, case=False)
        ]
        st.write(f"Results for '{search_query}':")
        st.dataframe(filtered_Ninedf, hide_index=True)
    else:
        st.write("Showing all records:")
        st.dataframe(Ninedf, hide_index=True)


elif search_query1.strip().lower() == "history":
    if search_query:
        #Filter for rows that contain the search string (case-insensitive)
        filtered_Twentydf = Twentydf[
            Twentydf['History Teachers'].str.contains(search_query, case=False) |
            Twentydf['Location'].str.contains(search_query, case=False) |
            Twentydf['Extension'].str.contains(search_query, case=False)
        ]
        st.write(f"Results for '{search_query}':")
        st.dataframe(filtered_Twentydf, hide_index=True)
    else:
        st.write("Showing all records:")
        st.dataframe(Twentydf, hide_index=True)


elif search_query1 == "" or search_query1:
    if search_query:
        #Filter for rows that contain the search string (case-insensitive)
        filtered_Eightdf = Eightdf[
            Eightdf['Science Teachers'].str.contains(search_query, case=False) |
            Eightdf['Location'].str.contains(search_query, case=False) |
            Eightdf['Extension'].str.contains(search_query, case=False)
        ]
        filtered_Ninedf = Ninedf[
            Ninedf['Math Teachers'].str.contains(search_query, case=False) |
            Ninedf['Location'].str.contains(search_query, case=False) |
            Ninedf['Extension'].str.contains(search_query, case=False)
        ]
        filtered_Twentydf = Twentydf[
            Twentydf['History Teachers'].str.contains(search_query, case=False) |
            Twentydf['Location'].str.contains(search_query, case=False) |
            Twentydf['Extension'].str.contains(search_query, case=False)
        ]
        st.write(f"Results for '{search_query}':")
        st.dataframe(filtered_Eightdf, hide_index=True)
        st.dataframe(filtered_Ninedf, hide_index=True)
        st.dataframe(filtered_Twentydf, hide_index=True)
    else:
        st.write("Showing all records:")
        st.dataframe(Eightdf, hide_index=True)
        st.dataframe(Ninedf, hide_index=True)
        st.dataframe(Twentydf, hide_index=True)
else:
    st.write("Showing all records:")
    st.dataframe(Eightdf, hide_index=True)
    st.dataframe(Ninedf, hide_index=True)
    st.dataframe(Twentydf, hide_index=True)