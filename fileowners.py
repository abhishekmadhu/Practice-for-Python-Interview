#  https://www.testdome.com/d/python-interview-questions/9


def get_key(my_dict, val):
    booklist = []
    for k, v in my_dict.items():
        if val == v:
            booklist.append(k)

    return booklist


def group_by_owners(files):
    names = files.keys()
    authors = files.values()
    # print(names)
    # print(authors)
    d = {}
    for author in authors:
        # print(get_key(files, author))
        d[author] = get_key(files, author)
    return d


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))