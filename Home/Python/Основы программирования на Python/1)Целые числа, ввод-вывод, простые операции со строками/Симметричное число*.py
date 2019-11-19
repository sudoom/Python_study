x_4 = int(input())
while x_4 < 10000:
    x_4 = x_4 + 1
    left_part_2 = x_4 // 100
    right_part_2 = x_4 % 100
    left_part_1_r = right_part_2 // 10
    right_part_1_r = right_part_2 % 10
    rev_right_part_2 = str(right_part_1_r) + str(left_part_1_r)
    symmetric_r = (int(rev_right_part_2) + left_part_2 - 1) // left_part_2
    symmetric_l = (int(rev_right_part_2)+left_part_2 - 1) // int(rev_right_part_2)
    print(int(symmetric_l == symmetric_r), x_4)
