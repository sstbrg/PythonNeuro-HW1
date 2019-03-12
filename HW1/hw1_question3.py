def compare_subjects_within_student(subj1_all_students, subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """

    relevant_students = {x: ('Subject1' if subj1_all_students[x] > subj2_all_students[x]
                             else 'Subject2')
                         for x in subj1_all_students if x in subj2_all_students}
    return relevant_students


if __name__ == '__main__':
    # Question 3
    subj1_all_students = {
        'Laura': 99,
        'Dale': 90,
        'Audrey': 42,
        'Bob': 24,
        'Shelly': 56,
        'Donna': 90,
        'James': 100}

    subj2_all_students = {
        'Laura': 60,
        'Dale': 90,
        'Audrey': 89,
        'Donna': 66,
        'James': 80,
        'Windom': 66,
        'Leland': 85}

    return_value = compare_subjects_within_student(subj1_all_students, subj2_all_students)

    print(f"Question 1 solution: {return_value}")
