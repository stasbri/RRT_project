import random
from objects import Map, Point, Tree, Node, random_point_in_range, new_point, dist
from args import source, limit
from logger import log


my_map = Map(source)


way_found = False

root_point = my_map.start
root = Node(root_point, None)
end_point = my_map.finish

tree = Tree(root)
log(my_map.size[0], my_map.size[1])
print('##########33logged map size')
log(my_map.start)
log(my_map.finish)
while not way_found:
    new_p = random_point_in_range((0, my_map.size[0]), (0, my_map.size[1]))
    best_node, second_best = tree.find_closest_node(new_p)
    new = new_point(best_node.point, new_p, limit)
    second_new = new_point(second_best.point, new_p, limit)
    new_node = Node(new, best_node)
    second_new_node = Node(new, best_node)
    if my_map.is_way(best_node.point, new_node.point):
        tree.add_node(new_node)
        log(str(new_node.point), str(best_node.point))
        if my_map.is_way(new, end_point):
            way_found = True
            tree.add_node(Node(end_point, new_node))
    elif my_map.is_way(second_best.point, second_new_node.point):
        tree.add_node(new_node)
        log(str(new_node.point), str(best_node.point))
        if my_map.is_way(new, end_point):
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



