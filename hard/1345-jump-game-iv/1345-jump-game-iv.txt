                idx = q.popleft()
                if idx == n - 1:
                    return steps
                if idx - 1 >= 0 and not visited[idx - 1]:
                    visited[idx - 1] = True
                    q.append(idx - 1)
                if idx + 1 < n and not visited[idx + 1]:
                    visited[idx + 1] = True
                    q.append(idx + 1)
                if arr[idx] in graph:
                    for nxt in graph[arr[idx]]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)
            for _ in range(len(q)):
                    del graph[arr[idx]]
            steps += 1
        return -1       
        while q:
        steps = 0