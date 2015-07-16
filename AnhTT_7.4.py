# a = [3,2,1]
# b = []
# c = []
#
# a = [3,2]
# b = []
# c = [1]
#
# a = [3]
# b = [2]
# c = [1]
#
# a = [3]
# b = [2,1]
# c = []
#
# a = []
# b = [2,1]
# c = [3]
#
# a = [1]
# b = [2]
# c = [3]
#
# a = [1]
# b = []
# c = [3,2]
#
# a = []
# b = []
# c = [3,2,1]


def change_tower_role(n, a, c, b):
    if n >= 1:
        change_tower_role(n-1, a, b, c)
        move_disk(a, c)
        change_tower_role(n-1, b, c, a)


def move_disk(s_tower, d_tower):
    disk = s_tower.pop()
    d_tower.append(disk)
    print a
    print c
    print b
    print ''


if __name__ == '__main__':
    a = [3,2,1]
    b = []
    c = []

    print a
    print b
    print c
    print ''

    change_tower_role(len(a),a,b,c)
