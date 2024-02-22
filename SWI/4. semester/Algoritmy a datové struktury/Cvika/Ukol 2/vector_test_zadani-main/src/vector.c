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
  UNUSED(original);
  return NULL;
}

void Vector_Clear(Vector_t *const vector)
{
  UNUSED(vector);
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
  UNUSED(vector);
  UNUSED(position);
  UNUSED(value);
  return false;
}

bool Vector_Remove(Vector_t *const vector, size_t position)
{
  UNUSED(vector);
  UNUSED(position);
  return false;
}

size_t Vector_Append(Vector_t *vector, Vector_DataType_t value)
{
  if(vector==NULL){
    return SIZE_MAX;
  }

  if(Vector_Length(vector)==vector->size){
    Vector_DataType_t *p = myRealloc(vector->items,(vector->size + vector->alloc_step)*sizeof(Vector_DataType_t));
    if(p==NULL){
      return SIZE_MAX;
    }
    vector->items=p;
    vector->next = vector->items + vector->size;
    vector->size += vector->alloc_step;
  }


  *vector->next = value;
  vector->next++;

  return Vector_Length(vector)-1;

}

void Vector_Set(Vector_t *const vector, size_t position, Vector_DataType_t value)
{
  UNUSED(vector);
  UNUSED(position);
  UNUSED(value);
}

bool Vector_Contains(const Vector_t *const vector, Vector_DataType_t value)
{
  UNUSED(vector);
  UNUSED(value);
  return false;
}

size_t Vector_IndexOf(const Vector_t *const vector, Vector_DataType_t value, size_t from)
{
  UNUSED(vector);
  UNUSED(value);
  UNUSED(from);
  return SIZE_MAX;
}

void Vector_Fill(const Vector_t *const vector,
                 Vector_DataType_t value,
                 size_t start_position,
                 size_t end_position)
{
  UNUSED(vector);
  UNUSED(value);
  UNUSED(start_position);
  UNUSED(end_position);
}

void Vector_Destroy(Vector_t **const vector)
{
  UNUSED(vector);
}

/* Private function definitions ------------------------------------------------------------------*/