            ans[i + size: i + m] = t[size:]
            pre = i
            
        # Precompute nearest pending positions
        pre_q = [-1] * len(ans)
        pre = -1
        for i, c in enumerate(ans):
            if c == '?':
                ans[i] = 'a'
                pre = i
            pre_q[i] = pre
            
        # Match ans against t using Z-function
        z = self.calc_z(t + ''.join(ans))
        
        # Process 'F'
        i = 0
        while i < n:
            if s[i] != 'F':
                i += 1
                continue
            if z[m + i] < m:
                i += 1
                continue
            # Modify the last pending position
            j = pre_q[i + m - 1]
            if j < i:
                return ""
            ans[j] = 'b'
            i = j + 1  # Optimization: skip past the modified index
        return ''.join(ans)