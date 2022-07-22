# Python program for insert and search
# operation in a Trie

class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch)-ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl.isEndOfWord

    def isEmpty(self):
        for i in range(26):
            if self.root.children[i] != None:
                return False
        return True

    def remove(self, key, depth):
        if self.root == None:
            return

        # If last character of key is being processed
        if depth == len(key):
            # This node is no more end of word after
            # removal of given key
            if self.root.isEndOfWord:
                self.root.isEndOfWord = False

            # If given is not prefix of any other word
            if self.isEmpty():
                self.root = None

            return self.root

        # If not last character, recur for the child
        # obtained using ASCII value
        index = ord(key[depth][0]) - ord('a')
        self.root.children[index] = self.remove(key, depth + 1)

        # If root does not have any child (its only child got
        # deleted), and it is not end of another word.
        if self.isEmpty() and self.root.isEndOfWord == False:
            self.root = None

        return self.root

# driver function


def main():

    # Trie object
    t = Trie()

    while True:
        command = input().split()
        match command[0]:
            case "add":
                if len(command) != 2:
                    print("Wrong command")
                else:
                    t.insert(command[1])
            case "delete":
                if len(command) != 2:
                    print("Wrong command")
                else:
                    t.remove(command[1],0)
            case "find":
                if len(command) != 2:
                    print("Wrong command")
                else:
                    print(t.search(command[1]))
            case "exit":
                break
            case _:
                print("Wrong command")


if __name__ == '__main__':
    main()
