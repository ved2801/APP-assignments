import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Enter and structure student marks subject-wise.")
    
    # Accept 5 float/integer marks for each of the 4 subjects
    parser.add_argument('--s1', nargs=5, type=float, required=True, help="Marks for Subject 1 (5 students)")
    parser.add_argument('--s2', nargs=5, type=float, required=True, help="Marks for Subject 2 (5 students)")
    parser.add_argument('--s3', nargs=5, type=float, required=True, help="Marks for Subject 3 (5 students)")
    parser.add_argument('--s4', nargs=5, type=float, required=True, help="Marks for Subject 4 (5 students)")
    
    args = parser.parse_args()
    
    # Combine the subject lists column-wise and transpose, 
    # or use column_stack so each column is a subject and each row is a student.
    marks_matrix = np.column_stack((args.s1, args.s2, args.s3, args.s4))
    
    print("\n--- 2D Marks Array (Rows = Students, Columns = Subjects) ---")
    print(marks_matrix)
    
    # Optional: Display student-wise averages
    print("\nStudent Averages:")
    for i, student_marks in enumerate(marks_matrix, start=1):
        print(f"Student {i}: {np.mean(student_marks):.2f}")

if __name__ == '__main__':
    main()
