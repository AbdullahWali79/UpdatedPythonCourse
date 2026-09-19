import random

# 1. Agay aane waale naye random words ki list
words_pool = ["PYTHON","isi" "ROBOT", "SPACE", "LAPTOP", "the action", "CYBERcrime"]

# Shuruat mein pehla word aapka naam hoga
secret_word = "HACKER MUHAMAD ABDULLAH BHATTI"

print("--- WELCOME CHIEF COMMANDER MUHAMAD ABDULLAH BHATTI ---")

# Poori game ko chalaye rakhne ke liye main loop
while True:
    guessed_letters = [" "]  # Saari spaces pehle se khuli rahengi
    wrong_guesses = 0        # Har naye word par ghaltiyan zero se shuru hongi

    # Ek lafaz khelne ka loop
    while wrong_guesses < 6:
        print("\n-------------------------------")
        print("CURRENT LIVE HANGMAN STATUS:")
        print("-------------------------------")
        
        # MANUAL DRAWING (Ghaltiyun ke mutabiq live badlega)
        if wrong_guesses == 0:
            print("   +---+")
            print("   |   |")
            print("   |")
            print("   |")
            print("  ===")
        elif wrong_guesses == 1:
            print("   +---+")
            print("   |   |")
            print("   |   O")
            print("   |")
            print("  ===")
        elif wrong_guesses == 2:
            print("   +---+")
            print("   |   |")
            print("   |   O")
            print("   |   |")
            print("  ===")
        elif wrong_guesses == 3:
            print("   +---+")
            print("   |   |")
            print("   |   O")
            print("   |  /|")
            print("  ===")
        elif wrong_guesses == 4:
            print("   +---+")
            print("   |   |")
            print("   |   O")
            print("   |  /|\\")
            print("  ===")
        elif wrong_guesses == 5:
            print("   +---+")
            print("   |   |")
            print("   |   O")
            print("   |  /|\\")
            print("   |  /")
            print("  ===")

        # Word ko dashes/blanks mein dikhana
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
                
        print("\nWORD:", display)
        print("WRONG ATTEMPTS:", wrong_guesses, "/ 6")

        # JEET KA FAISLA
        if "_" not in display:
            print(f"\n🎉 JIT GAYE ABDULLAH BHAI! Word tha: {secret_word}")
            break

        # User se input lena
        guess = input("\nEnter a letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet!")
            continue
            
        if guess in guessed_letters:
            print("Yeh letter aap pehle hi guess kar chuke hain!")
            continue

        guessed_letters.append(guess)

        # Ghalti check karna
        if guess not in secret_word:
            print("❌ Galat Guess!")
            wrong_guesses = wrong_guesses + 1

    # HAAR KA FAISLA (Agar 6 ghaltiyan poori ho jayein)
    if wrong_guesses == 6:
        print("   +---+")
        print("   |   |")
        print("   |   O")
        print("   |  /|\\")
        print("   |  / \\")
        print("  ===")
        print(f"\n💀 GAME OVER! Correct Word Tha: {secret_word}")

    # ⚡ FIX LOGIC: Ab computer agli game ke liye LAZMI list se random lafaz chunega
    secret_word = random.choice(words_pool)
    
    # Aglay lafaz par jane ka protocol
    play_again = input("\nDo you want to play the next word? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThank you for playing, Commander Abdullah! Goodbye.")
        break
