import time
from typing import List

from objects import Map, Tree, Node, random_point_in_range, new_point, dist
from args import source
from logger import log
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

tree = Tree(root)
log(my_map.size[0], my_map.size[1])
print('##########33logged map size')
log(my_map.start)
log(my_map.finish)
t = time.time()
while not way_found:
    new_p = random_point_in_range((0, my_map.size[0]), (0, my_map.size[1]))
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
                node.ans = new_node

    tree.add_node(new_node)
    # log(str(new_node.point), str(best_node.point))
    if my_map.new_point(new, new_point(new, end_point, limit)) == end_point:
        way_found = True
        tree.add_node(Node(end_point, new_node))


print('finished RRT* search, time =', time.time() - t)
for node in tree.tree:
    if node.ans is not None:
        log(str(node.point), str(node.ans.point))
n = tree.tree[-1]
print(n.cost())
path = list()
path.append(n)
log('path')
while n.ans is not None:
    log(n.point, n.ans.point)
    n = n.ans
    path.append(n)



