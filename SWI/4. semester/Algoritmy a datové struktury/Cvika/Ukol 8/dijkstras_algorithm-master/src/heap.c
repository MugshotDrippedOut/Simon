/*!
* \file       heap.c
* \author     Ondřej Ševčík
* \date       6/2019
* \brief      Implementation of the heap module in version min-heap.
* **********************************************************************
* \attention
* &copy; Copyright (c) 2022 FAI UTB. All rights reserved.
*
* Unauthorized copying of this file, via any medium is strictly prohibited
* Proprietary and confidential
*/

/* Includes --------------------------------------------------------------------------------------*/
#include "heap.h"
#include "mymalloc.h"

#include <stdlib.h>
#include <string.h>


/* Private macro ---------------------------------------------------------------------------------*/
#define UNUSED(x) (void)x
#define SWAP(x, y) Data_t temp = x; x = y; y = temp;

/* Private types ---------------------------------------------------------------------------------*/
/* Private variables -----------------------------------------------------------------------------*/
/* Private function declarations -----------------------------------------------------------------*/
/* Exported functions definitions ----------------------------------------------------------------*/
bool Heap_Init(tHeap *heap)
{
 if (heap ==NULL){
   return false;
 }
 heap->count =0;
 heap->maxItems = MAX_ITEMS_START;
 heap->array = myMalloc(MAX_ITEMS_START* sizeof(Data_t));

 if(heap->array ==NULL){
   return false;
 }

 return true;
}

bool Heap_Insert(tHeap *heap, Data_t insertData)
{
 UNUSED(heap);
 UNUSED(insertData);
 if(heap==NULL){
   return false;
 }
 if(heap->maxItems== heap->count){
   Data_t *p = myRealloc(heap->array,(heap->maxItems*2)*sizeof(Data_t ));
   if(p==NULL){
     return false;
   }
   heap->array = p;
   heap->count = Heap_Count(*heap);
   heap->maxItems = heap->maxItems*2;
 }

 heap->array[heap->count] = insertData; // at the end of array insert data

 size_t i = heap->count ;
 while (true) {
   if (i <= 0) {
     break;
   }
   if(Data_Cmp(&heap->array[i], &heap->array[(i-1)/2]) >= 0){
     break;
   }
   SWAP(heap->array[i], heap->array[(i-1)/2]);
   i = (i-1)/2;
 }

 heap->count++;
 return true;
}

void Heap_Destruct(tHeap *heap)
{
 UNUSED(heap);
 myFree(heap->array);
 heap->array=NULL;
 heap->count = 0;
 heap->maxItems = 0;
}

bool Heap_FindMin(tHeap heap, Data_t *value)
{
 if(value==NULL || heap.count == 0){
   return false;
 }

 *value = heap.array[0];
 return true;

}

bool Heap_DeleteMin(tHeap *heap, Data_t *deletedValue)
{
 UNUSED(heap);
 UNUSED(deletedValue);
 if(deletedValue==NULL || heap->count == 0){
   return false;
 }

 *deletedValue = heap->array[0];
 heap->array[0] = heap->array[heap->count-1];
 heap->count--;
 size_t i = 0;
 while(true){
   size_t left = 2*i+1;
   size_t right = 2*i+2;
   size_t smallest = i;
   if(left < heap->count && Data_Cmp(&heap->array[left], &heap->array[smallest]) < 0){
     smallest = left;
   }
   if(right < heap->count && Data_Cmp(&heap->array[right], &heap->array[smallest]) < 0){
     smallest = right;
   }
   if(smallest == i){
     break;
   }
   SWAP(heap->array[i], heap->array[smallest]);
   i = smallest;
 }
 return true;
}

void Heap_Process(tHeap heap, heapProcessCB cb)
{
 if(cb==NULL){
   return;
 }
 for (size_t i = 0; i < heap.count ; ++i) {
   cb(i,&heap.array[i]);

 }
}

bool Heap_Empty(tHeap heap)
{
 UNUSED(heap);
 if(heap.array==NULL||heap.count==0){
   return true;
 }
 return false;
}

unsigned Heap_Count(tHeap heap)
{
 UNUSED(heap);
 size_t count = heap.count;

 return count;
}
/* Private function definitions ------------------------------------------------------------------*/
