                return
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
            
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                cur.append(candidates[j])
                dfs(j + 1, total + candidates[j], cur)
                cur.pop()
        dfs(0, 0, [])
        return res