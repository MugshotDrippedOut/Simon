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

#define MAX_CITY_CONNECTIONS 8

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
  if(dijkstra)
  {
    if(dijkstra->distances)
    {
      myFree(dijkstra->distances);
      dijkstra->distances = NULL;
    }
    if(dijkstra->visited)
    {
      myFree(dijkstra->visited);
      dijkstra->visited = NULL;
    }
  }
}
/*! Counts the distance between sourceCityID city and every other one.
 *
 * \param[in] mapHeap       Heap, that stores each city and it's details.
 * \param[in] dijkstra      \ref tDijkstra structure, where are the shortest paths stored and
 * informations if cities were visited already.
 * \param[in] sourceCityID  Index of starting city.
 * \param[in] destination   Index of our destination.
 *
 * \return  Returns true if the destination is reachable and the value was found, return false
 * otherwise.
 */
bool Dijkstra_Dist(Data_t *mapHeap,
                   tDijkstra *dijkstra,
                   unsigned sourceCityID,
                   unsigned destination)
{
  (void)mapHeap;
  (void)dijkstra;
  (void)sourceCityID;
  (void)destination;
  if(!mapHeap || !dijkstra)
  {
    return false;
  }
  tHeap Heap;
  if(!Heap_Init(&Heap))
  {
    return false;
  }

  dijkstra->distances[sourceCityID] = 0; // Vzdialeost od zdrojoveho mesta je vzdy 0
  Heap_Insert(&Heap, mapHeap[sourceCityID]);

  Data_t city;
  while(Heap_DeleteMin(&Heap, &city))
  {
    dijkstra->visited[city.id] = true; // Vybrane mesto je navstivene

    for(size_t i=0; i<MAX_CITY_CONNECTIONS; i++) // Prejdeme vsetky cesty z mesta
    {
      if(city.roadCityIndex[i] == UINT_MAX)
      {
        break;
      }
      unsigned newDistance = dijkstra->distances[city.id] + city.roadLength[i];
      if(!dijkstra->visited[city.roadCityIndex[i]] && dijkstra->distances[city.roadCityIndex[i]] > newDistance)
        // Ak sme mesto este nenavstivili a nova vzdialenost je mensia ako predosla
        // tak ju ulozime
      {
        dijkstra->distances[city.roadCityIndex[i]] = newDistance;
        Heap_Insert(&Heap, mapHeap[city.roadCityIndex[i]]);
      }
    }
  }

  Heap_Destruct(&Heap);

  if(dijkstra->distances[destination] == INF)
  {
    return false;
  }
  return true;
}

/* Private function definitions ------------------------------------------------------------------*/
