class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        v=set()
        def dfs(room):
            v.add(room)
            for key in rooms[room]:
                if key not in v:
                    dfs(key)
        dfs(0)
        return len(v)==len(rooms)
        