package leetcode

func checkPossibility(nums []int) bool {
	index := -1
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] > nums[i+1] {
			if -1 != index {
				return false
			}
			index = i
		}
	}
	return -1 == index || 0 == index || len(nums)-2 == index || nums[index-1] <= nums[index+1] || nums[index] <= nums[index+2]
}
