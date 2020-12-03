from typing import List

def product_that_sums_up_to_2020(entries: List[int]) -> int:
    """Part one"""
    as_set = set(entries)
    for entry in entries:
        if 2020 - entry in as_set:
            return entry * (2020 - entry)
    raise ValueError("Not found")

def product_of_three_numbers_that_sums_up_to_2020(entries: List[int]) -> int:
    """Part two"""
    as_set = set(entries)
    # Using List comprehensions
    # sum_set = {i + j for i in entries for j in entries if i != j}
    # Without using list comprehensions
    sum_set = set()
    for i in entries:
        for j in entries:
            if i != j:
                sum_set.add(i + j)
    for i in entries:
        a = 2020 - i
        if a in sum_set:
            for j in entries:
                b = a - j
                if b in as_set:
                    return i * j * (2020 - i - j)
    raise ValueError("Not found")

def main() -> None:
    nums : List[int] = []
    try:
        nums = [int(n) for n in open("../input.txt").read().split()]
    except FileNotFoundError:
        print("input.txt ain't there, buddy")
        
    try:
        print(
            "Part 1:",
            product_that_sums_up_to_2020(nums)
        )
        print(
            "Part 2:",
            product_of_three_numbers_that_sums_up_to_2020(nums)
        )
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
