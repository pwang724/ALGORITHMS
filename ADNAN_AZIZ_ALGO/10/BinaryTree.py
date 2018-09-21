class BinaryTree:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

if __name__ == "__main__":
    a = BinaryTree()
    print(a.data)