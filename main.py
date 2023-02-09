from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left: str, right: str) -> bool:
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str) -> int:
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            prev = opening_brackets_stack[-1]
            if not are_matching(prev, next):
                return i + 1
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        return len(opening_brackets_stack)

    return 0


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch if mismatch != 0 else "Success")


if __name__ == "__main__":
    main()
