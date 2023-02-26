# Let's use our knowledge about booleans and comparisons to compare the data of two students
# from a collection of grade submissions.

id_1 = "#4"
average_grade_1 = "A"
test_score_1 = 90

id_2 = "#5"
average_grade_2 = "A"
test_score_2 = 70

no_duplicates = id_1 != id_2
print("No duplicate entries:")
print(no_duplicates)

same_average = average_grade_1 == average_grade_2
print("Same average grade:")
print(same_average)


# Now that we've saved the data for each student entry, we're ready to compare them.

higher_score = test_score_1 > test_score_2
print("id_1 has a higher score:")
print(higher_score)
