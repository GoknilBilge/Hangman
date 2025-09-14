import random
import Hangman_LivesAndLogo
import Hangman_Words

chosen_word = random.choice(Hangman_Words.word_list)
lives = 6
print(Hangman_LivesAndLogo.logo)

print(Hangman_LivesAndLogo.stages[lives])

length = len(chosen_word)
display = []
for _ in range(length):
    display += "_"
print(f"{' '.join(display)}")

guessed_letters = []
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You guessed the letter '{guess}', try a different letter.")
        continue
    else:
        guessed_letters.append(guess)
    for i in range(length):
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in chosen_word:
        print(f"The letter '{guess}' is not in the word.")
        lives -= 1
        if lives > 0:
            print(Hangman_LivesAndLogo.stages[lives])
        else:
            print(Hangman_LivesAndLogo.stages[0])
            print("You lose!")
    print(f"{' '.join(display)}")


if "_" not in display:
    print("Congrats, you won!")