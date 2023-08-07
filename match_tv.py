#בס"ד
#todo:get movie from client, get info about the movie ,get players categories creatores and more ,return also players creators movie at same category
from bs4 import BeautifulSoup
import requests
import imdb
# creating an instance of the IMDB()
ia = imdb.IMDb()
# Using the Search movie method

#BASEURL="https://www.imdb.com/"
#SERCHURL=BASEURL+"find/?s=all&q="
def count_unique_ids(arr):
    unique_ids = {}
    for id in arr:
        if id in unique_ids:
            unique_ids[id] += 1
        else:
            unique_ids[id] = 1

    unique_list = [{'id': id, 'count': count} for id, count in unique_ids.items()]

    # Sort the unique_list based on the 'count' value in descending order.
    sorted_unique_list = sorted(unique_list, key=lambda x: x['count'], reverse=True)

    return sorted_unique_list

def remove_movie_id(arr,movieid):
    i=0
    for id in arr:
        if "0"+movieid is id:
            arr.pop(i)
        i+=1
    return arr
def calculate_matching_percentage(movie, max_appearances, max_year):
    # Define weights for each parameter (adjust as needed).
    weight_category = 0.4
    weight_appearances = 0.3
    weight_year = 0.3

    # Extract movie details.
    category = movie['category']
    appearances = movie['count']
    year = movie['year']

    # Normalize parameters to a scale of 0 to 1.
    norm_category = category / 10  # Assuming categories are integers from 1 to 10.
    norm_appearances = appearances / max_appearances
    norm_year = (max_year - year) / max_year

    # Calculate the weighted average.
    weighted_average = (
        weight_category * norm_category +
        weight_appearances * norm_appearances +
        weight_year * norm_year
    )

    # Calculate the matching percentage (scaled to 0-100).
    matching_percentage = round(weighted_average * 100)

    # Ensure the matching percentage is within the valid range.
    matching_percentage = max(0, min(100, matching_percentage))

    return matching_percentage


def get_info(MOVIE):
    #todo:get info from imdb and return description name type year rating time and more
    movies = ia.search_movie(MOVIE)
    movie=movies[0]
    movieID=movie.movieID
    data=movie.data
    title=data["title"]
    year=data["year"]
    kind=data["kind"]
    coverimgurl=data["cover url"]
    return movieID,title,year,kind,coverimgurl

def get_series_info(movieid):
    data=ia.get_episode(movieid).data
    rating=data["rating"]
    genres=data['genres']
    languages=data['languages']
    seasons=data['seasons']
    detailes=data["plot"]
    return rating,genres,languages,seasons,detailes

def get_cast_and_creators(movieid):
    data = ia.get_episode(movieid).data
    cast=data["cast"]
    writer=data['writer']

    return cast,writer

def get_cast_and_creators_movie(movieid):
    data = ia.get_movie(movieid).data
    cast=data["cast"]
    writer=data['writer']

    return cast,writer

def get_movies_info(movieid):
    data=ia.get_movie(movieid).data
    rating=data["rating"]
    genres=data['genres']
    languages=data['languages']

    detailes=data["plot"]
    return rating,genres,languages,detailes



movieorseries=input("Please enter a movie or series to find a new series or movie in the same style\n")

print("getting first info")
info = (get_info(movieorseries))
if "series" in info[3]:
    movieid = int(info[0])
    print("get movie id and start search cast,creators and more information")
    info2 = get_series_info(movieid)
    cast = get_cast_and_creators(movieid)
    ALLMOVIES=[]
    directors = cast[1]
    cast = cast[0]
    print("get movie data")
    daata = ia.get_movie(movieid).data
    kind = (daata["kind"])
    categories = (daata['genres'])
    MAXPLAYERCOUNTFORGOODTIME = 15
    COUNTPLAYERS = 0
    print("Get movies by director")
    for director in directors:
        personID = director.personID
        if personID:
            print(f"get all movies for {personID}")
            titlesRefs = ia.get_person(int(personID)).titlesRefs
            json_items = list(titlesRefs.items())
            for i in range(len(json_items)):

                data = json_items[i][1].data
                movieID = json_items[i][1].movieID
                print(f"join this move id to the data {movieID}")
                ALLMOVIES.append(movieID)
                # title = data["title"]
                # kind = data["kind"]
                # print(movieID,title,kind)
    print("Get movies by players")
    for player in cast:
        personID = player.personID
        if COUNTPLAYERS<=MAXPLAYERCOUNTFORGOODTIME:
            if personID:
                print(f"get all movies for {personID}")
                titlesRefs = ia.get_person(int(personID)).titlesRefs
                json_items = list(titlesRefs.items())
                for i in range(len(json_items)):
                    data = json_items[i][1].data
                    movieID = json_items[i][1].movieID
                    print(f"join this move id to the data {movieID}")

                    ALLMOVIES.append(movieID)
                    title = data["title"]
                    kind = data["kind"]
                    # print(movieID,title,kind)
        COUNTPLAYERS+=1
    fullinfo = []
    print("modify all movies id")
    ALLMOVIES=(count_unique_ids(ALLMOVIES))
    top10moovies=[]
    TENNOTepisode = 10  # Initial value for the loop size
    i = 0
    COUNTMOVIES=0
    print("start getting data about the best 10 movies")
    while i < TENNOTepisode:
        if i != 0:

            data = ia.get_movie(ALLMOVIES[i]["id"]).data
            title = (data['localized title'])
            kind = (data.get("kind"))
            print(f"check details about this {kind}-{title}")

            if kind==None:
                kind="episode"
            if kind == "episode":
                #print("skip on episode")
                TENNOTepisode += 1  # Increase loop size if kind=="episode"
            else:
                #print("find movie or series")
                if COUNTMOVIES==10:
                    break
                matchgeners = 0
                geners = (data['genres'])
                for cat in categories:
                    for gen in geners:
                        if cat == gen:
                            matchgeners += 1
                jsontag = {
                    "title": title,
                    "type": kind,
                    "matchgen": fr"{matchgeners}-{len(categories)}".replace("-", " of "),
                    "count": ALLMOVIES[i]["count"],
                    "id": ALLMOVIES[i]["id"]
                }
                top10moovies.append(jsontag)
                COUNTMOVIES+=1
        i += 1
    print("find the top 10 movies")
    for inf in info:
        fullinfo.append(inf)
    for inf2 in info2:
        fullinfo.append(inf2)
    print(top10moovies)


elif "movie" in info[3]:
    movieid = int(info[0])
    print("get movie id and start search cast,creators and more information")
    info2 = get_movies_info(movieid)
    cast = get_cast_and_creators_movie(movieid)
    ALLMOVIES=[]
    print("get movie data")
    daata=ia.get_movie(movieid).data
    kind=(daata["kind"])
    categories=(daata['genres'])
    directors = cast[1]
    cast = cast[0]
    MAXPLAYERCOUNTFORGOODTIME=15
    COUNTPLAYERS=0
    print("Get movies by director")

    for director in directors:
        personID = director.personID
        if personID:
            print(f"get all movies for {personID}")
            titlesRefs = ia.get_person(int(personID)).titlesRefs
            json_items = list(titlesRefs.items())
            for i in range(len(json_items)):
                data=json_items[i][1].data
                movieID = json_items[i][1].movieID
                print(f"join this move id to the data {movieID}")
                ALLMOVIES.append(movieID)
                #title = data["title"]
                #kind = data["kind"]
                #print(movieID,title,kind)
    print("Get movies by players")
    for player in cast:
        personID = player.personID
        print(f"get all movies for {personID}")

        if COUNTPLAYERS<=MAXPLAYERCOUNTFORGOODTIME:
            if personID:
                titlesRefs = ia.get_person(int(personID)).titlesRefs
                json_items = list(titlesRefs.items())
                for i in range(len(json_items)):
                    data = json_items[i][1].data
                    movieID = json_items[i][1].movieID
                    print(f"join this move id to the data {movieID}")
                    ALLMOVIES.append(movieID)
                    title = data["title"]
                    kind = data["kind"]
                    # print(movieID,title,kind)
        COUNTPLAYERS+=1
    fullinfo = []
    print("modify all movies id")
    ALLMOVIES = (count_unique_ids(ALLMOVIES))
    top10moovies = []
    TENNOTepisode = 10  # Initial value for the loop size
    i = 0
    COUNTMOVIES = 0
    print("start getting data about the best 10 movies")
    while i < TENNOTepisode:
        if i != 0:

            data = ia.get_movie(ALLMOVIES[i]["id"]).data
            title = (data['localized title'])
            kind = (data.get("kind"))
            print(f"check details about this {kind}-{title}")

            if kind == None:
                kind = "episode"
            if kind == "episode":
                # print("skip on episode")
                TENNOTepisode += 1  # Increase loop size if kind=="episode"
            else:
                # print("find movie or series")
                if COUNTMOVIES == 10:
                    break
                matchgeners = 0
                geners = (data['genres'])
                for cat in categories:
                    for gen in geners:
                        if cat == gen:
                            matchgeners += 1
                jsontag = {
                    "title": title,
                    "type": kind,
                    "matchgen": fr"{matchgeners}-{len(categories)}".replace("-", " of "),
                    "count": ALLMOVIES[i]["count"],
                    "id": ALLMOVIES[i]["id"]
                }
                top10moovies.append(jsontag)
                COUNTMOVIES += 1
        i += 1
    print("find the top 10 movies")
    for inf in info:
        fullinfo.append(inf)
    for inf2 in info2:
        fullinfo.append(inf2)
    print(top10moovies)
#todo:get arr what twice and more filter category
