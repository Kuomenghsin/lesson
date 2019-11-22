
import copy
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def __init__(self):
        self.root=None
        
       
    def insert(self, root, val):
        new_node=TreeNode(val)
        if root.val==None:      #如果root.val為空值，則存入val
            root.val=val      

        else:
            if val <= root.val:          # val <= root.val時，再檢查root.left是否為空值，如果不是空值，則更換root再進行下一次insert
                if root.left == None:
                    root.left = new_node
                else:
                    self.insert(root.left,val)

            elif val > root.val:         # val > root.val時，再檢查root.right是否為空值，如果不是空值，則更換root再進行下一次insert
                if root.right == None:
                    root.right = new_node
                else:
                    self.insert(root.right,val)  

    
    def search(self, root, target):
        if root.val == None:        # 確認root使否為目標值
            return False
        
        elif root.val == target:            
            return root
        
        elif root.val>target:      # 如果root.val>目標值，root.left又不是空值則繼續向下尋找
            if root.left != None:
                return self.search(root.left, target)
            else:
                return False
       
        elif root.val<target:      # 如果root.val<目標值，root.right又不是空值則繼續向下尋找
            if root.right != None:
                return self.search(root.right, target)
            else:
                return False
    
    
    def min(self,node): 
        cur = node 
        while cur.left != None: 
            cur = cur.left  
        return cur 
                   
    def PreorderTraversal(self,root):
        node_list = []
        if root != None:
            node_list.append(root.val)
            node_list = node_list + Solution().PreorderTraversal(root.left)
            node_list = node_list + Solution().PreorderTraversal(root.right)
        return node_list        

    def find(self,root,target):
        list = []
        if root !=None:
            list.append(root.val)
            list = list + Solution().PreorderTraversal(root.left)
            list = list + Solution().PreorderTraversal(root.right)       

        if target in list:
            Solution().delete(root,target)
        else:
            return root
        
    def find_2(self,root,target,new_val):
        list = []
        if root !=None:
            list.append(root.val)
            list = list + Solution().PreorderTraversal(root.left)
            list = list + Solution().PreorderTraversal(root.right)       

        if target in list:
            Solution().modify(root,target,new_val)
            return root
        else:
            return root
        
               
        
        

    def delete(self, root, target):
        if root==None:      # 如果root為空值則回傳
            return root 
        else:
            if target<root.val:                          # target < root.val 則更換root為root.left再進行一次function
                root.left=self.delete(root.left,target)
                
            elif target>root.val:                        # target > root.val 則更換root為root.right再進行一次function
                root.right=self.delete(root.right,target)
                
            else:
                if root.left==None and root.right==None:  # 如果沒有小孩則將root刪除並回傳
                    #print('沒有小孩')
                    root=None
                    #return Solution().delete(root,target)          

                elif root.left == None :     # 只有一個child，沒有root.left，將root改為root.right
                    root = root.right
                    return Solution().delete(root,target) 

                elif root.right == None :    # 只有一個child，沒有root.right，將root改為root.left                
                    root = root.left
                    return Solution().delete(root,target) 

                else:                        # 有兩個child，要尋找右側樹的最小值
                    change_node = self.min(root.right)  # 找到右側樹中的最小值
                    root.val = change_node.val          # 將找到的值取代root.val　
                    root.right = self.delete(root.right, change_node.val)  # 再刪除剛剛找到的最小值
                    return Solution().delete(root,target)        
        return root
 
    def delete_2(self, root, target):       # 刪除一個
        if root==None:      # 如果root為空值則回傳
            return root 
        else:
            if target<root.val:                          # target < root.val 則更換root為root.left再進行一次function
                root.left=self.delete_2(root.left,target)
                
            elif target>root.val:                        # target > root.val 則更換root為root.right再進行一次function
                root.right=self.delete_2(root.right,target)
                
            else:
                if root.left==None and root.right==None:  # 如果沒有小孩則將root刪除並回傳
                    #print('沒有小孩')
                    root=None
                    #return root          

                elif root.left == None :     # 只有一個child，沒有root.left，將root改為root.right
                    root = root.right
                    return root

                elif root.right == None :    # 只有一個child，沒有root.right，將root改為root.left                
                    root = root.left
                    return root

                else:                        # 有兩個child，要尋找右側樹的最小值
                    change_node = self.min(root.right)  # 找到右側樹中的最小值
                    root.val = change_node.val          # 將找到的值取代root.val　
                    root.right = self.delete_2(root.right, change_node.val)  # 再刪除剛剛找到的最小值

        return root
        

            
    def modify(self, root, target, new_val):
        if root != None:            
            self.delete_2(root,target)
            self.insert(root,new_val)
            return Solution().find_2(root,target,new_val) 
        return root
                                              
        
     
       
                                              
 


 
    
    

root=TreeNode(5)  
Node1=TreeNode(3) 
Node2=TreeNode(8)
Node3=TreeNode(3)
Node4=TreeNode(7)
Node5=TreeNode(10)
Node6=TreeNode(-5)
Node7=TreeNode(6)

root.left=Node1
root.right=Node2
root.left.left=Node3
root.left.left.left=Node6
root.right.left=Node4
root.right.left.left=Node7
root.right.right=Node5


root1=copy.deepcopy(root)
root2=copy.deepcopy(root)
root3=copy.deepcopy(root)
root4=copy.deepcopy(root)

print(Solution().PreorderTraversal(root))

print('insert')
print(Solution().insert(root1,4)==root.left.right)
print('------------------')

print('delete')
root2=Solution().delete(root2,3)
print(root2.val==5 and root2.left.val==-5 and root2.left.left==None and root2.left.right==None)
print(root2.right.right.val==10 and root2.right.left.val==7 and root2.right.left.left.val==6)
print(root2.right.right.right==None and root2.right.right.left==None and root2.right.left.right==None and root2.left.right==None)
print(root2.right.left.left.left==None and root2.right.left.left.right==None and root2.right.val==8)
print(Solution().PreorderTraversal(root2))
print('------------------')

print('search')
print(Solution().search(root3,10)==root3.right.right)
print('------------------')

print('modify')
root4=Solution().modify(root4,7,4)
#print(isBinarySearchTree(root4))
print(Solution().PreorderTraversal(root4))
