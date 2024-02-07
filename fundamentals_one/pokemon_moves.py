"""Information about Pokémon moves, including a function to name them"""

descriptive_words = ['ice ', 'water ', 'hyper ', 'thunder ', 'fire ', 'photon ', 'ion ', 'lepton ', 'hadron ',
                     'fell ', 'furious ', 'stone ', 'iron ', 'heavy ', 'toxic ', 'kindness ', 'sorrowful ',
                     'fated ', 'desire ', 'faint ', 'bullet ', 'dancing ', 'convective ', 'barrier ', 'soulful ']
extra_credit_descriptive_words = ['mega', 'bio-', 'psycho', 'pyro', 'poke-', 'draco-', 'aero', 'ante', 'pseudo-', 'psy',
                                  'giga', 'charge-', 'bait-and-', 'electro-', 'anti', 'wake-up-', 'free', 'under']
physical_words = ["slam", "blitz", "charge", "drill", "beak", "wing", "punch", "kick", "suplex", "drop", "uppercut",
                  "jab", "tackle", "slap", "wailing", "bite", "fang", "flurry", "tail", "crash", "cleave", "throw",
                  "lunge", "break", "axe", "slash"]
special_words = ["ball", "beam", "twister", "wave", "pulse", "burst", "eruption", "sphere", "ball", "blast", "drain",
                 "erosion", "wind", "heartbreak", "kinesis", "dance", "zenith", "song", "aria", "uproar",
                 "gale", "spirit", "roar", "glare", "blaze", "flow", "soulblaze", "flare", "emanation"]


def split_down_the_middle(pokemon_name):
    """Split the Pokémon's name in two down the middle (more or less lol)"""
    name_midpoint = int(len(pokemon_name))
    pokemon_name_start = pokemon_name[:name_midpoint+1]
    pokemon_name_end = pokemon_name[name_midpoint-1:]
    return pokemon_name_start, pokemon_name_end


def number_value(input_string):
    """Convert the letters in the Pokémon's name to numbers and find their total value"""
    letter_value = 0
    for char in input_string.lower():
        letter_value += ord(char) - 96
    return letter_value


def create_move_part(letter_value, first_or_second, extra_credit=False):
    """Select a word from the words lists to use in creating a move. 'first' is for descriptive words (the first word
    in a move) and 'second' is for physical or special words (the second word in a move). Words are chosen from the
    list based on the modulus of the input value and the length of the list."""
    if first_or_second == 'first':
        word_list = descriptive_words
        if extra_credit:
            word_list += extra_credit_descriptive_words
    else:
        word_list = physical_words + special_words
    word_index = letter_value % len(word_list)
    move_part = word_list[word_index]
    return move_part


def move_generator(pokemon_name, move_list, extra_credit=False):
    """Get the name of a move based on the Pokémon's name. The current move list is needed in order to prevent repeats.
    To use the move_generator function, the first argument is the name of your Pokémon (a string). The second argument
    is the list of moves your Pokémon already knows -- empty lists are ok if it doesn't know any moves yet.
    For example:
    pokemon_name = "Floofy"
    move_list = []
    new_move = move_generator(pokemon_name, move_list)

    :param pokemon_name: (string) the name of the Pokémon the move is for
    :param move_list: (list) list of the Pokémon's current moves (can be empty)
    :param extra_credit: (bool) if True, more difficult-to-split descriptive words are used
    :return: (string) the name of a Pokémon move
    """
    # Split the Pokémon's name in two down the middle (more or less lol)
    pokemon_name_start, pokemon_name_end = split_down_the_middle(pokemon_name)

    # Convert the letters in the Pokémon's name to numbers and find their total value
    start_value = number_value(pokemon_name_start)
    end_value = number_value(pokemon_name_end)

    # Adjust the values based on the moves that have already been selected
    if len(move_list) > 0:
        start_value += number_value(move_list[-1].split()[-1])
        end_value += number_value(move_list[-1].split()[0])

    # Select the move based on the modulus of the number values
    move_name = (create_move_part(start_value, 'first', extra_credit) +
                 create_move_part(end_value, 'second'))

    return move_name
