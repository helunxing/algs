from bisect import bisect_left
from collections import deque


class Entry:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.inTop = False

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


class TopK:
    """
    @param: k: An integer
    """

    def __init__(self, k):
        # do intialization if necessary
        self.k = k
        self.top_k = deque()
        self.map = {}

    """
    @param: word: A string
    @return: nothing
    """

    def add(self, word):
        # write your code here
        if self.k == 0:
            return

        entry = None
        if word in self.map:
            entry = self.map[word]
            if entry.inTop:
                self.removeFromTop(entry)
            entry.freq += 1
        else:
            pass

    """
    @return: the current top k frequent words.
    """

    def topk(self):
        # write your code here
        pass


class Entry2:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.inTop = False

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


class TopK2:
    """
    @param: k: An integer
    """

    def __init__(self, k):
        self.k = k
        self.top_k = []
        self.mapping = {}

    """
    @param: word: A string
    @return: nothing
    """

    def add(self, word):
        if self.k == 0:
            return

        entry = None
        if word in self.mapping:
            entry = self.mapping[word]
            if entry.inTop:
                self.removeFromTop(entry)
            entry.freq += 1
        else:
            self.mapping[word] = Entry(word, 1)
            entry = self.mapping[word]

        self.addToTop(entry)

        if len(self.top_k) > self.k:
            self.top_k[0].inTop = False
            self.top_k.pop(0)

    """
    @return: the current top k frequent words.
    """

    def topk(self):
        if self.k == 0 or len(self.top_k) == 0:
            return []

        results = [e.word for e in self.top_k]
        results.reverse()
        return results

    def addToTop(self, entry):
        idx = bisect_left(self.top_k, entry)
        self.top_k.insert(idx, entry)
        entry.inTop = True

    def removeFromTop(self, entry):
        idx = bisect_left(self.top_k, entry)
        self.top_k.pop(idx)
        entry.inTop = False


# class Node {
#     String word
#     int times
#     public Node(String word, int times) {
#         this.word = word
#         this.times = times
#     }
# }

# public class TopK {
#     Queue<Node> queue = null;
#     Map<String, Node> map = new HashMap<>();
#     int k = 0;
#     /*
#     * @param k: An integer
#     */public TopK(int k) {
#         // do intialization if necessary
#         Comparator<Node> comparator = new Comparator<Node>() {
#             public int compare(Node left, Node right) {
#                 if (left.times == right.times) {
#                     return left.word.compareTo(right.word);
#                 }

#                 return right.times - left.times;
#             }
#         };

#         queue = new PriorityQueue<Node>(k == 0 ? 1 : k, comparator);
#         this.k = k;
#     }

#     /*
#      * @param word: A string
#      * @return: nothing
#      */
#     public void add(String word) {
#         // write your code here
#         if (!map.containsKey(word)) {
#             Node node = new Node(word, 1);
#             map.put(word, node);
#             queue.offer(node);
#         } else {
#             Node node = map.get(word);
#             node.times++;

#             queue.remove(node);
#             queue.offer(node);
#         }
#     }

#     /*
#      * @return: the current top k frequent words.
#      */
#     public List<String> topk() {
#         // write your code here
#         List<String> result = new ArrayList<>();
#         Stack<Node> stack = new Stack<>();

#         for (int i = 0; i < k && !queue.isEmpty(); i++) {
#             Node node = queue.poll();
#             stack.add(node);
#             result.add(node.word);
#         }

#         while (!stack.isEmpty()) {
#             queue.offer(stack.pop());
#         }

#         return result;
#     }
# }
