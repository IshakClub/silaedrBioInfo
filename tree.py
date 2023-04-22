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
            self.tree[word[0]] = node
            node.make_node(word[1:])
        else:
            self.tree[word[0]].make_node(word[1:])

    def find_node(self, prefix):
        if len(prefix) == 0:
            return self.tree
        first_let = prefix[0]
        if first_let not in self.tree:
            return
        n_node = self.tree[first_let].find_node(prefix[1:])
        if n_node:
            return n_node

    def all_words(self, prefix):
        if self.is_word:
            result = [prefix]
        else:
            result = []
            for let in self.tree:
                child = self.tree[let]
                result += child.all_words(prefix + let)
        return result


tree = Tree(False)

LIST_Of_TEMPLS = ['CATT', 'CAGT', 'ATTG']
for templ in LIST_Of_TEMPLS:
    tree.make_node(templ)


