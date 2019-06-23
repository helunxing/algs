class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        res = []

        # 最小
        i = 0
        while i < 256:
            if count[i] != 0:
                res.append(float(i))
                break
            i += 1

        # 最大
        i = 255
        while 0 <= i:
            if count[i] != 0:
                res.append(float(i))
                break
            i -= 1

        # 平均
        s, cnt = 0, 0
        # 众数
        major = 0
        for i, x in enumerate(count):
            s += i*x
            cnt += x
            if x > count[major]:
                major = i
        res.append(float(s/cnt))

        # 中位数
        tmp = 0
        goal = (cnt+1)//2
        i = 0
        if cnt & 1:
            while i < 256:
                if tmp < goal <= tmp+count[i]:
                    res.append(float(i))
                    break
                tmp += count[i]
                i += 1
        else:
            while i < 256:
                if tmp < goal < tmp+count[i]:
                    res.append(float(i))
                    break
                if tmp+count[i] == goal:
                    j = i+1
                    while j < 256:
                        if count[j]:
                            res.append(float(i+j)/2)
                            break
                        j += 1
                tmp += count[i]
                i += 1

        res.append(float(major))
        return res
