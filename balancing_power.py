def is_power_balanced(n, party):
    """
    There are n legislators in the State of Confusion, each representing one of the three major parties:

    Future One, Two-gether, and Triple Harmony.

    The founders of the State envisioned a healthy society where the three parties maintain
    the balance of power and no party gets a dictatorial position by having too many legislators.

    Formally, we say that the balance of power is achieved when no one party has strictly
    more legislators than the other two parties combined.

    The function input will have 2 paramaters. The first will be the total number of legislators (n), 
    the second will be n space-separated integers, representing the party aﬃliation of each elected person,
    1 being Futre One, 2 being Two-gether, 3 being Triple Harmony.

    The function will output a string on a single line, representing the headline of the article you will write.

    TODO: If the balance of power is achieved, then print only “Power Balanced” without quotation marks. 
    Otherwise, print only “[Party] Dominates” without quotation marks, where “[Party]” is replaced with the name of the winning party. 
    
    Note that the output is case-sensitive, and must match the format exactly without leading or trailing whitespace.
    """
    
    return None # TODO: Implement this function

def is_power_balanced(n, party):
    """
    Checks if power is balanced among three parties based on the number of legislators.
    """
    counts = [0, 0, 0, 0]  # Use index 1, 2, 3 (ignore index 0 for simplicity)

    for p in party:
        counts[p] += 1

    if counts[1] > counts[2] + counts[3]:
        print("Future One Dominates")
    elif counts[2] > counts[1] + counts[3]:
        print("Two-gether Dominates")
    elif counts[3] > counts[1] + counts[2]:
        print("Triple Harmony Dominates")
    else:
        print("Power Balanced")

is_power_balanced(5, [1, 1, 2, 2, 3])

# Run pytest test_problem_1.py to test the function