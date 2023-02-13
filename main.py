import os


def are_matching(left: str, right: str) -> bool:
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str) -> str:
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
        if next in ")]}":
            if not opening_brackets_stack:
                return str(i + 1)
            if are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop()
            else:
                return str(i + 1)
    if opening_brackets_stack:
        return str(i + 1)
    return "Success"


def main():
    mode = (
        input("Choose mode (I - manual input, F - read from file): ")
        .strip()
        .upper()
    )
    match mode:
        case "I":
            text = input()
            print(find_mismatch(text))
        case "F":
            for i in range(len(os.listdir("test")) // 2):
                print(f"Running test {i}... ", end="")
                with open(f"test/{i}", "r") as fi, open(
                    f"test/{i}.a", "r"
                ) as fa:
                    input_data = fi.readline()
                    answer_data = fa.readline().strip()
                    mismatch = find_mismatch(input_data)
                    if mismatch != answer_data:
                        print(
                            f"Test failed, want {answer_data}, got {mismatch}"
                        )
                    else:
                        print("Success")
        case _:
            print("Invalid mode")
            os.exit()


if __name__ == "__main__":
    main()
