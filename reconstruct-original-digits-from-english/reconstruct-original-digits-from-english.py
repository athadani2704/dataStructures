class Solution:
    def originalDigits(self, s: str) -> str:
        mappings = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
        freq = {}
        for val in s:
            freq[val] = freq.get(val, 0)+1
        result = ""
        if "z" in freq:
            result += freq["z"]*"0"
            freq["e"] -= freq["z"]
            freq["r"] -= freq["z"]
            freq["o"] -= freq["z"]
        if "w" in freq:
            result += freq["w"]*"2"
            freq["t"] -= freq["w"]
            freq["o"] -= freq["w"]
        if "x" in freq:
            result += freq["x"]*"6"
            freq["i"] -= freq["x"]
            freq["s"] -= freq["x"]
        if "u" in freq:
            result += freq["u"]*"4"
            freq["f"] -= freq["u"]
            freq["o"] -= freq["u"]
            freq["r"] -= freq["u"]
        if "r" in freq and freq["r"]>0:
            result += freq["r"]*"3"
            freq["t"] -= freq["r"]
            freq["h"] -= freq["r"]
            freq["e"] -= freq["r"]*2
        if "o" in freq and freq["o"]>0:
            result += freq["o"]*"1"
            freq["n"] -= freq["o"]
            freq["e"] -= freq["e"]
        if "g" in freq:
            result += freq["g"]*"8"
            freq["i"] -= freq["g"]
            freq["e"] -= freq["g"]
            freq["h"] -= freq["g"]
            freq["t"] -= freq["g"]
        if "f" in freq and freq["f"]>0:
            result += freq["f"]*"5"
            freq["i"] -= freq["f"]
            freq["e"] -= freq["f"]
        if "s" in freq and freq["s"]>0:
            result += freq["s"]*"7"
            freq["n"] -= freq["s"]
        if "i" in freq and freq["i"]>0:
            result += freq["i"]*"9"
        return "".join(sorted(result))