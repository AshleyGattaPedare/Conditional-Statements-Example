# Netflix wants to allow users to rate a movie they've watched out of 5 (5 being a top score and 0 being a bottom score) and then use the rating to recommend them another movie. 
# They want you to start with Avengers Endgame (just don't tell Disney+).
# There will be some new concepts in this brief such as 'while True' loops (which simply means the code will run/repeat itself infinitely until 'break').


# Step 1: Run the code as it is and see what happens.

# Step 2: As the example below, we have gotten the user rating for "Avengers: Endgame." Add to the code below by asking the user for a rating of 'The Lion King.' 


while True:
        rating_avengers_endgame = int(input("Rate Avengers: Endgame (0 to 5): "))
        if 0 <= rating_avengers_endgame <= 5:
            break
        else:
            print("Please enter a rating between 0 and 5.")
 

# Step 3: As an example below, we have provided recommendations based off of a customer's rating of Avengers Endgame. Underneath, add to the code by giving recommendations based off a customer's rating of 'The Lion King.'


if rating_avengers_endgame >= 3:
    print("You might enjoy 'Guardians of the Galaxy' because you seem to love Marvel movies with action and humor!")
else:
    print("You might enjoy 'Spider-Man: Homecoming' because it's another fun superhero movie!")

  

# Step 4: Go back to step 3 and add an 'elif' statement to the Avengers Endgame recommendations where if the rating is equal to or greater than 1, it recommends DC's Batman.
  

# Extension: What happens if the user puts in '6'? Can you add anything to the code to handle this error?
