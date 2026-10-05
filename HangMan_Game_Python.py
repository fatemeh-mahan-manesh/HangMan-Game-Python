PIN = input(
    "Please enter the secret word. (It's case sensitive so please use only lowercase letters for better experience.) : "
)
i = len(PIN)
index = 0
mistake = 0
status = i * "_"
found = False
position = 0
print(f"Now it's your turn to guess : {i*"_"}")
print(r"""
     -------
      |    |
           |
           |
           |
           |
    =========
    """)

while mistake < 6 and status != PIN:
    guess = input(f"Enter the letter of your guess. {6 - mistake} life(s) left : ")

    newstatus = ""
    index = 0
    found = False
    while index < len(PIN):
        if PIN[index] == guess:
            newstatus += guess
            found = True
        else:
            newstatus += status[index]
        index += 1
    status = newstatus
    print(f"Cool! {status} ")

    if found == True:
        print("Good guess! ")
    else:
        print("Don't worry. you can do it.")
        mistake += 1

        if mistake == 1:
            print(r"""
		     -------
		      |    |
		      O    |
		           |
		           |
		           |
		    =========
		    """)
        elif mistake == 2:
            print(r"""
		     -------
		      |    |
		      O    |
		      |    |
		           |
		           |
		    =========
		    """)
        elif mistake == 3:
            print(r"""
		      -------
		       |    |
		       O    |
		     / |    |
		            |
		            |
		    =========
		    """)
        elif mistake == 4:
            print(r"""
		     --------
		      |     |
		      O     |
		    / | \   |
		            |
		            |
		    =========
		    """)
        elif mistake == 5:
            print(r"""
		     --------
		      |     |
		      O     |
		    / | \   |
		     /      |
		            |
		    =========
		    """)
        elif mistake == 6:
            print(r"""
		     --------
		      |     |
		      O     |
		    / | \   |
		     / \    |
		            |
		    =========
		    """)

if status == PIN:
    print("YOU DID IT!")
elif mistake == 6:
    print(f"It's okay. The answer was : {PIN}")
