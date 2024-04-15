/*!
 * \file       dijkstra.c
 * \author     Ondřej Ševčík
 * \date       6/2019
 * \brief      Implementation of function for Dijkstra algorithm
 * **********************************************************************
 * \attention
 * &copy; Copyright (c) 2022 FAI UTB. All rights reserved.
 *
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

/* Includes --------------------------------------------------------------------------------------*/
#include "dijkstra.h"

#include "heap.h"

/* Private types ---------------------------------------------------------------------------------*/
/* Private macros --------------------------------------------------------------------------------*/
/* Private variables -----------------------------------------------------------------------------*/
/* Private function declarations -----------------------------------------------------------------*/
/* Exported functions definitions ----------------------------------------------------------------*/
bool Dijkstra_Init(tDijkstra *dijkstra, unsigned cityCount, unsigned sourceCityID)
{
  (void)dijkstra;
  (void)cityCount;
  (void)sourceCityID;
  return false;
}

void Dijkstra_Destruct(tDijkstra *dijkstra)
{
  (void)dijkstra;
}

bool Dijkstra_Dist(Data_t *mapHeap,
                   tDijkstra *dijkstra,
                   unsigned sourceCityID,
                   unsigned destination)
{
  (void)mapHeap;
  (void)dijkstra;
  (void)sourceCityID;
  (void)destination;
  return false;
}

/* Private function definitions ------------------------------------------------------------------*/
