class TreeNode:
    def __init__(self, name):
        self.name = name          # Node identifier (e.g., 'A', 'B', etc.)
        self.children = []        # List of child TreeNode objects
        self.parent = None        # Reference to the parent node
        self.locked = False       # Boolean to check if the node is locked
        self.locked_by = None     # ID of the user who locked the node

class Tree:
    def __init__(self, root: TreeNode):
        self.root = root          # Root node of the tree
        self.node_map = {}        # Dictionary to store nodes by their names for quick access

    def add_node(self, parent: TreeNode, child: TreeNode):
        """Add a child to the parent node."""
        child.parent = parent
        parent.children.append(child)
        self.node_map[child.name] = child

    def lock(self, x: str, uid: int) -> bool:
        """Attempt to lock the node `x` for user `uid`."""
        node = self.node_map.get(x)
        if node is None or node.locked:
            return False
        if self._has_locked_ancestor(node) or self._has_locked_descendant(node):
            return False
        node.locked = True
        node.locked_by = uid
        return True

    def unlock(self, x: str, uid: int) -> bool:
        """Unlock the node `x` if it's locked by user `uid`."""
        node = self.node_map.get(x)
        if node is None or not node.locked or node.locked_by != uid:
            return False
        node.locked = False
        node.locked_by = None
        return True

    def upgradeLock(self, x: str, uid: int) -> bool:
        """Upgrade the lock from any locked descendant of node `x` to `x` itself."""
        node = self.node_map.get(x)
        if node is None or node.locked:
            return False
        if not self._has_locked_descendant_by_user(node, uid):
            return False
        # Unlock all locked descendants
        self._unlock_descendants(node, uid)
        # Lock this node
        node.locked = True
        node.locked_by = uid
        return True

    def _has_locked_ancestor(self, node: TreeNode) -> bool:
        """Check if any ancestors of the node are locked."""
        current = node.parent
        while current:
            if current.locked:
                return True
            current = current.parent
        return False

    def _has_locked_descendant(self, node: TreeNode) -> bool:
        """Check if any descendants of the node are locked."""
        for child in node.children:
            if child.locked or self._has_locked_descendant(child):
                return True
        return False

    def _has_locked_descendant_by_user(self, node: TreeNode, uid: int) -> bool:
        """Check if all locked descendants of the node are locked by the same user."""
        locked_descendants = self._get_locked_descendants(node)
        return len(locked_descendants) > 0 and all(n.locked_by == uid for n in locked_descendants)

    def _get_locked_descendants(self, node: TreeNode) -> list:
        """Get a list of all locked descendants of the node."""
        locked_nodes = []
        for child in node.children:
            if child.locked:
                locked_nodes.append(child)
            locked_nodes.extend(self._get_locked_descendants(child))
        return locked_nodes

    def _unlock_descendants(self, node: TreeNode, uid: int):
        """Unlock all locked descendants of the node by user `uid`."""
        for child in node.children:
            if child.locked and child.locked_by == uid:
                child.locked = False
                child.locked_by = None
            self._unlock_descendants(child, uid)

# Example usage:
root = TreeNode("root")
tree = Tree(root)
tree.node_map["root"] = root

# Building the tree
node_a = TreeNode("A")
tree.add_node(root, node_a)

node_b = TreeNode("B")
tree.add_node(node_a, node_b)

node_c = TreeNode("C")
tree.add_node(node_a, node_c)

# Perform operations
print(tree.lock("B", 1))        # True
print(tree.lock("A", 2))        # False (ancestor is locked)
print(tree.unlock("B", 1))      # True
print(tree.lock("A", 2))        # True (now it's unlocked)
print(tree.lock("C", 2))        # True
print(tree.upgradeLock("A", 2)) # True (upgrade succeeds)
