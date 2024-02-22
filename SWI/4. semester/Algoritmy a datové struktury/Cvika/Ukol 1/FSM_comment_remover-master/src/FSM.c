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
  /* fputc => insetrs character */


  enum {
    STATE_DEFAULT, 
    STATE_SLASH,
    STATE_SINGLE_LINE_COMMENT,
    STATE_MULTI_LINE_COMMENT,
    STATE_POSSIBLE_END_MULTI_LINE_COMMENT,
    STATE_DOUBLE_QUOTE,
    STATE_SINGLE_QUOTE,
    STATE_ESCAPE_SEQUENCE_DOUBLE_QUOTE,
    STATE_ESCAPE_SEQUENCE_SINGLE_QUOTE
  } state = STATE_DEFAULT;
  
  int ch;

  while((ch = fgetc(input)) != EOF) {
    switch (state) {
      case STATE_DEFAULT:
        if(ch == '/') {
          state = STATE_SLASH;
        } else if(ch == '"') { 
          state = STATE_DOUBLE_QUOTE;
          fputc(ch, output);
        } else if(ch == '\'') { 
          state = STATE_SINGLE_QUOTE;
          fputc(ch, output);
        } else { 
          fputc(ch, output);
        }
        break;
      case STATE_SLASH:
        if(ch == '/') {
          state = STATE_SINGLE_LINE_COMMENT;
        } else if(ch == '*') {
          state = STATE_MULTI_LINE_COMMENT;
        } else { 
          fputc('/', output); 
          fputc(ch, output);
          state = STATE_DEFAULT;
        }
        break;
      case STATE_SINGLE_LINE_COMMENT:
        if(ch == '\n') {
          fputc(ch, output);
          state = STATE_DEFAULT;
        }
        break;
      case STATE_MULTI_LINE_COMMENT:
        if(ch == '*') {
          state = STATE_POSSIBLE_END_MULTI_LINE_COMMENT;
        }
        break;
      case STATE_POSSIBLE_END_MULTI_LINE_COMMENT:
        if(ch == '/') { 
          state = STATE_DEFAULT;
        } else if(ch != '*') {
          state = STATE_MULTI_LINE_COMMENT;
        }
        break;
      case STATE_DOUBLE_QUOTE:
          fputc(ch, output);
          if(ch == '\\') {
              state = STATE_ESCAPE_SEQUENCE_DOUBLE_QUOTE;
          } else if(ch == '"') {
              state = STATE_DEFAULT;
          }
          break;
      case STATE_ESCAPE_SEQUENCE_DOUBLE_QUOTE:
          fputc(ch, output);
          state = STATE_DOUBLE_QUOTE;
          break;
      case STATE_SINGLE_QUOTE:
          fputc(ch, output);
          if(ch == '\\') {
              state = STATE_ESCAPE_SEQUENCE_SINGLE_QUOTE;
          } else if(ch == '\'') {
              state = STATE_DEFAULT;
          }
          break;
      case STATE_ESCAPE_SEQUENCE_SINGLE_QUOTE:
          fputc(ch, output);
          state = STATE_SINGLE_QUOTE;
          break;
          }
  }

}

/* Private function definitions ----------------------------------------------*/