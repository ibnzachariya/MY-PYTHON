# scores = [20, 30, 40, 40, 50, 60, 70, 51]
#
# def analyze_scores(scores):
#     highest = scores[0]
#     lowest = scores[0]
#     total = 0
#     passed_count = 0
#
#     # Loop
#     for score in scores:
#         if score > highest:
#             highest = score
#         if score < lowest:
#             lowest = score
#         total += score
#         if score >= 50:
#             passed_count += 1
#
#     average = round(total / 8)
#     print("Highest score:", highest)
#     print("Lowest score:", lowest)
#     print("Average score:", average)
#     print("Number of students passed:", passed_count)
#
# analyze_scores(scores)