        def dfs(node):
            if not node:
                return False
            if k-node.val in numSet:
                return True
            
            numSet.add(node.val)
            return dfs(node.right) or dfs(node.left)
        return dfs(root)