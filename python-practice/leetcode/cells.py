class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        new_cells = [0] * len(cells)
        if n % 14 != 0:
            n = n % 14
        else:
            n = 14
            
        while n > 0:
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    new_cells[i] = 1
                else:
                    new_cells[i] = 0
            cells = new_cells.copy()
            n -= 1
            
        return new_cells

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        seen = dict()
        is_fast_forwarded = False

        while N > 0:
            if not in is_fast_forwarded:
                state_key = tuple(cells)
                if state_key in seen:
                    N %= seen[state_key] - N
                    is_fast_forwarded = True
                    else:
                        seen[state_key] = n
            if N > 0:
                N -= 1
                next_day_cells = slef.nextDat(cells)
                cells = next_day_cells
        return cells

