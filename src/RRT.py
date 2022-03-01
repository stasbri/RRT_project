import random
from functions import random_point_in_range, new_point, dist
from objects import Map, Point, Tree, Node
from args import source, limit
from logger import log


map = Map(source)


way_found = False

root_point = map.start
root = Node(root_point, None)
end_point = map.finish

tree = Tree(root)

log(map.size[0], map.size[1])
log(map.start)
log(map.finish)
while not way_found:
    new_p = random_point_in_range((0, map.size[0]), (0, map.size[1]))
    best_node = tree.find_closest_node(new_p)
    new = new_point(best_node.point, new_p, limit)
    new_node = Node(new, best_node)
    if map.is_way(best_node.point, new_node.point):
        tree.add_node(new_node)
        log(str(new_node.point), str(best_node.point))
        if dist(new, end_point) < limit:
            way_found = True
            tree.add_node(Node(end_point, new_node))


n = tree.tree[-1]
path = list()
path.append(n)
log('path')
while n.ans is not None:
    log(n.point, n.ans.point)
    n = n.ans
    path.append(n)



