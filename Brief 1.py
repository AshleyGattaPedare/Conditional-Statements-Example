#Step 1: We are going to define a list of recommendations. That's been done for you below.

all_movies = ["The Matrix", "Inception", "Pride and Prejudice", "Titanic"]

# Step 2: We need to find out from the user, what films they have already watched. To do this, create a variable called 'watched_movies' and ask the user to input the movies watched, seperated by commas.

              = input("Enter the movies you have watched, separated by commas (e.g., 'The Matrix, Pride and Prejudice'): ")


# Step 4: Add .split(", ") at the end of that line of code. This, in really simple terms, will seperate the movies listed.


# Step 5: Provide recommendations based on the watched movies. Use if, elif and else statements. The if statement is already there for you as an example.

if "The Matrix" in watched_movies:
    print("You might enjoy 'Inception' because you like Sci-Fi!")
elif "Pride and Prejudice" in watched_movies:
    print("You might enjoy 'Titanic' because you like Romance!")
else:
    print("How about watching 'The Matrix' or 'Pride and Prejudice' for a great start?")

# Step 6: Add an elif statement where you combine two films using 'and.' There's an example below but you need to come up with your own.

#       if "Barbie" in watched_movies and "Oppenheimer" in watched_movies:
#            print("You might enjoy 'The Grand Budapest Hotel' because you appreciate both whimsical and thought-provoking films!")

