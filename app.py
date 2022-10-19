import kociemba as hk
import optimal.solver as osv
import twophase.solver as tsv
print("Welcome to the Rubik's Cube Solver, based on Herbert Kociemba's algorithm to solve Rubik's Cubes!")
while True: 
 print("1. About the Rubik's Cube")
 print("2. Source Code on github")
 print("3. Credits")
 print("4. Solve with kociemba method")
 print("5. Solve optimally")
 print("6. Solve using twophase method ")
 check = int(input("Choose the page to go to: "))
 if check == 1:
    print("The Rubik's Cube is a 3-D combination puzzle originally invented in 1974 by Hungarian sculptor and professor of architecture Ernő Rubik. Originally called the Magic Cube,the puzzle was licensed by Rubik to be sold by Ideal Toy Corp in 1980 via businessman Tibor Laczi and Seven Towns founder Tom Kremer. The cube was released internationally in 1980 and became one of the most recognized icons in popular culture. It won the 1980 German Game of the Year special award for Best Puzzle. As of January 2009, 350 million cubes had been sold worldwide, making it the world's bestselling puzzle game and bestselling toy. On the original classic Rubik's Cube, each of the six faces was covered by nine stickers, each of one of six solid colours: white, red, blue, orange, green, and yellow. Some later versions of the cube have been updated to use coloured plastic panels instead, which prevents peeling and fading. Since 1988, the arrangement of colours has been standardised with white opposite yellow, blue opposite green, and orange opposite red, and the red, white, and blue arranged clockwise in that order. On early cubes, the position of the colours varied from cube to cube. An internal pivot mechanism enables each face to turn independently, thus mixing up the colours. For the puzzle to be solved, each face must be returned to have only one colour. Similar puzzles have now been produced with various numbers of sides, dimensions, and stickers, not all of them by Rubik. Although the Rubik's Cube reached its height of mainstream popularity in the 1980s, it is still widely known and used. Many speedcubers continue to practise it and similar puzzles, and compete for the fastest times in various categories. Since 2003, the World Cube Association, the international governing body of the Rubik's Cube, has organised competitions worldwide and recognises world records. Source: Wikipedia.")
 if check == 2:
     print("https://github.com/PyNonOfReplit/kociemba-rubiks-cube-solver")
 if check == 3:
     print("Developer: PyNon")
     print("GitHub: PyNonOfReplit")
     print("Algorithm Developer: Herbert Kociemba (hkociemba)")
     print("License: MIT License")
 if check == 4:
     print("Set the green face of your Rubik's cube facing towards you. Make sure that the white face is facing  upwards. If it is not, then flip your cube so that the white face is facing upwards. Next, set the red face to the right of your green face. Now, the green stickers will be considered as 'F' and the blue stickers  will be considered as 'B'. Your white stickers will be considered as 'U' and the yellow stickers will be considered as 'D'. Finally, the orange stickers will be considered as 'L' and the red stickers will be considered as 'R'. Enter your values, first with the white face, then the red face, then the green face, then the orange face and finally the blue face")
     cubestring = input("Enter your unsolved cube's sticker notation: ")
     try:
         hk.solve(cubestring)
     except ValueError:
         print("Your cube string might be invalid. Check your cube or rewrite the notation based on the given steps")
 if check == 5:
     print("Set the green face of your Rubik's cube facing towards you. Make sure that the white face is facing  upwards. If it is not, then flip your cube so that the white face is facing upwards. Next, set the red face to the right of your green face. Now, the green stickers will be considered as 'F' and the blue stickers  will be considered as 'B'. Your white stickers will be considered as 'U' and the yellow stickers will be considered as 'D'. Finally, the orange stickers will be considered as 'L' and the red stickers will be considered as 'R'. Enter your values, first with the white face, then the red face, then the green face, then the orange face and finally the blue face")
     cubestring = input("Enter your unsolved cube's sticker notation: ")
     moves = int(input("By how many moves would you like to solve your rubiks cube: "))
     timeout = int(input("How long do you want the calculation to be? If your desired target is not reached within this time limit, the shortest possible solution will be given: "))
     try:
         tsv.solve(cubestring, moves, timeout)
     except ValueError:
         print("Your cube string might be invalid. Check your cube or rewrite the notation based on the given steps")
 if check == 6:
     print("Set the green face of your Rubik's cube facing towards you. Make sure that the white face is facing  upwards. If it is not, then flip your cube so that the white face is facing upwards. Next, set the red face to the right of your green face. Now, the green stickers will be considered as 'F' and the blue stickers  will be considered as 'B'. Your white stickers will be considered as 'U' and the yellow stickers will be considered as 'D'. Finally, the orange stickers will be considered as 'L' and the red stickers will be considered as 'R'. Enter your values, first with the white face, then the red face, then the green face, then the orange face and finally the blue face")
     cubestring = input("Enter your unsolved cube's sticker notation: ")
     try:
         osv.solve(cubestring)
     except ValueError:
         print("Your cube string might be invalid. Check your cube or rewrite the notation based on the given steps")
     
     
