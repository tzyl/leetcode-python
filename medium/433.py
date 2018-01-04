from collections import deque, defaultdict
from itertools import combinations


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if start not in bank:
            bank.append(start)
        edges = self.generate_edges(bank)
        distances = defaultdict(lambda: -1)
        distances[start] = 0
        discovered = set(start)
        Q = deque([start])
        while Q:
            current_gene = Q.popleft()
            for gene in edges[current_gene]:
                if gene not in discovered:
                    discovered.add(gene)
                    distances[gene] = distances[current_gene] + 1
                    Q.append(gene)
        return distances[end]

    def generate_edges(self, bank):
        edges = defaultdict(list)
        for gene1, gene2 in combinations(bank, 2):
            if sum(c1 != c2 for c1, c2 in zip(gene1, gene2)) == 1:
                edges[gene1].append(gene2)
                edges[gene2].append(gene1)
        return edges
