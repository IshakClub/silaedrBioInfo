class Tree:
    def __init__(self, is_word):
        self.is_word = is_word
        self.tree = {}

    def make_node(self, word):
        if len(word) == 0:
            self.is_word = True
            return
        node = Tree(False)
        if word[0] not in self.tree:
            self.tree[word[0]] = (node,)
        else:
            self.tree[word[0]] += (node,)
        node.make_node(word[1:])

    def find_node(self, prefix):
        if len(prefix) == 0:
            return self.tree
        first_let = prefix[0]
        if first_let not in self.tree:
            return
        for node in self.tree[first_let]:
            n_node = node.find_node(prefix[1:])
            if n_node:
                return n_node

    def all_words(self):
        if self.is_word:
            return ''
        for let in self.tree:
            word = let
            for node in self.tree[let]:
                word += node.all_words()
                return word


tree = Tree(False)
tree.make_node('qwe')
tree.make_node('qyy')
tree.make_node('aww')
print(tree.find_node('qy'))
print(tree.all_words())