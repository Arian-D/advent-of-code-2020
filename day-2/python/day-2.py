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
    """Part 1"""
    [policy, password] = line.split(':')
    [between, character] = policy.split()
    (a, b) = tuple(map(int, between.split('-')))
    return is_between(character, password, (a, b))

def is_in_correct_position(character: str,
                           password: str,
                           positions: Tuple[int, int]) -> bool:
    def xor(a: bool, b: bool) -> bool:
        return (a or b) and not (a and b)
    (fst, snd) = positions
    return xor(password[fst - 1] == character, password[snd - 1] == character)

def is_valid_with_correct_rule(line: str) -> bool:
    """Part 2"""
    [policy, password] = line.split(':')
    [between, character] = policy.split()
    (a, b) = tuple(map(int, between.split('-')))
    return is_in_correct_position(character, password[1:], (a, b))

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
    valid_password_count = 0
    for policy in rules:
        if is_valid_with_correct_rule(policy):
            valid_password_count += 1
    print("Part 2:",
          f"There are {valid_password_count} valid passwords.")

if __name__ == "__main__":
    main()
