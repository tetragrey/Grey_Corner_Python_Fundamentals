"""This file is for filling in answers to the problems given in a lesson.

In order to answer a question, write the code within the function block provided. Return the answers that are requested

Once you've finished a problem, you can go to test_fundamentals_one_problems and run it to see if your answer was right.
If it's right, the corresponding test will pass. If it's not right, the test will fail, but don't worry -- every
test fails on the first try :)"""

"""
Warm-up: Defining variables
Create three variables:
    1. A string (it can have whatever you want in it, or even be empty)
    2. A list with at least one element inside (the element can be anything you want)
    3. An empty list

Return all three variables to pass the test."""

def warm_up():
    """Write your code here, then return the answer"""
    my_string =
    my_list =
    my_empty_list =

    return my_string, my_list, my_empty_list


# ---------------------------------------------------------------------------------------------------------------------


"""
Problem 1: Function calls
So you've got a function. When you want to use that function, you call it. Function calls are sort of the point of
functions.
Every function does something. Let's look at the `range` function, for instance, which is maybe one of the most useful
functions in Python. It automatically creates a list of all the numbers between any two numbers that you give it.
The idea goes:
    - You want a function to do its thing, so you call its name. `range`
    - You also want to give the function the things it needs to work. These are called the arguments, and they
      go inside the parentheses you always see after the function's name. `range(0, 5)`
    - Now you're making a list from 0 to 4 (not a typo, that's how range works), and it looks like [0, 1, 2, 3, 4].
      BUT it's just THERE. It gets created and then instantly lost into the aether. To hold it down, we need to give it
      a name -- that is, we need to assign it to a variable. `example_list = range(0, 5)`
And that's a complete function call. Now you've got the value you wanted. I hope you wanted a list from 0 to 4!
As an extra bit to know about the range function, the result you get from it isn't actually a list. To see your list,
you have to call the list function. For example:
```
>>> example_range = range(0,5)
>>> example_list = list(example_range)
>>> example_list
[0, 1, 2, 3, 4]
```

Call the range function to make a list from 2 to 6. It should look like this: [2, 3, 4, 5, 6]. Don't forget to use the
list function to get to see the list. Then, return the list from 2 to 6 to pass the test."""

def problem_one():
    """Write your code here, then return the answer"""

    return


# ---------------------------------------------------------------------------------------------------------------------


"""
Problem 2: Split
The split function is useful for working with words -- among other things! It splits a string into pieces divided
by the character (or character combination) of your choice. Those pieces are then dumped into a list.
The default character is a space.
Example usage:
```
>>> sample_string = "I like coconuts"
>>> sample_string.split()
['I', 'like', 'coconuts']
```

Make a string with at least two words in it. Then, use the split function to divide the string into a list of words.
Return the list of words to pass the test."""

def problem_two():
    """Write your code here, then return the answer"""

    return


# ---------------------------------------------------------------------------------------------------------------------


"""
Problem 3: List indices
You can get the nth element in a list by adding `[n]` after the name of the list. BUT! Remember, for some reason Python
always starts counting from 0. So to get the first element in a list called `clothes`, you have to use `clothes[0]`.
To get the second element, it's `clothes[1]. This is not the case when counting backwards. To get the last element in a
list called `clothes`, you use `clothes[-1]`.

You're given a list called `races`. Return the 2nd element and the last element of that list.
The linter does not like the races list, but don't worry about it."""

def problem_three(races=["catgirl", "miqo'te", "catboy", "catperson", "human but with cat ears (and a tail)"]):
    """Write your code here, then return the answer"""

    return


# ---------------------------------------------------------------------------------------------------------------------


"""
Problem 4: Searching inside lists
If you want to check whether something is inside a list, the syntax is actually pretty intuitive. Let's say you've got
a list of numbers and you want to make sure 2 is inside that list.
```
>>> list_of_numbers = list(range(0, 5))
>>> two_is_in_the_list = 2 in list_of_numbers
>>> two_is_in_the_list
True
```
When you ask whether 2 is in the list, it'll tell you either True or False. These aren't strings! They're True or False
values specifically. In the above example, two_is_in_the_list is a variable that holds the value True.

You're given a list of strings called list_of_strings. Each string is the name of a color. Check whether blue is in
the list, then return the result."""

def problem_four(list_of_strings=["green", "red", "yellow", "purple", "magenta", "fuschia"]):
    """Write your code here, then return the answer"""

    return


# ---------------------------------------------------------------------------------------------------------------------


"""
Problem 5: Join
If the split function is a way to turn a string into a list, then the join function does the opposite. You give it two
things: the list you want to turn into a string, and the character you want to put between the elements. The list goes
in the parentheses as an argument, while the joining character goes before `.join`. Make sure you put that period before
it! Often, of course, you'll want that joining character to be a space (or nothing), but the options are useful.
```
>>> example_list = ["I'm", "coo-coo", "for", "Cocoa", "Puffs"]
>>> '~'.join(example_list) 
"I'm~coo-coo~for~Cocoa~Puffs"
```
These are simple functions, btw, and we're going through a couple slowly now to give you experience, but going forward
you'll be looking these up yourself on Google and ChatGPT. Don't worry about memorizing them! You can always look them
up again later when you need them.

For now, though, I'm giving you a list called broken_sentence. I want you to join it with a comma and a space ', ' and
then return the resulting string to pass the test."""

def problem_five(broken_sentence=['I like to eat peaches', 'blood', 'and oranges', 'you got that?']):
    """Write your code here, then return the answer"""

    return


# ---------------------------------------------------------------------------------------------------------------------


"""
Problem 6: Searching inside strings
Searching inside strings is about as intuitive as searching inside lists! Let's say you've got a string called
potatoes_string and you want to check whether 'potato' appears in that string. You just do:
```
>>> potatoes_string = "I eat potatoes with cranberry sauce"                                                                                                                                                
>>> 'potato' in sample_string
True
```
If the string you're searching for isn't in the bigger string, of course, checking whether it's there will return False.

You're given a string called chicken_joke. Search for one string that's in there, and search for a different string
that's not in there. Return the results of both searches."""

def problem_six(chicken_joke="Why did the chicken cross the road? Because she couldn't walk around it."):
    """Write your code here, then return the answer"""

    return


# ---------------------------------------------------------------------------------------------------------------------


"""
Problem 7: Conditionals
Conditionals are one of the most famous and essential elements of coding. By establishing that something can happen
only if something else is true, you gain a lot of control over exactly what your code is doing.
```
>>> example_number = 4
>>> if example_number == 3:
...     print('The number is 3')
... elif example_number == 4:
...     print('The number is 4')
... else:
...     print("The number isn't 3 or 4, but other than that, who knows what it is?")
...
The number is 4
```
 - if: does the thing under it if the condition is True.
 - else: does the thing under it if all of the if or elif conditions before it were False.
 - elif: does the thing under it if all of the if or elif conditions before it were False AND its own condition is True.
   (elif is, of course, short for else if)
It's important that you get the indents right. Everything that is intended under a conditional happens if the
condition is met; on the other hand, the conditional only does what's indented and nothing else.

For this problem, I'm giving you an integer called mystery_number. You don't know what it is! I want you to find out
whether it's positive, negative, or zero. To pass the test, you need to return a string. If the number is positive,
the string should be 'positive'. If the number is negative, the string should be 'negative', and if the number is 0,
the string should be -- you guessed it -- 'zero'.
This one might take some Googling or experimenting!"""

def problem_seven(mystery_number):
    """Write your code here, then return the answer"""

    return


# ---------------------------------------------------------------------------------------------------------------------


"""
Problem 8: For loops
Loops are a way of doing the same thing to different variables. Let's take a look at this example:
```
>>> word_list = ['smarmy', 'unction', 'blurt']
>>> for word in word_list:
...     print(word)
...
smarmy
unction
blurt

```
With this one command, we printed the whole list! As you can imagine, a for loop is especially powerful when you have a
very long list to work through.
What did the loop do, though, exactly? Well, we gave it the list `word_list`, and then it will take each element in the
list one by one. First, it'll pick smarmy. It'll assign 'smarmy' to the variable `word`. Then it'll execute the 
indented code: in this simple case, it just prints what's inside the variable `word`. Then it loops back to the
beginning and starts over with the next element in the list.

For this last exercise, we're going to expand on our work with conditionals. Instead of getting one mystery number,
now you'll be getting a whole `mystery_number_list`. You don't know what numbers are in this mystery list, and you don't
know how many numbers are in it, either. Use a loop to find out how many of the numbers in the list are positive,
how many are negative, and how many are 0. To pass the test, return three integer variables:
 - The number of positive numbers in the list
 - The number of negative numbers in the list
 - The number of instances of the number 0 in the list
Hint: To count things, you can create a variable with a value of 0 and then add +1 to it every time the event you're
interested in happens ;)"""

def problem_eight(mystery_number_list):
    """Write your code here, then return the answer"""

    return


"""All done! Now all that's left is the project. Nice job :)"""