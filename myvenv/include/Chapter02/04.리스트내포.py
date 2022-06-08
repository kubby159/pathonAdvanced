# 리스트 내포
# for 사용
nums = [i for i in range(5)]
print(nums) #[0, 1, 2, 3, 4]

nums2 = [100,200,300]
double_nums2 = [i * 2 for i in nums2]
print(double_nums2) # [200, 400, 600]


# if 사용
nums3 = [i for i in range(10) if i % 2 == 0]
print(nums3) # [0, 2, 4, 6, 8]

nums4 = [100,200,300,400,500]
double_nums4 = [i * 2 for i in nums4 if i >= 300]
print(double_nums4)