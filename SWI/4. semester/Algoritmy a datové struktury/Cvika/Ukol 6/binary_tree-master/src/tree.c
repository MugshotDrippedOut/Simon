/*!
 * \file       tree.c
 * \author     Ondřej Ševčík
 * \date       6/2019
 * \brief      Source file for binary tree
 * **********************************************************************
 * \attention
 * &copy; Copyright (c) 2022 FAI UTB. All rights reserved.
 *
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

/* Includes --------------------------------------------------------------------------------------*/
#include "tree.h"
#include "mymalloc.h"

/* Private types ---------------------------------------------------------------------------------*/
/* Private macros --------------------------------------------------------------------------------*/
#define UNUSED(x) (void)x


/* Private variables -----------------------------------------------------------------------------*/
/* Private function declarations -----------------------------------------------------------------*/
/* Exported functions definitions ----------------------------------------------------------------*/

bool Tree_Init(Tree *const tree)
{
  UNUSED(tree);
  if(!tree)return false;

  tree->root=NULL;
  tree->nodeCount=0;
  return true;
}

// Helper function to delete all nodes in a tree
void Delete_node(TreeNode *nodeToDelete) {

  if (nodeToDelete == NULL) return;

  Delete_node(nodeToDelete->left);
  Delete_node(nodeToDelete->right);

  myFree(nodeToDelete);
}

void Tree_Clear(Tree *const tree)
{
  if (tree == NULL) return;

  Delete_node(tree->root);

  tree->root = NULL;
  tree->nodeCount = 0;
}


bool Tree_Insert(Tree *const tree, const Data_t data)
{

  if(!tree)return false;
  if (!tree->root){
    TreeNode *node = myMalloc(sizeof (TreeNode));
    if(!node)return false;
    node->left = node->right = NULL;
    node->data = data;
    tree->root = node;
    tree->nodeCount++;
    return true;
  }

  TreeNode *search = tree->root;
  TreeNode *parent = NULL;
  int res = 0;
  while (search !=NULL){
    parent = search;
    res = Data_Cmp(&data, &search->data);
    if(res<0){
      search = search->left;
    }
    if(res>0){
      search = search->right;
    }
    if(res == 0){
      return false;
    }
  }

  TreeNode *node = myMalloc(sizeof (TreeNode));
  if(node == NULL)return false;
  node->left = node->right = NULL;
  node->data = data;
  if(res<0) {
    parent->left = node;
  } else{
    parent->right=node;
  }
  tree->nodeCount++;
  return true;
}

void Tree_Delete(Tree *const tree, const Data_t data)
{
  if (!tree) return;

  TreeNode *search = tree->root;
  TreeNode *parent = NULL;
  int res;

  while (search != NULL) {
    res = Data_Cmp(&data, &search->data);
    if (res == 0) break;

    parent = search;
    search = (res < 0) ? search->left : search->right;
  }

  if (search == NULL) return;

  if (search->left == NULL || search->right == NULL) {
    TreeNode *temp = (search->left != NULL) ? search->left : search->right;

    if (parent == NULL) {
      tree->root = temp;
    } else if (parent->left == search) {
      parent->left = temp;
    } else {
      parent->right = temp;
    }
    myFree(search);
  } else {
    TreeNode *max = search->left;
    parent = search;
    while (max->right != NULL) {
      parent = max;
      max = max->right;
    }

    search->data = max->data;

    if (parent->left == max) {
      parent->left = max->left;
    } else {
      parent->right = max->left;
    }

    myFree(max);
  }
  tree->nodeCount--;
}
const Data_t *Tree_Get_Data(const TreeNode *const node)
{
  if(!node)return NULL;

  return &node->data;
}

TreeNode *Tree_Find_Node(Tree tree, const Data_t data)
{
  TreeNode *search = tree.root;
  int res;
  while (search !=NULL){
    res = Data_Cmp(&data, &search->data);
    if(res<0){
      search = search->left;
    }
    if(res>0){
      search = search->right;
    }
    if(res == 0){
      return search;
    }
  }

  return NULL;
}

size_t Tree_Get_Count(Tree tree)
{
  return tree.nodeCount;
}

void inOrder(TreeNode *node, TreeNodeProc proc){
  if(!node){
    return;
  }
  inOrder(node->left,proc);
  proc(node);
  inOrder(node->right, proc);
}
void preOrder(TreeNode *node, TreeNodeProc proc){
  if(!node){
    return;
  }
  proc(node);
  preOrder(node->left,proc);
  preOrder(node->right, proc);
}
void postOrder(TreeNode *node, TreeNodeProc proc){
  if(!node){
    return;
  }
  postOrder(node->left,proc);
  postOrder(node->right, proc);
  proc(node);
}
void Tree_Process(Tree tree, TreeNodeProc proc, TreeProcessMode mode)
{
  if(!proc || !tree.root)return;

  switch (mode) {
    case IN_ORDER:
      inOrder(tree.root, proc);
      break;
    case PRE_ORDER:
      preOrder(tree.root, proc);
      break;
    case POST_ORDER:
      postOrder(tree.root, proc);
      break;
  }
}

/* Private function definitions ------------------------------------------------------------------*/
