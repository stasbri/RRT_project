import json


class logger:
    def __init__(self, log_file: str):
        self.logs = dict()
        self.logs['verts'] = []
        self.log_file = log_file
        self.logs['path'] = []

    def read_size(self, x, y):
        self.logs['size'] = [x, y]

    def read_start(self, x, y):
        self.logs['start'] = [x, y]

    def read_finish(self, x, y):
        self.logs['finish'] = [x, y]

    def read_new_vert(self, x1, y1, x2, y2):
        self.logs['verts'].append(['+', x1, y1, x2, y2])

    def read_del_vert(self, x1, y1, x2, y2):
        self.logs['verts'].append(['-', x1, y1, x2, y2])

    def read_path_vert(self, x1, y1, x2, y2):
        self.logs['path'].append([x1, y1, x2, y2])

    def __del__(self):
        f = open(self.log_file, 'w')
        f.write(json.dumps(self.logs))
        f.close()
