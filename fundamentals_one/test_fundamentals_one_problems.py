import pytest
from fundamentals_one_problems import warm_up, problem_one, problem_two, problem_three, problem_four, problem_five
from fundamentals_one_problems import problem_six, problem_seven, problem_eight


def test_warm_up():
    my_string, my_list, my_empty_list = warm_up()
    assert type(my_string) is type('hello world')
    assert type(my_list) is type([])
    assert type(my_empty_list) is type([])
    assert len(my_list) > 0
    assert len(my_empty_list) == 0


def test_problem_one():
    test_list = problem_one()
    if test_list == [2, 3, 4, 5]:
        raise ValueError("Uh-oh! Looks like you forgot about an important detail about how range works and now you're"
                         "\nmissing your 6 on the end! Try making your maximum value (the second argument) a bit "
                         "bigger ;)")
    if type(test_list) is type(range(2, 7)):
        raise ValueError("Don't forget to use the list function so you get the list! Otherwise you're just making a "
                         "range object")
    assert test_list == [2, 3, 4, 5, 6]


def test_problem_two():
    test_list = problem_two()
    assert type(test_list) is type([])
    assert len(test_list) > 1


def test_problem_three():
    answers = [answer for answer in problem_three()]
    assert "miqo'te" in answers
    assert 'human but with cat ears (and a tail)' in answers


def test_problem_four():
    blue_in_list = problem_four()
    assert blue_in_list is False


def test_problem_five():
    joined_sentence = problem_five()
    assert joined_sentence == "I like to eat peaches, blood, and oranges, you got that?"


def test_problem_six():
    answers = [answer for answer in problem_six()]
    assert True in answers
    assert False in answers


def test_problem_seven():
    # Test for a negative value
    positive_result = problem_seven(-1)
    assert positive_result == 'negative'

    # Test for a positive value
    positive_result = problem_seven(4)
    assert positive_result == 'positive'

    # Test for zero
    positive_result = problem_seven(0)
    assert positive_result == 'zero'


def test_problem_eight():
    mystery_number_list = [1, 2, 3, 0, -1, 0, 4, 5]
    answers = [answer for answer in problem_eight(mystery_number_list)]
    assert 5 in answers
    assert 2 in answers
    assert 1 in answers


if __name__ == '__main__':
    pytest.main()
