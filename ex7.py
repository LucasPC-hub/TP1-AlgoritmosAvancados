class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_end_of_word = True

    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True


if __name__ == "__main__":
    trie = Trie()

    palavras = ["casa", "casamento", "casaco", "bola", "bolada", "bolacha"]
    for palavra in palavras:
        trie.insert(palavra)

    print(f"'casa' está na Trie? {trie.search('casa')}")  # True
    print(f"'casamento' está na Trie? {trie.search('casamento')}")  # True
    print(f"'cas' está na Trie? {trie.search('cas')}")  # False
    print(f"'bolo' está na Trie? {trie.search('bolo')}")  # False

    print(f"Existe palavra com prefixo 'cas'? {trie.starts_with('cas')}")  # True
    print(f"Existe palavra com prefixo 'bol'? {trie.starts_with('bol')}")  # True
    print(f"Existe palavra com prefixo 'bal'? {trie.starts_with('bal')}")  # False