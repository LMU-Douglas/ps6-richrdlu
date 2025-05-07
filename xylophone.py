def cost_of_bars(bars):
    """
    A xylophone is a musical instrument made of wooden bars, each of which makes a specific pitch when
    struck with a mallet. 

    The wooden bars must have contiguous integer lengths from the longest to the shortest,
    without duplicates. In other words, every bar except for the rightmost one must have a length exactly 1
    longer than the one immediately to its right. 

    For example, a xylophone may have bars of lengths [7, 6, 5, 4]
    or [10, 9, 8], but not [7, 5, 4] nor [3, 3, 2, 1].


    You already have 3 wooden bars of diﬀerent lengths, and want to create a xylophone using all of them.


    You may **not** cut the bars or alter them in any way, but you **may buy additional wooden bars** as necessary.
    The cost of buying a wooden bar is equal to its length. 

    TODO: Find the minimum cost to build a xylophone

    The only paramater is a string with three space-separated integers, each number is the length of a bar you already have.

    You are guaranteed that the three integers are distinct.

    Your program must return a single integer that represents the minimum cost to make a xylophone using
    all three given wooden bars.
    """
    # Hint: The python sort() method can be used to sort a list of integers in ascending order.
    
    return None # TODO: Implement this function

def cost_of_bars(bars):
    bar_list = list(map(int, bars.split()))

    longest = max(bar_list)
    shortest = min(bar_list)

    needed_bars = list(range(longest, shortest - 1, -1)) 

    existing_set = set(bar_list)
    total_cost = 0
    for bar in needed_bars:
        if bar not in existing_set:
            total_cost += bar 

    return total_cost

print(cost_of_bars("7 6 5"))
# Run pytest test_problem_3.py to test the function