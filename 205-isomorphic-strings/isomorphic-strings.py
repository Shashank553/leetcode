class Solution(object):
    def isIsomorphic(self, s, t):
        notebook1 = {}  # s -> t
        notebook2 = {}  # t -> s

        for i in range(len(s)):
            person = s[i]
            nickname = t[i]

            # If both are new, write in notebook
            if person not in notebook1 and nickname not in notebook2:
                notebook1[person] = nickname
                notebook2[nickname] = person

            # If person is old, but nickname is different -> Wrong
            elif notebook1.get(person) != nickname:
                return False

            # If nickname is old, but person is different -> Wrong
            elif notebook2.get(nickname) != person:
                return False

        return True