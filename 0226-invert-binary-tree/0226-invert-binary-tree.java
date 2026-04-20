/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        Stack<TreeNode> nodes = new Stack<>();
        if (root != null) {
            nodes.push(root);
        } else {
            return root;
        }
        while(nodes.size()>0) {
            TreeNode cur = nodes.pop();
            TreeNode temp = null;
            if (cur.left != null) {
                nodes.push(cur.left);
            }
            if (cur.right != null) {
                nodes.push(cur.right);
            }
            
            temp = cur.left;
            cur.left = cur.right;
            cur.right = temp;
        }
        return root;
    }
}