class SnapshotArray:

    def __init__(self, length: int):
        self.lst = [[[0, 0]] for i in range(length)]
        self.snapshots = 0
        

    def set(self, index: int, val: int) -> None:
        if self.lst[index][-1][1] == self.snapshots:
            self.lst[index][-1][0] = val
        else:
            self.lst[index].append([val, self.snapshots])

    def snap(self) -> int:
        self.snapshots += 1
        return self.snapshots - 1        

    def get(self, index: int, snap_id: int) -> int:
        indexLst = self.lst[index]
        
        start = 0
        end = len(indexLst) - 1
        while (start < end) :
            mid = end - (end - start) // 2
            
            if indexLst[mid][1] > snap_id:
                end = mid - 1
            else:
                start = mid
        
        return indexLst[start][0]
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)