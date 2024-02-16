/*!
 * \file       FSM.c
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
/* Includes ------------------------------------------------------------------*/
#include "FSM.h"

/* Private types -------------------------------------------------------------*/
/* Private macros ------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/
/* Private function declarations ---------------------------------------------*/
/* Exported functions definitions --------------------------------------------*/
void FSM_RemoveNotes(FILE* input, FILE* output) {
  (void)input;
  (void)output;
  if (input == NULL || output == NULL) {
    return;
  }
  /* Types of comment and what to look out for */
  /* Types */
  // 1. Single line comment
      //
  // 2. Multi line comment
      /*
      */
  /* Look out for */
    // ""
    // ''
    // //
    // /*
    // */
    // \n

  enum {
    STATE_DEFAULT, 
    STATE_SLASH, /* Ceck for / */
    STATE_COMMENT, /* */
    STATE_STAR, /* Check for * */
    STATE_END /* Check for end of comment */
  } state = STATE_DEFAULT;
  
  int ch;

  while((ch = fgetc(input)) != EOF) {
    switch (state) {
      case STATE_DEFAULT:
        if (ch == '/') {
          state = STATE_SLASH;
        } else {
          fputc(ch, output);
        }
        break;
      case STATE_SLASH:
        if (ch == '/') {
          state = STATE_COMMENT;
        } else if (ch == '*') {
          state = STATE_STAR;
        } else {
          fputc('/', output);
          fputc(ch, output);
          state = STATE_DEFAULT;
        }
        break;
      case STATE_COMMENT:
        if (ch == ''
    }

  }



}

/* Private function definitions ----------------------------------------------*/