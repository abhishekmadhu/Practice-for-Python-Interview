#  https://www.testdome.com/d/python-interview-questions/9


def unique_names(names1, names2):
    s = set()
    for name in names1:
        s.add(name)
    for name in names2:
        s.add(name)

    ml = [elem for elem in s]
    return ml


names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2), sep=', ')  # should print Ava, Emma, Olivia, Sophia