/*!
 * \file       dtmf.c
 * \author     Ondřej Ševčík
 * \date       9/2019
 * \brief      Implementation of DTMF generator module
 * **************************************************************
 * \attention
 * &copy; Copyright (c) 2022 FAI UTB. All rights reserved.
 *
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

/* Includes --------------------------------------------------------------------------------------*/
#include "dtmf.h"

#include "wavfile.h"

#include <math.h>
#include <stdbool.h>

/* Private types ---------------------------------------------------------------------------------*/
/* Private macros --------------------------------------------------------------------------------*/
#define VOLUME 1000

#define UNUSED(x) (void)x
/* Private variables -----------------------------------------------------------------------------*/
static double mSamplesLUT[WAVFILE_SAMPLES_PER_SECOND];

/* Private function declarations -----------------------------------------------------------------*/
/* Exported functions definitions ----------------------------------------------------------------*/
/* Private function definitions ------------------------------------------------------------------*/

/* Function definition ----------------------------------------------------- */
bool DTMF_Generate(Vector_t *vector, char symbol)
{
  UNUSED(symbol);
  static bool initialized = false;
  if (!initialized) {
    for (int i = 0; i < WAVFILE_SAMPLES_PER_SECOND; i++) {
      mSamplesLUT[i] = (double)i / WAVFILE_SAMPLES_PER_SECOND * 2 * M_PI;
    }
    initialized = true;
  }
  if(vector==NULL){
    return false;
  }
  // Pridat filtrovanie symbolov a precyklenie
  Vector_DataType_t lowF = 0;
  Vector_DataType_t highF = 0;
  Vector_DataType_t tone =0;
  
  char arr[16] ={'1','2','3','A','4','5','6','B','7','8','9','C','*','0','#','D'};
  Vector_DataType_t highs[4] = {1209,1336,1477,1633};
  Vector_DataType_t lows[4] = {697,770,852,941};

  // Filter symbols
  bool validSymbol = false;
  for (int i = 0; i < 16; i++) {
    if (symbol == arr[i] || symbol == ' ') {
      validSymbol = true;
      break;
    }
  }
  if (!validSymbol)return false;



  for(int i = 0; i<16;i++){
    if(symbol == arr[i]){
      lowF = lows[i/4];
      highF = highs[i%4];
    }
  }

  for (size_t i = 0; i < WAVFILE_SAMPLES_PER_SECOND; ++i) {
    if(symbol == ' '){
      tone = 0;
      Vector_Append(vector,tone);
    }
    else{
      tone = VOLUME * (sin(lowF* mSamplesLUT[i]) + sin(highF* mSamplesLUT[i])) ;
      Vector_Append(vector,tone);
    }
  }

  return true;
}
