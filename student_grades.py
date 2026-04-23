from sorting import random_numbers


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        pocet_bodu = self.get_by_index(index)
        if pocet_bodu >= 90:
            return "A"
        elif 80 <= pocet_bodu >= 89:
            return "B"
        elif 70 <= pocet_bodu >= 79:
            return "C"
        elif 60 <= pocet_bodu >= 69:
            return "D"
        elif 50 <= pocet_bodu >= 59:
            return "E"
        else:
            return "F"

    def find(self, pocet_bodu):
        zoznam = []
        for i in range(len(self.scores)):
            if self.scores[i] == pocet_bodu:
                zoznam.append(i)
        return zoznam

    def get_sorted(self):
        scores = self.scores.copy()
        while True:
            zmena = 0
            for i in range(len(scores) - 1):
                if scores[i] > scores[i + 1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]
                    zmena += 1
            if zmena == 0:
                break
        return scores

# results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

# print(results.count())          # 9
# print(results.get_by_index(2))  # 91
# print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]
#
# print(results.get_grade(2))  # A (91 bodů)
# print(results.get_grade(6))  # A (100 bodů)
# print(results.get_grade(7))  # F (38 bodů)

# print(results.find(100))  # [6]
# print(results.find(50))   # [4]
# print(results.find(77))   # []
# print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]
# print(results.scores)         # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(f"{results.count()} students.")
    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")
    print(f"Indexes of students with 100 points: {results.find(100)}")
    print(f"Sorted results: {results.get_sorted()}")


main()
random_results = StudentsGrades(random_numbers(30, 0, 100))
print(random_results.count())
print(random_results.get_sorted())