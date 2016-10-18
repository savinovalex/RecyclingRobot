

class RecyclingEnviroment(object):

    actions = ('UP', 'RIGHT', 'DOWN', 'LEFT')

    move_directions = {'UP': (-1, 0), 'RIGHT': (0, 1), 'DOWN': (1, 0), 'LEFT': (0, -1)}

    def __init__(self, field_size, start_point, target_point):
        self.field_size = field_size
        self.current_point = start_point
        self.start_point = start_point
        self.target_point = target_point

    def get_current_state(self):
        return self.current_point

    def reset(self):
        self.current_point = self.start_point

    def apply_action(self, direction):
        moveDelta = RecyclingEnviroment.move_directions[direction]

        s = self.current_point
        s_moved = (s[0] + moveDelta[0], s[1] + moveDelta[1])
        self.current_point = s_moved

        if not(0 <= s_moved[0] and s_moved[0] < self.field_size[0] and 0 <= s_moved[1] and s_moved[1] < self.field_size[1]):
            return None

        if s_moved == self.target_point:
            return s_moved, 1

        return s_moved, 0

    def is_terminated(self):
        return self.current_point == self.target_point