#Great work on the first brief! You've done so well, that your boss has asked you to make the recommendation system more complex by using 'or' statements. Afterall, we want to give our Netflix customers lots of choices.

#Step 1: Read the starter code below carefully. 


watched_movies = []                                                                             # It has set up an empty list called 'watched_movies' and given the user a list of movie options.
print("Enter the movies you have watched, one by one. Type 'done' when finished.")
print("Options: Barbie, Oppenheimer, The Godfather, Casablanca, The Matrix, Inception")

while True:                                                                                     #Here, a loop has been set up to take the user's input (movie they have watched) and makes it lowercase.
    movie = input("Movie: ")
    if movie.lower() == 'done':
        break
    if movie in ["Barbie", "Oppenheimer", "The Godfather", "Casablanca", "The Matrix", "Inception"]:
        watched_movies.append(movie)



#Step 2: Use 'if' statements, 'in' and 'or' statements to make recommendations for The Godfather & Casablanca (gangster/romance films), The Matrix & Inception. Barbie and Oppenheimer have already been done as an example.
#Add your code below.

if "Barbie" in watched_movies or "Oppenheimer" in watched_movies:
    if "Barbie" in watched_movies:
        print("You might enjoy 'Legally Blonde' because you like fun and stylish comedies!")
    if "Oppenheimer" in watched_movies:
        print("You might enjoy 'The Imitation Game' because you like historical dramas with deep themes!")




#Step 3: Write an if statement above which prints a statement if none of these movies have been watched.


