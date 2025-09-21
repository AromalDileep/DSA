# from sortedcollections import SortedList

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(SortedList)   # movie -> SortedList[(price, shop)]
        self.sm_p = {}                          # (shop, movie) -> price
        self.rented = SortedList()              # SortedList[(price, shop, movie)]

        for s, m, p in entries:
            self.movies[m].add((p, s))
            self.sm_p[(s, m)] = p

    def search(self, movie: int) -> List[int]:
        res = []
        n = len(self.movies[movie])
        for i in range(min(5, n)):
            res.append(self.movies[movie][i][1])
        return res

    def rent(self, shop: int, movie: int) -> None:
        p = self.sm_p[(shop, movie)]
        self.movies[movie].discard((p, shop))
        self.rented.add((p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.sm_p[(shop, movie)]
        self.movies[movie].add((p, shop))
        self.rented.discard((p, shop, movie))

    def report(self) -> List[List[int]]:
        res = []
        n = len(self.rented)
        for i in range(min(5, n)):
            _, s, m = self.rented[i]
            res.append([s, m])
        return res
