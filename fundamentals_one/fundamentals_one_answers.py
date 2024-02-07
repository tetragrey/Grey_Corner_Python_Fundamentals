"""This file contains the answers for the problems given in a lesson."""


def warm_up():
    """Write your code here, then return the answer"""
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
    """Write your code here, then return the answer"""
    joined_sentence = ', '.join(broken_sentence)
    return joined_sentence
