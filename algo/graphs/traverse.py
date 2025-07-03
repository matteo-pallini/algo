"""
The main difference between the two approaches is that with bfs we use a queue,
 while with dfs we use a stack
"""


def bfs(graph_root, searched_value):
    queue, visited = [graph_root], set()
    while queue:
        node = queue.pop(0)
        if node:
            visited.add(node)
            if node.value == searched_value:
                return node
            for linked_node in node.linked_nodes:
                if linked_node not in visited:
                    queue.append(linked_node)


def dfs(graph_root, searched_value):
    stack, visited = [graph_root], set()
    while stack:
        node = stack.pop()
        if node:
            visited.add(node)
            if node.value == searched_value:
                return node
            for linked_node in node.linked_nodes:
                if linked_node not in visited:
                    stack.append(linked_node)
