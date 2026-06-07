# def calculate_love_score(Abdulfatai, Rofeeah):
#     combined_names = (Abdulfatai + Rofeeah).lower()
#     true_count = combined_names.count("t") + combined_names.count("r") + combined_names.count(
#         "u") + combined_names.count("e")
#     love_count = combined_names.count("l") + combined_names.count("o") + combined_names.count(
#         "v") + combined_names.count("e")
#     love_score = int(str(true_count) + str(love_count))
#
#     print(f"Love score = {love_score}")
#
#
#     calculate_love_score(Abdulfatai, Rofeeah)

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("Abdulfatai", "Rofeeah")
