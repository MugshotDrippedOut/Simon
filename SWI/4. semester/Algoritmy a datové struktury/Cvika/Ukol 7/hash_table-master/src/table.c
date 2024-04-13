/*!
 * \file       table.c
 * \author     Ondřej Ševčík
 * \date       6/2019
 * \brief      Implementation  of functions for HashTable.
 * **************************************************************
 * \attention
 * &copy; Copyright (c) 2022 FAI UTB. All rights reserved.
 *
 * Unauthorized  copying  of  this file, via any medium is strictly prohibited
 * Proprietary  and  confidential
 */
/*! \addtogroup  hashTable
 *  \{
 */
/* Includes --------------------------------------------------------------------------------------*/
#include "table.h"

#include "hash_private.h"
#include "mymalloc.h"

#include <stdio.h>
#include <string.h>

/* Private types ---------------------------------------------------------------------------------*/
/* Private macros --------------------------------------------------------------------------------*/
#define UNUSED(x) (void)x

/* Private variables -----------------------------------------------------------------------------*/
/* Private function declarations -----------------------------------------------------------------*/
/* Exported functions definitions ----------------------------------------------------------------*/
bool HashTable_Init(HashTable *table, size_t size, bool deletecontents)
{
  UNUSED(table);
  UNUSED(size);
  UNUSED(deletecontents);

  if(!table)
    return false;

  table->count = 0;
  table->size = size;
  table->take_ownership = deletecontents;
  table->buckets = myMalloc(sizeof(HashTableNode*) * size);

  if(!table->buckets)
    return false;

  for(size_t i = 0; i < size; i++)
  {
    table->buckets[i] = NULL;
  }

  return true;
}

void HashTable_Destruct(HashTable *table)
{
  UNUSED(table);

  if(!table)
    return;

  for(size_t i = 0; i < table->size; i++)
  {
    HashTableNode *myNode = table->buckets[i];
    while(myNode)
    {
      HashTableNode *next = myNode->next;
      if(table->take_ownership)
      {
        Data_Destruct(myNode->key);
        Data_Destruct(myNode->value);
      }
      myFree(myNode);
      myNode = next;
    }
  }
  myFree(table->buckets);
  table->buckets = NULL;
  table->size = 0;
  table->count = 0;
}

bool HashTable_Insert(HashTable *table, Data_t *key, Data_t *value)
{
  UNUSED(table);
  UNUSED(key);
  UNUSED(value);

  if(!table || !key || !value)
    return false;

  size_t i = hash(table,key);
  HashTableNode *node = table->buckets[i];
  while (node){
    if (Data_Cmp(node->key, key) == 0){
      return false;
    }
    node = node->next;
  }

  HashTableNode *newNode = myMalloc(sizeof(HashTableNode));
  if(!newNode)
    return false;

  newNode->key = key;
  newNode->value = value;
  newNode->next = table->buckets[i];
  table->buckets[i] = newNode;
  table->count++;

  return true;
}

bool HashTable_Replace(HashTable *table, Data_t *key, Data_t *value)
{
  UNUSED(table);
  UNUSED(key);
  UNUSED(value);

  if(!table || !key || !value)
    return false;

  size_t i = hash(table,key);
  HashTableNode *node = table->buckets[i];
  while (node){
    if(Data_Cmp(key, node->key) == 0){
      if(table->take_ownership){
        Data_Destruct(node->value);
        node->value = value;
      }
      else{
        node->value = value;
      }
      return true;
    }
    node = node->next;
  }
  return false;
}

bool HashTable_Delete(HashTable *table, Data_t *key)
{
  if(!table || !key)
    return false;
  size_t i = hash(table,key);
  HashTableNode *node = table->buckets[i];
  HashTableNode *previous = NULL;
  while (node){
    if (Data_Cmp(node->key, key) == 0){
      if (previous){
        previous->next = node->next;
      } else {
        table->buckets[i] = node->next;
      }
      if (table->take_ownership){
        Data_Destruct(node->key);
        Data_Destruct(node->value);
      }
      myFree(node);
      table->count--;
      return true;
    }
    previous = node;
    node = node->next;
  }
  return false;
}

Data_t *HashTable_Find(HashTable *table, Data_t *key)
{
  UNUSED(table);
  UNUSED(key);

  if(!table || !key)
    return NULL;

  size_t i = hash(table,key);
  HashTableNode *node = table->buckets[i];
  while (node){
    if (Data_Cmp(node->key, key) == 0){
      return node->value;
    }
    node = node->next;
  }


  return NULL;

}

size_t HashTable_Get_Count(HashTable table)
{
  UNUSED(table);
  /*! Gets the count of the items in the table.
 *
 * \param[in] table Pointer at the table.
 *
 * \return Returns number of items in table.
   */
  if(!table.buckets)
    return 0;
  return table.count;
}


void HashTable_Clear(HashTable *table)
{

  UNUSED(table);

  if(!table)
    return;

for(size_t i = 0; i < table->size; i++)
  {
    HashTableNode *node = table->buckets[i];
    while(node)
    {
      HashTableNode *next = node->next;
      if(table->take_ownership)
      {
        Data_Destruct(node->key);
        Data_Destruct(node->value);
      }
      myFree(node);
      node = next;
    }
  }
  table->count = 0;
  for(size_t i = 0; i < table->size; i++)
  {
    table->buckets[i] = NULL;
  }
}

void HashTable_Process(HashTable *table, TableNodeProc proc)
{
  UNUSED(table);
  UNUSED(proc);

  if(!table || !proc)
    return;

  for(size_t i = 0; i < table->size; i++)
  {
    HashTableNode *node = table->buckets[i];
    while(node)
    {
      proc(node->key, node->value);
      node = node->next;
    }
  }
}

/* Private function definitions ------------------------------------------------------------------*/

/*! \} */
