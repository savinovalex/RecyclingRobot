

class RecyclingModel(object):

    actions = ('UP', 'RIGHT', 'DOWN', 'LEFT')

    move_directions = {'UP': (-1, 0), 'RIGHT': (0, 1), 'DOWN': (1, 0), 'LEFT': (0, -1)}

    def __init__(self, field_size):
        self.field_size = field_size

    def get_new_state(self, s, direction):
        move_delta = RecyclingModel.move_directions[direction]

        s_moved = (s[0] + move_delta[0], s[1] + move_delta[1])

        if 0 <= s_moved[0] and s_moved[0] < self.field_size[0] and 0 <= s_moved[1] and s_moved[1] < self.field_size[1]:
            return s_moved
        else:
            return None

