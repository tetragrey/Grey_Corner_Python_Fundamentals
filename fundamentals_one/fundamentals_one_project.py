"""Assignment: Every Pokémon knows four moves. Pokémon moves are divided into physical and special moves. We're going to
create a Pokémon, give it four moves, and then find out whether it's a special attacker or a physical attacker. You can
see all the physical and special words, as well as the move_generator function you'll be using, in pokemon_moves.py. The
import statement I already wrote in this file for you will let you use them here. Consider testing them out ahead of
time so you know what you're working with.
    1. Give your Pokémon a name of your choosing. The name should be saved as a string.
    2. Use the move_generator function (look at the green text in the move_generator function in pokemon_moves.py for
       usage instructions) to create four moves. Each move is a string. Save these four moves as a list.
    3. Use an f-string to print all your Pokémon's moves.
    4. Check against physical_words and special_words to count how many of your Pokémon's moves are physical and how
       many are special. If there are more physical moves than special, it's a physical attacker. If there are more
       special moves than physical, it's a special attacker. If it's even, it's a balanced attacker. Assign your
       Pokémon's attack style (physical, special, or balanced) to a variable.
    5. Use an f-string to print your Pokémon's attack style.

    Extra credit: Add the following keyword argument to the move_generator function: extra_credit=True
    Then try to fix the rest of the code so it works again. This will require some out-of-the-box thinking; you won't
    be able to just use the split function anymore. (If it's still easy, try different Pokémon names)


    EXAMPLE PRINT OUTPUT:
Floofy's moves are:
- fire slash
- heavy suplex
- water burst
- fell erosion
Floofy is a balanced attacker.
"""

from pokemon_moves import physical_words, special_words, move_generator

# ________Your code here________
