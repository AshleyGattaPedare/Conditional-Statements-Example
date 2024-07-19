# Miss Gatta's super secret grade decider pro 3000

bribe_type = input("What did the student bring? (snacks, money, nothing): ").lower()

if bribe_type == "snacks":
    snack = input("What kind of snacks did they bring? (cookies, chips, donuts): ").lower()
    if snack == "cookies":
        print("Cookies for grades! 🍪 They get an A+, because who can resist cookies?")
    elif snack == "chips":
        print("Chips for grades! 🥔 They get a B, because chips are great, but cookies are better.")
    elif snack == "donuts":
        print("Donuts for grades! 🍩 They get an A++, because donuts are the ultimate bribe!")
    else:
        print("Mystery snack! 🍫 They get a C for curiosity and for making me guess.")
