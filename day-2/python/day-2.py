from typing import Tuple, List

def is_between(character: str,
               password: str,
               between: Tuple[int, int]) -> bool:
    (a, b) = between
    count = 0
    for c in password:
        if c == character:
            count += 1
        if count > b:
            return False
    if count < a:
        return False
    return True

def is_valid(line: str) -> bool:
    [policy, password] = line.split(':')
    [between, character] = policy.split()
    (a, b) = tuple(map(int, between.split('-')))
    return is_between(character, password, (a, b))

def main() -> None:
    rules: List[str] = []
    valid_password_count = 0
    try:
        rules = open("../input.txt").read().split('\n')[:-1]
    except FileNotFoundError:
        print("Put input.txt back where it came from, or so help me.")

    for policy in rules:
        if is_valid(policy):
            valid_password_count += 1
    print("Part 1:",
          f"There are {valid_password_count} valid passwords.")

if __name__ == "__main__":
    main()
