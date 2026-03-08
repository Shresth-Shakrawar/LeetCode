                    break
            
            if cur.val > newNode.val:
                if cur.left is not None:
                    cur = cur.left
                    continue
                else:
                    cur.left = newNode
                    break
            #print(f"{cur.val=} {cur.left=} {cur.right}")
        return root