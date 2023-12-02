from collections.abc import Iterator

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def problem_part_1(line: str) -> int:
    def find(lined):
        for i in lined:
            try:
                int(i)
            except:
                ...
            else:
                return i

    return int(find(line) + find(line[::-1]))


def problem_part_2(line: str) -> int:
    def find(lined, backward=False):
        text_num = ""
        for i in lined:
            try:
                int(i)
            except:
                if backward:
                    text_num = i + text_num
                else:
                    text_num += i
                for k in numbers:
                    if k in text_num:
                        return numbers[k]
            else:
                return i

    return int(find(line) + find(line[::-1], True))


def sample_data() -> Iterator[str]:
    for l in (
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ):
        yield l


def problem_data() -> Iterator[str]:
    with open("Day1/data", "r") as f:
        for l in f.readlines():
            yield l


def main() -> None:
    part1, part2 = 0, 0
    for l in problem_data():
        part1 += problem_part_1(l)
        part2 += problem_part_2(l)

    print(part1, part2)  # 55538, 54875


if __name__ == """__main__""":
    main()
