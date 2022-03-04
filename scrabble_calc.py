one_point = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
two_points = ["d", "g"]
three_points = ["b", "c", "m", "p"]
four_points = ["f", "h", "v", "w", "y"]
five_letters = ["k"]
eight_points = ["j", "k"]
ten_points = ["q", "z"]


def scrabble_calc(word):
    word_score = 0

    for letter in word:
        if letter in one_point:
            word_score += 1
        elif letter in two_points:
            word_score += 2
        elif letter in three_points:
            word_score += 3
        elif letter in four_points:
            word_score += 4
        elif letter in five_letters:
            word_score += 5
        elif letter in eight_points:
            word_score += 8
        elif letter in ten_points:
            word_score += 10

    return word_score


print(scrabble_calc("zoo"))
