from pokemon_moves import special_words, physical_words, move_generator


if __name__ == "__main__":
    pokemon_name = "Floofy"
    move_list = []
    for _ in range(4):
        new_move = move_generator(pokemon_name, move_list, extra_credit=False)
        move_list.append(new_move)
    print(f"{pokemon_name}'s moves are:"
          f"\n- {move_list[0]}"
          f"\n- {move_list[1]}"
          f"\n- {move_list[2]}"
          f"\n- {move_list[3]}")

    special_moves = 0
    physical_moves = 0
    for move in move_list:
        if move.split()[1] in physical_words:
            physical_moves += 1
        if move.split()[1] in special_words:
            special_moves += 1

    if special_moves > physical_moves:
        attack_style = 'special'
    elif physical_moves > special_moves:
        attack_style = 'physical'
    else:
        attack_style = 'balanced'
    print(f"{pokemon_name} is a {attack_style} attacker.")
