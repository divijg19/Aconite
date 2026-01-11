# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/

def flip_and_invert_image(image):
    for row in image:
        for i in range((len(row) + 1) // 2):
            row[i], row[-i - 1] = 1 - row[-i - 1], 1 - row[i]
    return image
