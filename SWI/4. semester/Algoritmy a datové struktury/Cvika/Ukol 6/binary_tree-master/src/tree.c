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
  if(!tree){
    return false;
  }
  tree->root=NULL;
  tree->nodeCount=0;
  return true;
}

void Tree_Clear(Tree *const tree)
{
  UNUSED(tree);
}

bool Tree_Insert(Tree *const tree, const Data_t data)
{
  UNUSED(tree);
  UNUSED(data);
  if(!tree){
    return false;
  }
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
  UNUSED(tree);
  UNUSED(data);
}

const Data_t *Tree_Get_Data(const TreeNode *const node)
{
  UNUSED(node);
  return NULL;
}

TreeNode *Tree_Find_Node(Tree tree, const Data_t data)
{
  UNUSED(tree);
  UNUSED(data);
  return NULL;
}

size_t Tree_Get_Count(Tree tree)
{
  UNUSED(tree);
  return 0;
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
  UNUSED(tree);
  UNUSED(proc);
  UNUSED(mode);

  if(!proc || !tree.root){
    return;
  }

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
