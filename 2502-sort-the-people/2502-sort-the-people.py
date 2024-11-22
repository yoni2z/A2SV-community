class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        length = len(heights) - 1
        sorted = False

        while not sorted:
            sorted = True
            for i in range(0, length):
                if heights[i] < heights[i + 1]:
                    sorted = False
                    heights[i], heights[i + 1] = heights[i + 1], heights[i]
                    names[i], names[i + 1] = names[i + 1], names[i]

        return names