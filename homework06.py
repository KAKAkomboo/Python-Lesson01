# TASK 02

class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.__grades:
            self.__grades[subject] = []
        self.__grades[subject].append(grade)

    def get_average(self, subject):
        if subject not in self.__grades:
            return None
        grades = self.__grades[subject]
        return sum(grades) / len(grades) if grades else 0

    def get_ov_average(self):
        all_g = []
        for grades in self.__grades.value():
            all_g.extend(grades)
        return sum(all_g) / len(all_g) if all_g else 0

    def get_t(self):
        t = {}
        for subject in self.__grades:
            t[subject] = self.get_average(subject)
        return t


student = Student("Anna")
student.add_grade("Math", 90)
student.add_grade("Math", 85)
print(student.get_average("Math"))



# task 12

class Candidate:
    def __init__(self, name, party):
        self.name = name
        self.party = party

class VotSystem:
    def __init__(self):
        self.__votes = {}
        self.candidates = {}

    def add_candidate(self, candidate):
        self.candidates[candidate.name] = candidate
        self.__votes[candidate.name] = 0

    def vote(self, candidate_name):
        if candidate_name in self.__votes:
            self.__votes[candidate_name] += 1

    def get_res(self):
        return self.__votes.copy()

    def get_winner(self):
        if not self.__votes:
            return None
        winner = max(self.__votes, key=self.__votes.get)
        return winner

    def get_t(self):
        return sum(self.__votes.values())

voting = VotSystem()
voting.add_candidate(Candidate("John", "Party A"))
voting.vote("John")
print(voting.get_winner())

# task 13

class Workout:
    def __init__(self, typ, duration, calor, date):
        self.typ = typ
        self.duration = duration
        self.calories = calor
        self.date = date

class FitnessT:
    def __init__(self):
        self.workouts = []

    def add_workouts(self, workout):
        self.workouts.append(workout)

    def get_total_calories(self, s_date, e_date):
        total = 0
        for w in self.workouts:
            if s_date <= w.date <= e_date:
                total += w.calories
        return total

    def get_worko_by_type(self, typ):
        return [w for w in self.workouts if w.typ == typ]

    def get_avarage_duration(self):
        if not self.workouts:
            return 0
        total_d = sum(w.duration for w in self.workouts)
        return total_d / len(self.workouts)

tracker = FitnessT()
tracker.add_workouts(Workout("Running", 30, 300, "2024-01-15"))
print(tracker.get_total_calories("2024-01-01", "2024-01-31"))

# task 14

class User:
    def __init__(self, name):
        self.name = name
        self.__friend = set()
        self.__posts = []

    def add_friend(self, user):
        self.__friend.add(user.name)

    def remove_friend(self, user):
        self.__friend.discard(user.name)

    def post(self, mess):
        self.__posts.append(mess)

    def get_posts(self):
        return self.__posts.copy()

    def get_f_count(self):
        return len(self.__friend)

user1 = User("Anna")
user2 = User("John")
user1.add_friend(user2)
print(user1.get_f_count())