from urllib.parse import non_hierarchical


class Node:

    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None