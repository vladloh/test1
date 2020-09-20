import heapq
from nltk import word_tokenize, pos_tag
import tqdm

class Node:
    def __init__(self):
        self.word = ""
        self.children = {}
        self.count = 0
        self.sorted_subnodes = []

    def __lt__(self, other):
        return (-self.count, self.word) < (-other.count, other.word)

    def go(self, c):
        if c not in self.children:
            new_node = Node()
            self.children[c] = new_node
        return self.children[c]

    def assign_word(self, word):
        self.word = word

    def get_child(self, c):
        if c in self.children:
            return self.children[c]
        else:
            return None

    def inc(self, count=1):
        self.count += count

    def precalc_sorted_subnodes(self):
        merging_lists = []
        if self.count > 0:
            merging_lists.append([self])

        for (c, child) in self.children.items():
            child.precalc_sorted_subnodes()
            merging_lists.append(child.sorted_subnodes)

        self.sorted_subnodes = list(heapq.merge(*merging_lists))



class PrefixTree:
    def __init__(self):
        self.root = Node()

    def add_word(self, word, count):
        vertex = self.root
        for i in range(len(word)):
            vertex = vertex.go(word[i])
            vertex.assign_word(word[:i+1])
        vertex.inc(count)

    def add_dictionary(self, dictionary):
        for (word, count) in dictionary.items():
            self.add_word(word, count)

    def precalc_sorted(self):
        self.root.precalc_sorted_subnodes()


    def find_vertex(self, word):
        vertex = self.root
        for i in range(len(word)):
            vertex = vertex.get_child(word[i])
            if not vertex: break
        return vertex

    def count_word(self, word):
        vertex = self.find_vertex(word)
        if vertex:
            return vertex.count
        else:
            return 0


class Autocompletor:
    def __init__(self):
        self.dictionary = {}
        self.tree = PrefixTree()

    def tokenize(self, text):
        tokens = word_tokenize(text.lower())
        tagged = pos_tag(tokens, tagset="universal")
        words = [word for (word, word_type) in tagged if word_type != '.']
        return words

    def build_dictionary(self, input_text=""):
        if not input_text:
            with open("input.txt") as f:
                input_text = f.read()

        all_words = self.tokenize(input_text)
        for word in all_words:
            if word not in self.dictionary:
                self.dictionary[word] = 0
            self.dictionary[word] += 1

        self.tree.add_dictionary(self.dictionary)
        self.tree.precalc_sorted()


    def search_top_k_strings(self, prefix, k=10):
        vertex = self.tree.find_vertex(prefix.lower())
        if vertex is None:
            return []
        best_nodes = vertex.sorted_subnodes
        best_k_nodes = best_nodes[:k]
        best_words = [node.word for node in best_k_nodes]
        return best_words

    def search_top_k_strings_stupid(self, prefix, k=10):
        prefix = prefix.lower()
        good = [i for i in self.dictionary if i.startswith(prefix)]
        good = sorted(good, key=lambda x: (-self.dictionary[x], x))
        return good[:k]



if __name__ == "__main__":
    ac = Autocompletor()
    ac.build_dictionary()
    while True:
        s = input()
        res1 = ac.search_top_k_strings(s)
        res2 = ac.search_top_k_strings_stupid(s)

        print("Fast method:", res1)
        print("Slow method:", res2)
