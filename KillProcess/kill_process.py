import Queue
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        if not kill:
            return pid
        ht = {}
        kills = Queue.Queue()
        kills.put(kill)
        ans = []
        for index, pp in enumerate(ppid):
            if pp in ht:
                ht[pp].append(pid[index])
            else:
                ht[pp] = [pid[index]]
        if kill not in ht:
            return [kill]
        while not kills.empty():
            kill = kills.get()
            ans.append(kill)
            if kill in ht:
                children = ht[kill]
                for c in children:
                    kills.put(c)
        return ans