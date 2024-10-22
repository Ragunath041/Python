from collections import deque

class Tree:
    def __init__(self, name, head=None):
        self.name = name
        self.head = head
        self.childrens = []
        self.islocked = False
        self.locked_by = -1
        self.descendants_locked = 0 # Number of locked descendants

    def add_children(self, children_names):
        for name in children_names:
            self.childrens.append(Tree(name, self))

class TreeManager:
    def __init__(self, root_name):
        self.root = Tree(root_name)
        self.node_map = {root_name: self.root}

    def build_tree(self, node_names, max_children):
        queue = deque([self.root])
        idx = 1
        total_nodes = len(node_names)
        
        while queue and idx < total_nodes:
            current_node = queue.popleft()
            for _ in range(max_children):
                if idx >= total_nodes:
                    break
                child_name = node_names[idx]
                child_node = Tree(child_name, current_node)
                current_node.childrens.append(child_node)
                self.node_map[child_name] = child_node
                queue.append(child_node)
                idx += 1

    def can_lock_or_upgrade(self, node):
        # Check if the node or any of its ancestors are locked
        current = node.head
        while current:
            if current.islocked:
                return False
            current = current.head
        return True

    def lock(self, name, user_id):
        node = self.node_map[name]
        if node.islocked or node.descendants_locked > 0:
            return False
        if not self.can_lock_or_upgrade(node):
            return False

        # Lock the node
        node.islocked = True
        node.locked_by = user_id

        # Update ancestors
        current = node.head
        while current:
            current.descendants_locked += 1
            current = current.head

        return True

    def unlock(self, name, user_id):
        node = self.node_map[name]
        if not node.islocked or node.locked_by != user_id:
            return False

        # Unlock the node
        node.islocked = False
        node.locked_by = -1

        # Update ancestors
        current = node.head
        while current:
            current.descendants_locked -= 1
            current = current.head

        return True

    def upgrade(self, name, user_id):
        node = self.node_map[name]
        if node.islocked or node.descendants_locked == 0:
            return False
        if not self.can_lock_or_upgrade(node):
            return False

        # Check if all locked descendants are locked by the same user
        def can_upgrade(node):
            if node.islocked and node.locked_by != user_id:
                return False
            for child in node.childrens:
                if not can_upgrade(child):
                    return False
            return True

        if not can_upgrade(node):
            return False

        # Unlock all locked descendants
        def unlock_all(node):
            if node.islocked:
                self.unlock(node.name, user_id)
            for child in node.childrens:
                unlock_all(child)

        unlock_all(node)

        # Lock the current node
        return self.lock(name, user_id)

# Input and execution part
size = int(input())
max_children = int(input())
test_cases = int(input())
node_names = input().split()

tree_manager = TreeManager(node_names[0])
tree_manager.build_tree(node_names, max_children)

for _ in range(test_cases):
    query_type, node_name, user_id = input().split()
    user_id = int(user_id)

    if query_type == '1':  # Lock
        print("true" if tree_manager.lock(node_name, user_id) else "false")
    elif query_type == '2':  # Unlock
        print("true" if tree_manager.unlock(node_name, user_id) else "false")
    elif query_type == '3':  # Upgrade
        print("true" if tree_manager.upgrade(node_name, user_id) else "false")
