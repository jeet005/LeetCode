class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        output = 0
        for i in range(len(colors) - 1):
            if colors[i] != colors[i-1] and colors[i]!= colors[i+1]:
                output += 1
        print(output)
        if (colors[0] != colors[1] and colors[0] != colors[-1]) or colors[-1] != colors[-2] and colors[-1] != colors[0]:
            output += 1
        return output
        