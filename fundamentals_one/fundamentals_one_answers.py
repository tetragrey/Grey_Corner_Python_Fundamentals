"""This file contains the answers for the problems given in a lesson."""


def warm_up():
    my_string = "hello world"
    my_list = ['this is a list', 'yes it is']
    my_empty_list = []
    return my_string, my_list, my_empty_list


def problem_one():
    example_range = range(2, 7)
    example_list = list(example_range)
    return example_list


def problem_two():
    potato_string = "Potatoes have eyes but cannot see Taisan"
    potato_list = potato_string.split()
    return potato_list


def problem_three(races=["catgirl", "miqo'te", "catboy", "catperson", "human but with cat ears (and a tail)"]):
    second_element = races[1]
    last_element = races[-1]
    return second_element, last_element


def problem_four(list_of_strings=["green", "red", "yellow", "purple", "magenta", "fuschia"]):
    blue_in_list = 'blue' in list_of_strings
    return blue_in_list


def problem_five(broken_sentence=['I like to eat peaches', 'blood', 'and oranges', 'you got that?']):
    joined_sentence = ', '.join(broken_sentence)
    return joined_sentence


def problem_six(chicken_joke="Why did the chicken cross the road? Because she couldn't walk around it."):
    chick_in_string = "chick" in chicken_joke
    rooster_in_string = "rooster" in chicken_joke
    return chick_in_string, rooster_in_string


def problem_seven(mystery_number):
    number_value = ''
    if mystery_number == 0:
        number_value = 'zero'
    elif mystery_number > 0:
        number_value = 'positive'
    elif mystery_number < 0:
        number_value = 'negative'
    return number_value


def problem_eight(mystery_number_list):
    positives = 0
    negatives = 0
    zeroes = 0
    for mystery_number in mystery_number_list:
        if mystery_number == 0:
            zeroes += 1
        elif mystery_number > 0:
            positives += 1
        elif mystery_number < 0:
            negatives += 1
    return positives, negatives, zeroes
