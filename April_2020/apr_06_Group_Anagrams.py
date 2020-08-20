class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in res_dict:
                res_dict[sorted_word] = []
            res_dict[sorted_word].append(word)

        return res_dict.values()