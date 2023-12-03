# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
# ~=#=~ ADVENT OF CODE 2023 ~=#=~
# ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
#
# Day 01: Trebuchet
# https://adventofcode.com/2023/day/1
#
# Author: Lucas Queiroz (Firemanarg)

import re

def main():
	input_file = open("input.txt", "r")
	sum = 0
	for line in input_file.readlines():
		nums = re.findall(r'\d', line)
		sum += int(nums[0] + nums[-1])
	print(sum)


main()
