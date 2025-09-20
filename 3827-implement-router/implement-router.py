from sortedcontainers import SortedList

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # Stores (source, destination, timestamp)
        self.packet_set = set()
        self.destination_map = defaultdict(SortedList)  # destination -> SortedList of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False

        self.queue.append(packet)
        self.packet_set.add(packet)
        self.destination_map[destination].add(timestamp)

        while len(self.queue) > self.memoryLimit:
            old_packet = self.queue.popleft()
            self.packet_set.remove(old_packet)
            _, old_dest, old_time = old_packet
            self.destination_map[old_dest].remove(old_time)
            if not self.destination_map[old_dest]:
                del self.destination_map[old_dest]

        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []

        packet = self.queue.popleft()
        self.packet_set.remove(packet)
        _, dest, time = packet
        self.destination_map[dest].remove(time)
        if not self.destination_map[dest]:
            del self.destination_map[dest]

        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destination_map:
            return 0
        times = self.destination_map[destination]
        left = times.bisect_left(startTime)
        right = times.bisect_right(endTime)
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)