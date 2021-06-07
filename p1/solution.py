import string


def solution(x):
    # Your code here
    model = dict(zip(string.ascii_lowercase, string.ascii_lowercase[::-1]))
    decipher = ''
    for i in x:
        decipher += model.get(i, i)
    return decipher


print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
