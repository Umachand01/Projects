import imdb
um=imdb.IMDb()
movie_name=input("enter movies name: ")
movies=um.search_movie(str(movie_name))
index=movies[0].getID()
movie=um.get_movie(index)
title=movie['title']
rating=movie['rating']
year=movie['year']
cast=movie['cast']
list_of_cast=",".join(map(str,cast))
print("tital:-",title)
print("rating:-",rating)
print("relised date:-",year)
print("cast of movie:-",list_of_cast)