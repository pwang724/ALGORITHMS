class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.data)


if __name__ == "__main__":
    a = Node()
    print(a.data)