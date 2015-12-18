# debug lines h3h3
# import pdb; pdb.set_trace()


def do():
    problem_second(get_input())
    # test = [
    #     "qjhvhtzxzqqjkmpb",
    #     "xxyxx",
    #     "uurcxstgmygtbstg",
    #     "ieodomkazucvgmuy",
    #     "aaangdddf",
    #     "rxexcbwhiywwwwnu"
    # ]
    # problem_second(test)


def problem_first(iterable):
    vowels = ["a", "e", "i", "o", "u"]
    forbidden_words = ["ab", "cd", "pq", "xy"]
    nice_strings = 0
    for line in iterable:
        if len(line) < 1:
            continue
        # Lets say all words are nice at first until proven nasty.
        nice_string = True
        vowels_count = []
        repeated_letter = False
        for word in forbidden_words:
            if line.find(word) != -1:
                nice_string = False
        if not nice_string:
            continue
        for char in line:
            if repeated_letter == char:
                repeated_letter = True
            if repeated_letter != True:
                repeated_letter = char
            if char in vowels:
                vowels_count.append(char)
        if len(vowels_count) < 3 or repeated_letter != True:
            continue
        nice_strings += 1
    print(nice_strings)


def problem_second(iterable):
    nice_strings = 0
    nice_dict = {}
    nice_set = set()
    for line in iterable:
        line = line.replace("\n", "")
        word_dict = {}
        len_line = len(line)
        char = ""
        char_counts = 0
        for x in range(0, len_line):
            if (x + 1) > len_line:
                break
            if char == line[x]:
                char_counts += 1
            else:
                char_counts = 1
            char = line[x]
            key = line[x:x + 2]
            if len(key) != 2:
                break
            if char_counts > 1 and (char_counts % 2) == 0 and key in word_dict and key[0] == key[1]:
                continue
            if key in word_dict:
                word_dict[key] += 1
            else:
                word_dict[key] = 1
        repeated_pair = False
        char_between_repeated = False
        repeated_pair_str = ""
        for x in range(0, len_line):
            word = line[x:x + 2]
            if repeated_pair and char_between_repeated:
                break
            if not repeated_pair and len(word) == 2:
                repeated_pair = word_dict[word] >= 2
                if repeated_pair:
                    repeated_pair_str = word
            if not char_between_repeated:
                char_between_repeated = checkCharBetweenPair(line[x - 1:x + 2])
        if repeated_pair and char_between_repeated:
            nice_set.add(line)
        nice_dict[line] = {"word": repeated_pair_str,
                           "char_between_repeated": char_between_repeated, "repeated_pair": repeated_pair}
    print(len(nice_set))
    return nice_dict


def checkCharBetweenPair(word):
    if len(word) != 3:
        return False
    return word[0] == word[2]


def get_input():
    return open("input", "r")
