import matplotlib.pyplot as plt

subjects = input("Enter subjects: ").split()
marks = list(map(int, input("Enter marks: ").split()))

plt.bar(subjects, marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()