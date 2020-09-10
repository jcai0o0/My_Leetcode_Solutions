class Solution_1:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        m = max(len(v1), len(v2))
        for i in range(m):
            temp1, temp2 = 0, 0
            if i < len(v1):
                temp1 = int(v1[i])
            if i < len(v2):
                temp2 = int(v2[i])
            if temp1 < temp2:
                return -1
            elif temp1 > temp2:
                return 1
        return 0

class Solution_2:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1, n2 = len(nums1), len(nums2)

        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            print(i1, i2)
            if i1 != i2:
                return 1 if i1 > i2 else -1

        # the versions are equal
        return 0