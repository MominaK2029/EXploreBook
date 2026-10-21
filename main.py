import csv
# comma separate value

with open("YA_Books.csv", mode = "r", encoding="utf-8") as bookfile:
    # Mode  r means read
    # as file means alias/nickname 

    books = csv.reader(bookfile)
    # Skip header row
    next(books)
    
    # author col is at index 1
    minrating = 5 
    max_year = 0 
    max_rating = 5
    for row in books:
    #     print authors with letter 'M'
    #     if row[1].startswith("M"):
    #         print(row[1])

     #     Print out last name
    #     authorname = row[1]
    #     lastindex = authorname.rfind(" ")
    #     lastname = authorname[lastindex + 1 :]
    # if lastname.startswith("J"):
    #     print(authorname)

         #find most_recenbook (highest)
        year = int(row[2])
        if max_year < year:
            max_year = year
            most_recent_book = row


        # Book with the worst rating
        rating = float(row[6])
        if minrating > rating:
            minrating = rating
            worstbook = row

    # Longest book publshed before 2000
        if year < 2000:
            pages = int(row[5])
            if pages > 100:
                longestbook = row
    print(f"The longest book before the 2000s: {longestbook}")
    print(f"Most recent book: \n{most_recent_book}")
    print(f"The worst book: \n {worstbook}")
            
         
    # # Highest rated over 100 pages
    if pages > 100:
        if rating > minrating:
            rating <= max_rating
            highestrated = row
    print(f"The highest rated book with over 100 pages: {highestrated}")
