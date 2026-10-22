import streamlit as st
import pandas as pd


st.title("BookShelf")

sdf = pd.DataFrame({
    'Science Teachers': ["J. Coughlin", "M. Calkins", "G. Dura", "T. Giaya", 'K. Lauritsen', "R. Magner", "B. Maynard", "M. McCook", "J. Mulcahy", "S. Snay"],
    'Location': ['C409', 'D423', 'B310', 'D420', 'C407', 'B312', 'C417', 'B210', 'D428', 'B212'],
    'Extension': ['17580', '50433', '50332', '50432', '50394', '50333', '50397', '50397', '50437', '50318']
})
# 2. Add the search bar widget
# Use the [Streamlit text_input documentation](https://docs.streamlit.io/develop/api-reference/widgets/st.text_input) for more parameters.
search_query1 = st.text_input("Search Genre", placeholder="Type here... ex: Horror")


search_query = st.text_input("Search Book Name", placeholder="Type here... ex: The Lightning Theif")


# 3. Filter data based on input


if search_query1.strip().lower() == "science":
    if search_query:
        # Filter for rows that contain the search string (case-insensitive)
        filtered_sdf = sdf[
            sdf['Science Teachers'].str.contains(search_query, case=False) |
            sdf['Location'].str.contains(search_query, case=False) |
            sdf['Extension'].str.contains(search_query, case=False)
        ]
        st.write(f"Results for '{search_query}':")
        st.dataframe(filtered_sdf, hide_index=True)
    else:
        st.write("Showing all records:")
        st.dataframe(sdf, hide_index=True)

elif search_query1 == "" or search_query1:
    if search_query:
        #Filter for rows that contain the search string (case-insensitive)
        filtered_sdf = sdf[
            sdf['Science Teachers'].str.contains(search_query, case=False) |
            sdf['Location'].str.contains(search_query, case=False) |
            sdf['Extension'].str.contains(search_query, case=False)
        ]
        st.write(f"Results for '{search_query}':")
        st.dataframe(filtered_sdf, hide_index=True)
    else:
        st.write("Showing all records:")
        st.dataframe(sdf, hide_index=True)
else:
    st.write("Showing all records:")
    st.dataframe(sdf, hide_index=True)