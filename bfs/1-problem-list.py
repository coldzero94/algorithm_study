# https://leetcode.com/problems/range-sum-of-bst/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        total = 0
        
        # 현재 노드의 값이 범위 안에 있는 경우
        if low <= root.val <= high:
            total += root.val
        
        # BST 특성을 활용한 최적화된 탐색
        if root.val > low:
            total += self.rangeSumBST(root=root.left, low=low, high=high)
        if root.val < high:
            total += self.rangeSumBST(root=root.right, low=low, high=high)
        
        return total
    

def create_tree_from_list(values: List[int]) -> Optional[TreeNode]:
    if not values:
        return None
    
    # None 값은 건너뛰고 실제 노드만 생성
    nodes = []
    for val in values:
        if val is None or val == "null":
            nodes.append(None)
        else:
            nodes.append(TreeNode(val))
    
    # 트리 연결
    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            
            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]
    
    return nodes[0] if nodes else None


if __name__ == "__main__":
    # 입력값
    values = [10,5,15,3,7,None,18]  # 이런 형식으로 입력이 주어짐
    low = 7
    high = 15
    
    # 트리 생성
    root = create_tree_from_list(values)
    
    # Solution 실행
    solution = Solution()
    result = solution.rangeSumBST(root, low, high)
    print(f"Result: {result}")