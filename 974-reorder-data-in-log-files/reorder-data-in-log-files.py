class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digi = []
        letter = []

        for log in logs:
            if log[-1].isdigit():
                
                digi.append(log)
            else:
                letter.append(log)

        letter.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))

        return letter + digi
