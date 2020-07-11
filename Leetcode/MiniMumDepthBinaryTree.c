/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int minimum(int a,int b){
    int val=(a<b)?a:b;  
    return val;
}
int minDepth(struct TreeNode* root){

    if(root==NULL){
        return(0);
    }
    else if(root->left!=NULL && root->right==NULL){
        return(1+minDepth(root->left));
    }
    else if(root->right!=NULL && root->left==NULL){
        return(1+minDepth(root->right));
    }
    else{
        return(1+minimum(minDepth(root->left),minDepth(root->right)));
    }
    
}


