#Netflix now wants to take the customer's reviewed TV shows and tell them their top genre. 
#This will help customers figure out what kinds of shows they like. 

# Step 1: Get user ratings for three TV shows. This has been done for Bridgerton and Friends as examples. Add Stranger Things.

print("Rate the following TV shows from 0 to 5:")

while True:
        rating_bridgerton = int(input("Rating for Bridgerton (Drama/Romance): "))
        if 0 <= rating_bridgerton <= 5:
            break
        else:
            print("Please enter a rating between 0 and 5.")

while True:
        rating_friends = int(input("Rating for Friends (Comedy): "))
        if 0 <= rating_friends <= 5:
            break
        else:
            print("Please enter a rating between 0 and 5.")






# Step 2: Determine the top genre based on the ratings.
# Underneath the print statement create a variable called total_drama_romance which is equal to rating_bridgerton, total_comedy which is equal to rating_friends and total_sci_fi_horror which is equal to rating_stranger_things. 


print("Determining your top genre based on your ratings:")




# Step 3: Determine the top genre. 1) Create an elif statement where if total_comedy is greater than total_drama_romance and total_sci_fi_horror, print that the top genre is comedy. 
# 2) Create an elif statement for if Sci Fi/Horror is the top genre.


if (total_drama_romance > total_comedy) and (total_drama_romance > total_sci_fi_horror):
    print("Your top genre is Drama/Romance!")
  


  
else:
    print("You seem to like multiple genres equally!")


# Extension 1: Can you use floats instead of integers? What if someone inputs 2.5 as a review?

