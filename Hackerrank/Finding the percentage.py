# You have a record of N students. Each record contains the student's name, 
# and their percent marks in Maths, Physics and Chemistry. 
# The marks can be floating values. The user enters some integer N followed by the names
#  and marks for N students. 
#  You are required to save the record in a dictionary data type. 
#  The user then enters a student's name. 
#  Output the average percentage marks obtained by that student, 
#  correct to two decimal places.

# Input Format

# The first line contains the integer N, the number of students. 
# The next N lines contains the name and marks obtained by that student separated by a space.
# The final line contains the name of a particular student previously listed.


# Sample Input

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output

# 56.00 (Malika's Average)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    students = list(student_marks)
    keys_marks = student_marks[query_name]
    result = sum(keys_marks) / len(keys_marks)
    print("{0:.2f}".format(round(result, 2)))
