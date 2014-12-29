Guard game
==========

You're being held in a guarded room in Dr. Boolean's mad science lab.
How can you escape?

Beta Rabbit, a fellow captive and rabbit, notices a chance. The lab guards are
always exceptionally bored, and have made up a game for themselves. They take
the file numbers from the various specimens in the Professors lab, and see who
can turn them into single digit numbers the fastest.

"I've observed them closely," Beta says. "For any number, the way they do this
is by taking each digit in the number and adding them all together, repeating
with the new sum until the result is a single digit. For example, when a guard
picks up the medical file for Rabbit #1235, she would first add those digits
together to get 11, then add those together to get 2, her final sum."

See if you can short circuit this game entirely with a clever program, thus
driving the guards back to severe boredom. That way they will fall asleep and
allow you to sneak out!

Write a function `answer(x)`, which when given a number `x`, returns the final
digit resulting from performing the above described repeated sum process on `x`.

`x` will be 0 or greater, and less than `2^31 -1` (or 2147483647), and the
answer should be 0 or greater, and a single integer digit.

Test cases
==========

Inputs:

    (long) x = 13

Output:

    (int) 4

Inputs:

    (long) x = 1235

Output:

    (int) 2
