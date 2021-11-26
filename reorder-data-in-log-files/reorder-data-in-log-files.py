from string import ascii_lowercase as al

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = {}
        result = []
        for log in logs:
            if log.split()[1][0] in al:
                x = " ".join(log.split()[1:])
                let[x] = let.get(x, [])+[log]
        for key in sorted(let.keys()):
            result.extend(sorted(let[key]))
        for log in logs:
            if log.split()[1][0] not in al:
                result.append(log)
        return result
        