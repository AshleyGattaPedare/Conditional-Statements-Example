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

elif bribe_type == "money":
    amount = int(input("How much money did they offer? (enter amount): "))
    if amount >= 100:
        print("Rich with bribes! 💵 They get an A+++, but only if they promise to share!")
    elif amount >= 50:
        print("Generous bribe! 💸 They get an A, but let's keep it a secret.")
    elif amount >= 10:
        print("Modest bribe! 💰 They get a B, because every little bit helps.")
    else:
        print("Small bribe! 💳 They get a C, but thanks for the effort.")
else:
    print("No bribes, no snacks! 🍎 They get a standard grade based on their actual work.")
