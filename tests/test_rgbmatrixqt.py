# SPDX-FileCopyrightText: 2021 Rose Hooper
# SPDX-License-Identifier: MIT

"""
Basic tests for the adafruit_is31fl3741 driver.
"""

from adafruit_is31fl3741.adafruit_rgbmatrixqt import Adafruit_RGBMatrixQT

EXPECTED_RGBMATRIXQT_COORDS = {
    (0, 0): (240, 242, 241),
    (1, 0): (245, 244, 243),
    (2, 0): (246, 248, 247),
    (3, 0): (251, 250, 249),
    (4, 0): (252, 254, 253),
    (5, 0): (257, 256, 255),
    (6, 0): (258, 260, 259),
    (7, 0): (263, 262, 261),
    (8, 0): (264, 266, 265),
    (9, 0): (269, 268, 267),
    (10, 0): (342, 344, 343),
    (11, 0): (347, 346, 345),
    (12, 0): (350, 349, 348),
    (0, 1): (150, 152, 151),
    (1, 1): (155, 154, 153),
    (2, 1): (156, 158, 157),
    (3, 1): (161, 160, 159),
    (4, 1): (162, 164, 163),
    (5, 1): (167, 166, 165),
    (6, 1): (168, 170, 169),
    (7, 1): (173, 172, 171),
    (8, 1): (174, 176, 175),
    (9, 1): (179, 178, 177),
    (10, 1): (315, 317, 316),
    (11, 1): (320, 319, 318),
    (12, 1): (323, 322, 321),
    (0, 2): (120, 122, 121),
    (1, 2): (125, 124, 123),
    (2, 2): (126, 128, 127),
    (3, 2): (131, 130, 129),
    (4, 2): (132, 134, 133),
    (5, 2): (137, 136, 135),
    (6, 2): (138, 140, 139),
    (7, 2): (143, 142, 141),
    (8, 2): (144, 146, 145),
    (9, 2): (149, 148, 147),
    (10, 2): (306, 308, 307),
    (11, 2): (311, 310, 309),
    (12, 2): (314, 313, 312),
    (0, 3): (90, 92, 91),
    (1, 3): (95, 94, 93),
    (2, 3): (96, 98, 97),
    (3, 3): (101, 100, 99),
    (4, 3): (102, 104, 103),
    (5, 3): (107, 106, 105),
    (6, 3): (108, 110, 109),
    (7, 3): (113, 112, 111),
    (8, 3): (114, 116, 115),
    (9, 3): (119, 118, 117),
    (10, 3): (297, 299, 298),
    (11, 3): (302, 301, 300),
    (12, 3): (305, 304, 303),
    (0, 4): (60, 62, 61),
    (1, 4): (65, 64, 63),
    (2, 4): (66, 68, 67),
    (3, 4): (71, 70, 69),
    (4, 4): (72, 74, 73),
    (5, 4): (77, 76, 75),
    (6, 4): (78, 80, 79),
    (7, 4): (83, 82, 81),
    (8, 4): (84, 86, 85),
    (9, 4): (89, 88, 87),
    (10, 4): (288, 290, 289),
    (11, 4): (293, 292, 291),
    (12, 4): (296, 295, 294),
    (0, 5): (30, 32, 31),
    (1, 5): (35, 34, 33),
    (2, 5): (36, 38, 37),
    (3, 5): (41, 40, 39),
    (4, 5): (42, 44, 43),
    (5, 5): (47, 46, 45),
    (6, 5): (48, 50, 49),
    (7, 5): (53, 52, 51),
    (8, 5): (54, 56, 55),
    (9, 5): (59, 58, 57),
    (10, 5): (279, 281, 280),
    (11, 5): (284, 283, 282),
    (12, 5): (287, 286, 285),
    (0, 6): (0, 2, 1),
    (1, 6): (5, 4, 3),
    (2, 6): (6, 8, 7),
    (3, 6): (11, 10, 9),
    (4, 6): (12, 14, 13),
    (5, 6): (17, 16, 15),
    (6, 6): (18, 20, 19),
    (7, 6): (23, 22, 21),
    (8, 6): (24, 26, 25),
    (9, 6): (29, 28, 27),
    (10, 6): (270, 272, 271),
    (11, 6): (275, 274, 273),
    (12, 6): (278, 277, 276),
    (0, 7): (210, 212, 211),
    (1, 7): (215, 214, 213),
    (2, 7): (216, 218, 217),
    (3, 7): (221, 220, 219),
    (4, 7): (222, 224, 223),
    (5, 7): (227, 226, 225),
    (6, 7): (228, 230, 229),
    (7, 7): (233, 232, 231),
    (8, 7): (234, 236, 235),
    (9, 7): (239, 238, 237),
    (10, 7): (333, 335, 334),
    (11, 7): (338, 337, 336),
    (12, 7): (341, 340, 339),
    (0, 8): (180, 182, 181),
    (1, 8): (185, 184, 183),
    (2, 8): (186, 188, 187),
    (3, 8): (191, 190, 189),
    (4, 8): (192, 194, 193),
    (5, 8): (197, 196, 195),
    (6, 8): (198, 200, 199),
    (7, 8): (203, 202, 201),
    (8, 8): (204, 206, 205),
    (9, 8): (209, 208, 207),
    (10, 8): (324, 326, 325),
    (11, 8): (329, 328, 327),
    (12, 8): (332, 331, 330),
}


def test_matrix_qt_coordinates():
    """
    Tests that the RGBMatrixQT board coordinate mapping behaves as expected.
    """
    coords = {}
    for y in range(Adafruit_RGBMatrixQT.height):
        for x in range(Adafruit_RGBMatrixQT.width):
            coords[x, y] = Adafruit_RGBMatrixQT.pixel_addrs(x, y)

    assert len(coords) == len(EXPECTED_RGBMATRIXQT_COORDS)
    for x_y, rgb in coords.items():
        assert x_y in EXPECTED_RGBMATRIXQT_COORDS
        assert EXPECTED_RGBMATRIXQT_COORDS[x_y] == rgb
