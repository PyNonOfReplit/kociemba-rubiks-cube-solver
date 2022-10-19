$pip install RubikTwoPhase
import twophase.solver as tsv
print("Set the green face of your Rubik's cube facing towards you. Make sure that the white face is facing  upwards. If it is not, then flip your cube so that the white face is facing upwards. Next, set the red face to the right of your green face. Now, the green stickers will be considered as 'F' and the blue stickers  will be considered as 'B'. Your white stickers will be considered as 'U' and the yellow stickers will be considered as 'D'. Finally, the orange stickers will be considered as 'L' and the red stickers will be considered as 'R'. Enter your values, first with the white face, then the red face, then the green face, then the orange face and finally the blue face")
cubestring = input("Enter your unsolved cube's sticker notation: ")
moves = int(input("By how many moves would you like to solve your rubiks cube: "))
timeout = int(input("How long do you want the calculation to be? If your desired target is not reached within this time limit, the shortest possible solution will be given: "))
try:
    tsv.solve(cubestring, moves, timeout)
except ValueError:
    print("Your cube string might be invalid. Check your cube or rewrite the notation based on the given steps")
