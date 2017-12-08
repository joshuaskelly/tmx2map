import math
import numpy

class Matrices(object):
    # Helper matrices
    horizontal_flip = numpy.identity(4)
    horizontal_flip[0, 0] = -1

    vertical_flip = numpy.identity(4)
    vertical_flip[1, 1] = -1

    diagonal_flip = numpy.zeros((4, 4))
    diagonal_flip[0, 1] = -1
    diagonal_flip[1, 0] = -1
    diagonal_flip[2, 2] = 1
    diagonal_flip[3, 3] = 1


def angle_between(dest, base):
    """Returns the angle in positive degrees from base to dest in the
    xy-plane.

    dest: A vector
    base: A vector

    Returns:
        Angle in degrees [0, 360)
    """

    target = dest[0], dest[1]
    p_axis = -base[1], base[0]
    b_axis = base[0], base[1]

    x_proj = numpy.dot(target, b_axis)
    y_proj = numpy.dot(target, p_axis)

    return -math.degrees(math.atan2(y_proj, x_proj)) % 360


def vector_from_angle(degrees):
    """Returns a unit vector in the xy-plane rotated by the given degrees from
    the positive x-axis"""
    radians = math.radians(degrees)
    z_rot_matrix = numpy.identity(4)
    z_rot_matrix[0, 0] = math.cos(radians)
    z_rot_matrix[0, 1] = -math.sin(radians)
    z_rot_matrix[1, 0] = math.sin(radians)
    z_rot_matrix[1, 1] = math.cos(radians)

    return tuple(numpy.dot(z_rot_matrix, (1, 0, 0, 0))[:3])