from typing import List

def product_that_sums_up_to_2020(entries: List[int]) -> int:
    as_set = set(entries)
    for entry in entries:
        if 2020 - entry in as_set:
            return entry * (2020 - entry)
    raise ValueError("Not found")

def main() -> None:
    try:
        print(
            product_that_sums_up_to_2020(
                [int(n) for n in open("../input.txt").read().split()]
            )
        )
    except:
        print("Rip")

if __name__ == "__main__":
    main()
