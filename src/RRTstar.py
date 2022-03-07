import time
from typing import List

from objects import Map, Tree, Node, new_point, dist
from args import source
from logger import logger
import sys

from math import inf

args = sys.argv
if len(args) > 1:
    source = int(args[1])

my_map = Map(source)
limit = my_map.limit



way_found = False

root_point = my_map.start
root = Node(root_point, None)
end_point = my_map.finish

logger = logger('src/logs.json')

tree = Tree(root)
logger.read_size(my_map.size[0], my_map.size[1])
logger.read_start(my_map.start.x, my_map.start.y)
logger.read_finish(my_map.finish.x, my_map.finish.y)
t = time.time()
while not way_found:
    new_p = my_map.random_point_in_range()
    best_node = tree.find_closest_node(new_p)

    new = new_point(best_node.point, new_p, limit)

    new = my_map.new_point(best_node.point, new)
    c = dist(best_node.point, new) + best_node.cost()
    close_nodes: List[Node] = tree.close_nodes(new, limit)
    for node in close_nodes:
        if dist(new, node.point) + node.cost() < c:
            if my_map.is_way(node.point, new):
                c = dist(new, node.point) + node.cost()
                best_node = node

    new_node = Node(new, best_node)
    for node in close_nodes:
        if dist(new, node.point) + new_node.cost() < node.cost():
            if my_map.is_way(new, node.point):
                logger.read_del_vert(*(node.point.as_nums() + node.ans.point.as_nums()))
                node.ans = new_node
                logger.read_new_vert(*(new_node.point.as_nums() + node.point.as_nums()))


    tree.add_node(new_node)
    # log(str(new_node.point), str(best_node.point))
    logger.read_new_vert(*(best_node.point.as_nums() + new_node.point.as_nums()))
    if my_map.new_point(new, new_point(new, end_point, limit)) == end_point:
        way_found = True
        tree.add_node(Node(end_point, new_node))


print('finished RRT* search, time =', time.time() - t)

n = tree.tree[-1]
print(n.cost())
path = list()
path.append(n)

while n.ans is not None:
    logger.read_path_vert(* (n.point.as_nums() + n.ans.point.as_nums()))
    n = n.ans
    path.append(n)



