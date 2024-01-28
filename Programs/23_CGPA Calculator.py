# Sample Input:
# Student1 Student2 Student3 Student4
#     90      90      90      67
#     90      67      78      7
#     49      50      50      23
# Sample Output:
# Student1 => ('90', '90', '49', 180)
# Student2 => ('90', '67', '50', 207)
# Student3 => ('90', '78', '50', 218)
# Student4 => ('67', '7', '23', 67)

name = list(map(str, input().split()))
n = len(name)
subject1 = list(map(int, input().split()))
subject2 = list(map(int, input().split()))
subject3 = list(map(int, input().split()))
for i in range(n):
    if subject1[i] >= 50 or subject2[i] >= 50 or subject3[i] >= 50:
        cgpa = 0
        if subject1[i] >= 50:
            cgpa += subject1[i]
        if subject2[i] >= 50:
            cgpa += subject2[i]
        if subject3[i] >= 50:
            cgpa += subject3[i]
        print("{}=>('{}', '{}', '{}', {})".format(name[i], subject1[i], subject2[i], subject3[i], cgpa))



