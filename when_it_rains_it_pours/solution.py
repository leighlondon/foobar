"""
The solution to the "when_it_rains_it_pours" problem.
"""


def answer(heights):
    """
    The solution.

    Move along the list of heights, starting at index 0, and search for a
    local maxima (a 'peak').

    If next neighbour to the right is higher, then discard the current peak
    and move forward.

    If next is lower, advance the "second peak" towards the next peak.
    In the code below, the first peak is "left" and the second is "right".

    Once the "right" peak has been found, the area between them needs to be
    calculated. This needs to have the values of the slice between them, and
    the heights of the peaks as well, to be able to find the "lowest" of the
    two peaks and use this to find the missing spaces. Then sum this to the
    total area value, and repeat.
    """
    # Area starts at 0.
    total_area = 0
    # Alias the heights to make it easier to follow.
    h = heights

    # Start at the first (the "left" side).
    i = 1

    # Set the initial indexes for the "peaks".
    left = 0
    right = 0

    # Defensive bounds checking.
    if len(h) == 1:
        return 0

    # Continue along until we reach the end.
    while i < len(h):

        # If left is shorter, move forward.
        if h[left] <= h[i]:
            # If the next item is taller for the left scout,
            # simply move along the left scout.
            left = i
            i = i + 1

        # If left is taller, start the right scout.
        elif h[left] > h[i]:
            # Move the right scout forward until a peak greater
            # or equal to the left scout is found, and then find
            # the area in that slice.
            #
            # Once this is found, move the left scout to the right,
            # and continue again.
            #
            # The initial value for the right peak is the trough value, i,
            # so that we can check for better-but-not-best peaks.
            right = i

            # We start up another while loop, but this one has a chance to
            # break- and we backtrack the i value as well, anyway.
            while i < len(h):

                if h[i] >= h[left]:
                    # An unambiguous peak, just break now. There are no
                    # better possible peaks for this trough.
                    right = i
                    break

                elif h[i] >= h[right]:
                    # There's an ambiguous peak, we don't know if there's a
                    # better peak a few values further.
                    right = i

                # It's neither a better peak nor the best peak, just keep
                # moving forward.
                i = i + 1

            # Only run the area calculation if it's required.
            # This can be for one of two reasons- an ambiguous peak was found
            # and no better peak was found in the rest of the values,
            # or an unambiguous peak was found. In each case, we can check
            # by seeing if the 'right' peak value has changed from the
            # initial value.
            if right > left + 1:
                area = calculate_area(h[left], h[right], h[left:right])
                total_area = total_area + area

            # Advance the left peak and then repeat. This can, in some cases,
            # mean backtracking the current i pointer node. So we just set
            # it to the generic case that covers both,
            # "move forward the left, then move one further for i".
            left = right
            i = left + 1

    # Pass back the total area.
    return total_area


def calculate_area(left, right, heights):
    """
    Calculating the area in a slice of numbers.
    Needs to know the height of the border peaks and
    the values of the slice.
    """
    # Defensiveness.
    if not heights:
        return 0
    # Figure out the lower of the two peaks.
    lowest = left if left < right else right
    # Start the running total.
    total = 0
    # Account for the first element being the left peak.
    # Sub slice it further, calculate area for each column,
    # and sum them for the total area in this section.
    for element in heights[1:]:
        total = total + (lowest - element)
    # Return the total.
    return total
