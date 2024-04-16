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
#include "mymalloc.h"
#include "heap.h"

#define MAX_CITY_CONNECTIONS 10

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
  if(!dijkstra)
  {
    return false;
  }

  dijkstra->distances = myMalloc(sizeof(unsigned int) * cityCount);
  if(!dijkstra->distances)
  {
    return false;
  }

  dijkstra->visited = myMalloc(sizeof(bool) * cityCount);
  if(!dijkstra->visited)
  {
    myFree(dijkstra->distances);
    return false;
  }
  for(size_t i=0; i<cityCount; i++)
  {
    dijkstra->visited[i] = false;
    dijkstra->distances[i] = INF;
  }
  dijkstra->distances[sourceCityID] = 0;
  return true;
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
  if(!mapHeap || !dijkstra)
  {
    return false;
  }
  tHeap Heap;
  if(!Heap_Init(&Heap))
  {
    return false;
  }

  Heap_Insert(&Heap, mapHeap[sourceCityID]);

  Data_t city;
  Heap_DeleteMin(&Heap, &city);


  for(size_t i=0; i<MAX_CITY_CONNECTIONS; i++)
  {
    if(city.roadLength[i] > 0){

    }
  }


  Heap_Destruct(&Heap);

  (void)mapHeap;
  (void)dijkstra;
  (void)sourceCityID;
  (void)destination;
  return false;

}

/* Private function definitions ------------------------------------------------------------------*/
