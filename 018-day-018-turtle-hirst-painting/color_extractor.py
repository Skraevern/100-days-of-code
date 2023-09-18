import colorgram


def extract_rgb_as_tuples(color_object):
    """Takes out each rgb value from colorgram object as tuple and returns list"""
    color_list = []
    for i in range(0, len(color_object)):
        rgb = color_object[i].rgb
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        color_list.append((red, green, blue))
    return color_list


# vs code terminal has to be in this folder for it to work
colors = colorgram.extract("hirst.jpeg", 30)

rgb_color_list = extract_rgb_as_tuples(colors)

print(rgb_color_list)
# [(229, 225, 221), (232, 206, 82), (225, 150, 88), (220, 228, 222), (228, 221, 224), (120, 167, 186), (158, 14, 20), (214, 223, 228), (33, 110, 158), (232, 83, 46), (123, 175, 144), (171, 20, 15), (7, 98, 37), (200, 63, 28), (185, 186, 27), (30, 129, 47), (12, 41, 75), (14, 64, 40), (243, 201, 5), (137, 81, 95), (84, 15, 22), (48, 167, 75), (44, 25, 21), (5, 65, 137), (171, 134, 149), (48, 150, 195), (232, 170, 161), (213, 65, 70), (74, 135, 186), (168, 207, 172)]

# removed backroud colors
# [ (232, 206, 82), (225, 150, 88), (120, 167, 186), (158, 14, 20), (33, 110, 158), (232, 83, 46), (123, 175, 144), (171, 20, 15), (7, 98, 37), (200, 63, 28), (185, 186, 27), (30, 129, 47), (12, 41, 75), (14, 64, 40), (243, 201, 5), (137, 81, 95), (84, 15, 22), (48, 167, 75), (44, 25, 21), (5, 65, 137), (171, 134, 149), (48, 150, 195), (232, 170, 161), (213, 65, 70), (74, 135, 186), (168, 207, 172)]
