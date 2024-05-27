class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        add = 0
        ref = {}

        for i in range(len(list1)):
            if list1[i] in list2:
                add = i + list2.index(list1[i])
                ref[list1[i]] = add 
            add = 0 

        return [k[0] for k in ref.items() if k[1] == min(ref.values())]
