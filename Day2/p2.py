from collections.abc import Iterator
import re


def parse_throw(throw: str) -> tuple[int, int, int]:
    red, green, blue = 0, 0, 0
    if (r := re.search(r"(\d+) (red)", throw)) is not None:
        red = int(r.group(1))

    if (g := re.search(r"(\d+) (green)", throw)) is not None:
        green = int(g.group(1))

    if (b := re.search(r"(\d+) (blue)", throw)) is not None:
        blue = int(b.group(1))

    return red, green, blue


def parse_game_part_1(game: str) -> int:
    red, green, blue = 12, 13, 14
    for throw in game.split(";"):
        rc, gc, bc = parse_throw(throw)
        if rc > red or gc > green or bc > blue:
            break
    else:
        return int(re.findall(r"\d+", game)[0])
    return 0


def parse_game_part_2(game: str) -> int:
    r, g, b = 0, 0, 0
    for throw in game.split(";"):
        rc, gc, bc = parse_throw(throw)
        r = rc if rc > r else r
        g = gc if gc > g else g
        b = bc if bc > b else b

    return r * g * b


def sample_data() -> Iterator[str]:
    for l in (
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ):
        yield l


def problem_data() -> Iterator[str]:
    with open("Day2/data", "r") as f:
        for l in f.readlines():
            yield l


def main() -> None:
    part1, part2 = 0, 0
    for l in problem_data():
        part1 += parse_game_part_1(l)
        part2 += parse_game_part_2(l)

    print(part1, part2)  # 3059, 65371


if __name__ == """__main__""":
    main()
