import combinations as combs
import sorts as sorts
import searchs as searchs
import BinarySearchTree as BST
import Graph as graph

print(f"Testing: All subsequences")
print(f"--- String")
test1 = ['1', '2', '3', '4']
print(f"INPUT: {test1}")
print(f"OUTPUT:")
to_print = "\n"
for e in combs.allSubsequences_String(test1):
    to_print += "   " + str(e) + "\n"
print(to_print)
print(f"--- Finished ---")

print(f"Testing: All subsequences")
print(f"--- Bits")
test1 = ['1', '2', '3', '4']
print(f"INPUT: {test1}")
print(f"OUTPUT:")
to_print = "\n"
for e in combs.allSubsequences_Bits(test1):
    to_print += "   " + str(e) + "\n"
print(to_print)
print(f"--- Finished ---")

print(f"\nTesting: All Subarrays")
test1 = ['1', '2', '3', '4']
print(f"INPUT: {test1}")
print(f"OUTPUT:")
to_print = "\n"
for e in combs.allSubarrays(test1):
    to_print += "   " + str(e) + "\n"
print(to_print)
print(f"--- Finished ---")

print(f"\nTesting: is Colorful")
print(f"Is colorful {3245}: {combs.isColorful(3245)}")
print(f"Is colorful {10}: {combs.isColorful(10)}")
print(f"Is colorful {326}: {combs.isColorful(326)}")
print(f"--- Finished ---")

print(f"\nTesting: is Colorful with Generator")
print(f"Is colorful {3245}: {combs.isColorful_generator(3245)}")
print(f"Is colorful {10}: {combs.isColorful_generator(10)}")
print(f"Is colorful {326}: {combs.isColorful_generator(326)}")
print(f"--- Finished ---")

print(f"\nTesting: Quicksort")
test1 = [2, 1]
test2 = [1]
test3 = [1, 2, 10, 9, 2, 3, 5, 1, 2, 5, 20]
print(f"Ordered {test1} => {sorts.quicksort(test1)}")
print(f"Ordered {test2} => {sorts.quicksort(test2)}")
print(f"Ordered {test3} => {sorts.quicksort(test3)}")
print(f"--- Finished ---")

print(f"\nTesting: Binary Search Recursive")
test1 = [1, 2]
test2 = [1]
test3 = [1, 2, 10, 19, 20, 30, 50, 100, 200, 250, 2000]
print(f"Search for 2 in {test1} => Pos: {searchs.binary_search_rec(2,test1)}")
print(f"Search for 0 in {test2} => Pos: {searchs.binary_search_rec(0,test2)}")
print(
    f"Search for 200 in {test3} => Pos: {searchs.binary_search_rec(200,test3)}")
print(f"--- Finished ---")

print(f"\nTesting: Binary Search Iterative")
test1 = [1, 2]
test2 = [1]
test3 = [1, 2, 10, 19, 20, 30, 50, 100, 200, 250, 2000]
print(f"Search for 2 in {test1} => Pos: {searchs.binary_search_ite(2,test1)}")
print(f"Search for 0 in {test2} => Pos: {searchs.binary_search_ite(0,test2)}")
print(
    f"Search for 200 in {test3} => Pos: {searchs.binary_search_ite(200,test3)}")
print(f"--- Finished ---")

print(f"\nTesting: Binary Search Tree")
tree = BST.BinarySearchTree()
arr = [4, 2, 3, 1, 7, 6]
for e in arr:
    tree.insert(e)
BST.preOrder(tree.root)
print(f"--- Finished ---\n")


def cost(posa, posb):
    MAX_V = 6
    roll = 0
    while (posa + (MAX_V*roll) + MAX_V) <= posb:
        roll += 1
    if (posa + (MAX_V*roll)) == posb:
        return roll
    else:
        return roll + 1


g = graph.Graph()
g.add_vertex(1)
g.add_vertex(100)


ladders = [[32, 62],
           [42, 68],
           [12, 98]]

snakes = [[95, 13],
          [97, 25],
          [93, 37],
          [79, 27],
          [75, 19],
          [49, 47],
          [67, 17]]

ladders2 = [[3, 54],
            [37, 100]]

snakes2 = [[56, 33]]

for f, t in ladders2 + snakes2:
    g.add_vertex(f)
    g.add_vertex(t)
    g.add_edge(f, t, 0)
    for v in g.get_vertices():
        if v < f and v != t:
            g.add_edge(v, f, cost(v, f))
        if v > t and v != f:
            g.add_edge(t, v, cost(t, v))

g.add_edge(1, 100, cost(1, 100))

print('Graph data:')
for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print(f"( {vid} , {wid}, {v.get_weight(w)})")


path = g.a_star_algorithm(g.get_vertex(1), g.get_vertex(100))


def countRolls(path):
    rolls = 0
    for i in range(len(path)-1):
        v = path[i]
        sv = path[i+1]
        rolls += v.adjacent[sv]
    return rolls


print(countRolls(path))
