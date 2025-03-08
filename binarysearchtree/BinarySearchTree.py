from .Node import Node

class BinarySearchTree:
    root: 'Node' = None

    def __init__(self, value: int = None):
        if value != None:
            self.root = Node(value)


    def __insert_node_value(self, node: Node, value: int):
        if value == node.value:
            raise(ValueError('Cannot insert duplicate value'))
        if value < node.value:
            if not node.left:
                node.left = Node(value)
                return self
            else:
                return self.__insert_node_value(node.left, value)
        else:
            if not node.right:
                node.right = Node(value)
                return self
            else:
                return self.__insert_node_value(node.right, value)

    def insert(self, value):
        '''
        This is a robust implementation of a method to insert a
        value into the BST using recursion
        '''
        if not self.root:
            self.root = Node(value)
            return self

        return self.__insert_node_value(self.root, value)

    def linear_insert(self, value):
        '''
        This is a naive implementation of a method to insert a
        value into the BST with a while loop
        This version may actually be preferred, as recursive
        abstractions can be really hard to deterministically test
        '''
        node = Node(value)
        if not self.root:
            self.root = node
            return self

        current = self.root
        while current:
            if value == current.value:
                raise(ValueError('Cannot insert duplicate value'))
            if value < current.value:
                if not current.left:
                    current.left = node
                    return self
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = node
                    return self
                else:
                    current = current.right

    def __node_contains(self, node: Node, value: int):
        if not node:
            return False

        if value == node.value:
            return True
        elif value < node.value and node.left:
            return self.__node_contains(node.left, value)
        else:
            return self.__node_contains(node.right, value)

    def contains(self, value):
        '''
        This is a robust implementation to check whether the BST contains
        a value using recursion
        '''
        if not self.root:
            return False

        return self.__node_contains(self.root, value)


    def linear_contains(self, value):
        '''
        This is a naive implementation to check whether the BST contains
        a value using a while loop
        '''
        if not self.root:
            return False

        current = self.root

        while current:
            if value == current.value:
                return True
            elif  value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def min_value(self, node: Node):
        while node.left is not None:
            node = node.left

        return node.value

    def __delete_node(self, node: Node, value: int):
        if not node:
            return None

        if value < node.value:
            node.left = self.__delete_node(node.left, value)
        elif value > node.value:
            node.right = self.__delete_node(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                sub_tree_min = self.min_value(node.right)
                node.value = sub_tree_min
                node.right = self.__delete_node(node.right, sub_tree_min)

        return node

    def delete(self, value: int):
        self.root = self.__delete_node(self.root, value)

    def breadth_first_search_traversal(self):
        '''
        Traverse the entire BST and return a list of all
        values via breadth first.
        '''
        current = self.root

        queue = []
        result = []

        while (current):
            result.append(current.value)
            if (current.left):
                queue.append(current.left)
            if (current.right):
                queue.append(current.right)
            current = queue.pop(0) if len(queue) > 0 else None

        return result

    def depth_first_search_traversal_preorder(self):
        if (not self.root):
            return []

        results = []

        def traverse_depth(node: Node):
            results.append(node.value)

            if node.left:
                traverse_depth(node.left)
            if node.right:
                traverse_depth(node.right)

        traverse_depth(self.root)

        return results

    def depth_first_search_traversal_postorder(self):
        if (not self.root):
            return []

        results = []

        def traverse_depth_postorder(node: Node):
            if node.left:
                traverse_depth_postorder(node.left)

            if node.right:
                traverse_depth_postorder(node.right)

            results.append(node.value)

        traverse_depth_postorder(self.root)

        return results

    def depth_first_search_traversal_inorder(self):
        if (not self.root):
            return []

        results = []

        def traverse_depth_inorder(node: Node):
            if node.left:
                traverse_depth_inorder(node.left)

            results.append(node.value)

            if node.right:
                traverse_depth_inorder(node.right)

        traverse_depth_inorder(self.root)

        return results
