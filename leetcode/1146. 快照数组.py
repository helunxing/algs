import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.d = {0: {}}
        self.sid = 0

    def set(self, index: int, val: int) -> None:
        self.d[self.sid][index] = val

    def snap(self) -> int:
        self.sid += 1
        self.d[self.sid] = self.d[self.sid-1].copy()
        return self.sid-1

    def get(self, index: int, snap_id: int) -> int:
        return self.d[snap_id][index] if index in self.d[snap_id] else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


# 实现支持下列接口的「快照数组」- SnapshotArray：

# SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
# void set(index, val) - 会将指定索引 index 处的元素设置为 val。
# int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
# int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
