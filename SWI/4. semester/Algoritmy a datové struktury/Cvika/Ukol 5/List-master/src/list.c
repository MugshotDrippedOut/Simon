/*!
 * \file       list.c
 * \author     Ondřej Ševčík
 * \date       6/2019
 * \brief      Implementing functions of ATD list defined in a header file
 * list.h
 * ****************************************************************************
 * \attention
 * &copy; Copyright (c) 2022 FAI UTB. All rights reserved.
 *
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

/* Includes --------------------------------------------------------------------------------------*/
#include "list.h"

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Private types ---------------------------------------------------------------------------------*/
/* Private macros --------------------------------------------------------------------------------*/
#define UNUSED(x) (void)x

/* Private variables -----------------------------------------------------------------------------*/
/* Private function declarations -----------------------------------------------------------------*/
/* Exported functions definitions ----------------------------------------------------------------*/

void List_Init(List_t *const list)
{
  UNUSED(list);
}

void List_Insert_First(List_t *const list, Data_t data)
{
  UNUSED(list);
  UNUSED(data);
}

void List_First(List_t *const list)
{
  UNUSED(list);
}

bool List_Copy_First(List_t list, Data_t *data)
{
  UNUSED(list);
  UNUSED(data);
  return false;
}

void List_Delete_First(List_t *const list)
{
  UNUSED(list);
}

void List_Post_Delete(List_t *const list)
{
  UNUSED(list);
}

void List_Post_Insert(List_t *const list, Data_t data)
{
  UNUSED(list);
  UNUSED(data);
}

bool List_Copy(List_t list, Data_t *data)
{
  UNUSED(list);
  UNUSED(data);
  return false;
}

void List_Active_Update(const List_t *const list, Data_t data)
{
  UNUSED(list);
  UNUSED(data);
}

void List_Active_Next(List_t *const list)
{
  UNUSED(list);
}

bool List_Is_Active(List_t list)
{
  UNUSED(list);
  return false;
}

/* Private function definitions ------------------------------------------------------------------*/