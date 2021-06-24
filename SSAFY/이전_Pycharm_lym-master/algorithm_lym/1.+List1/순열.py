for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)

# 중복순열
# # N = 3 # 1 ~ 4
# # W = 4
# # B= [0] * 4
# #
# # for B[0] in range(0, W):
# #     for B[1] in range(0, W):
# #         for B[2] in range(0, W):
# #             for B[3] in range(0, W):
# #                 print(B)
# #                 if N < 4: break
# #             if N < 3: break
# #         if N < 2: break