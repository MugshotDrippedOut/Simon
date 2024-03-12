/*!
 * \file       data.c
 * \author     Dulik
 * \date       9. 3. 2015
 * \brief      Implementation of the data module.
 * **********************************************************************
 * \attention
 * &copy; Copyright (c) 2022 FAI UTB. All rights reserved.
 *
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */
/* Includes --------------------------------------------------------------------------------------*/
#include "data.h"

#include <stdio.h>
#include <string.h>

#include "ioutils.h"

/* Private macro ---------------------------------------------------------------------------------*/
/* Private types ---------------------------------------------------------------------------------*/
/* Private variables -----------------------------------------------------------------------------*/
/* Private function declarations -----------------------------------------------------------------*/
/* Exported functions definitions ----------------------------------------------------------------*/

int Data_Cmp(const Data_t *d1, const Data_t *d2) {
  return strcmp(d1->name, d2->name);
}

bool Data_Get(Data_t *data) {
  size_t eoln_pos = 0;
  printf("Please enter name: ");

  if (!io_utils_get_string(data->name, sizeof(data->name))) {
    return false;
  }

  eoln_pos = strcspn(data->name, "\n\r"); /* Najdi pozici konce radku */
  data->name[eoln_pos] = 0;               /* a "ustrihni" konec radku */
  printf("Enter age, weight and height (separated by Enter):\n");

  if (!io_utils_get_double(&data->age)) {
    return false;
  }

  if (!io_utils_get_double(&data->weight)) {
    return false;
  }

  if (!io_utils_get_double(&data->height)) {
    return false;
  }

  return true;
}

void Data_Print(Data_t *data) {
  printf("Name=%s, age=%0.1lf, weight=%0.1lf, height=%0.1lf\n", data->name,
         data->age, data->weight, data->height);
}

/* Private function definitions ----------------------------------------------*/
