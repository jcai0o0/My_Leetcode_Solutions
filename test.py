def numTriplets(nums1, nums2):
    if not nums1 or not nums2:
        return 0
    res = 0
    dic1 = {}
    for i in range(len(nums1)):
        if nums1[i] in dic1:
            res += dic1[nums1[i]]
        else:
            mul = nums1[i] * nums1[i]
            cnt = 0
            for j in range(len(nums2)):
                b = mul // nums2[j]
                temp = nums2[j + 1:].count(b)
                cnt += temp
            dic1[nums1[i]] = cnt
            res += cnt

    dic2 = {}
    for i in range(len(nums2)):
        if nums2[i] in dic2:
            res += dic2[nums2[i]]
        else:
            mul = nums2[i] * nums2[i]
            cnt = 0
            for j in range(len(nums1)):
                b = mul // nums1[j]
                temp = nums1[j + 1:].count(b)
                cnt += temp
            dic2[nums2[i]] = cnt
            res += cnt
    return res

if __name__ == "__main__":
    ans = numTriplets([7,4], [5,2,8,9])
    print(ans)