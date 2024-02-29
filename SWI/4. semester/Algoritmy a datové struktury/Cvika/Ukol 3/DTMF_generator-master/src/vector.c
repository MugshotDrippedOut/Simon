/*!
 * \file       vector.c
 * \author     Horak, Jurena
 * \date       2019.6
 * \brief      Implementation of function.h header file
 * ******************************************
 * \attention
 * &copy; Copyright (c) 2022 FAI UTB. All rights reserved.
 *
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */
/* Includes --------------------------------------------------------------------------------------*/
#include "vector.h"

#include "mymalloc.h"

/* Private types ---------------------------------------------------------------------------------*/
/* Private macros --------------------------------------------------------------------------------*/
#define UNUSED(x) (void)x

/* Private variables -----------------------------------------------------------------------------*/
/* Private function declarations -----------------------------------------------------------------*/
/* Exported functions definitions ----------------------------------------------------------------*/
Vector_t *Vector_Create(size_t initial_size, size_t alloc_step)
{
  Vector_t *vector = myMalloc(sizeof(Vector_t));
  if (vector == NULL){
    return  NULL;
  }

  vector->size = initial_size;
  vector->alloc_step = alloc_step;
  vector->items = myMalloc(initial_size*sizeof(Vector_DataType_t ));

  if(vector-> items == NULL){

    myFree(vector);
    return NULL;
  }
  vector->next = vector->items;
  return vector;
}

Vector_t *Vector_Copy(const Vector_t *const original)
{
  Vector_t *copy = myMalloc(sizeof(&original));
  if (copy == NULL){
    return  NULL;
  }

  copy->size = original->size;
  copy->alloc_step = original->alloc_step;
  if(original->items==NULL){
    return NULL;
  }
  copy->items = myMalloc(original->size*sizeof(Vector_DataType_t ));
  copy->next = copy->items;
  return copy;


}

void Vector_Clear(Vector_t *const vector)
{
  if(vector==NULL){
    return;
  }
  myFree(vector->items);
  vector->size = 0;
  vector->items = NULL;
  vector->next = NULL;
}

size_t Vector_Length(const Vector_t *const vector)
{
  if(vector == NULL){
    return SIZE_MAX;
  }


  return vector->next-vector->items;
}

bool Vector_At(const Vector_t *const vector, size_t position, Vector_DataType_t *const value)
{
  if(vector==NULL){
    return false;
  }
  if(position>=Vector_Length(vector)){
    return false;
  }
  *value = *(vector->items+position);
  return true;
}

bool Vector_Remove(Vector_t *const vector, size_t position)
{
  if(vector==NULL || position>=Vector_Length(vector)){
    return false;
  }
  for(size_t i = position; i<Vector_Length(vector)-1; i++){
    *(vector->items+i) = *(vector->items+i+1);
  }
  vector->next--;
  return true;
}

void Vector_Append(Vector_t *vector, Vector_DataType_t value)
{

  if(Vector_Length(vector)==vector->size){
    Vector_DataType_t *p = myRealloc(vector->items,(vector->size + vector->alloc_step)*sizeof(Vector_DataType_t));

    vector->items=p;
    vector->next = vector->items + vector->size;
    vector->size += vector->alloc_step;
  }

  *vector->next = value;
  vector->next++;


}

void Vector_Set(Vector_t *const vector, size_t position, Vector_DataType_t value)
{

  if(vector==NULL || position>= Vector_Length(vector)){
    return;
  }
  *(vector->items+position) = value;

}

bool Vector_Contains(const Vector_t *const vector, Vector_DataType_t value)
{
  if(vector==NULL){
    return false;
  }
  for(size_t i = 0; i < Vector_Length(vector)-1; ++i) {
    if(*(vector->items+i)==value){
      return true;
    }
  }
  return false;
}

size_t Vector_IndexOf(const Vector_t *const vector, Vector_DataType_t value, size_t from)
{
  if(vector==NULL){
    return SIZE_MAX;
  }
  for (size_t i = from; i < Vector_Length(vector)-1; ++i) {
    if(*(vector->items+i)==value) {
      return i;
    }
  }
  return SIZE_MAX;
}

void Vector_Fill(const Vector_t *const vector,
                 Vector_DataType_t value,
                 size_t start_position,
                 size_t end_position)
{
  if(vector==NULL){
    return;
  }
  if(start_position>end_position){
    return;
  }
  if(start_position>= Vector_Length(vector)){
    return;
  }
  if(end_position>= Vector_Length(vector)){
    end_position= Vector_Length(vector);
  }
  for (size_t i = start_position; i < end_position+1; ++i) {

    *(vector->items+i) = value;
  }
}

void Vector_Destroy(Vector_t **const vector)
{
  UNUSED(vector);
  if(*vector==NULL){
    return;
  }
  myFree((*vector)->items);
  myFree(*vector);
  *vector = NULL;
}

/* Private function definitions ------------------------------------------------------------------*/