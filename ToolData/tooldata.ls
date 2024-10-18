/PROG tooldata
/ATTR
OWNER        = MNEDITOR;
COMMENT      = "TOOLDATA BY CODE AUTOMACAO E ROBOTICA";
PROG_SIZE    = 0;
CREATE       = DATE 17-10-2024  TIME 22:18:29;
MODIFIED     = DATE 17-10-2024  TIME 22:18:29;
FILE_NAME    = ;
VERSION      = 0;
LINE_COUNT   = 0;
MEMORY_SIZE  = 0;
PROTECT      = READ_WRITE;
TCD: STACK_SIZE    = 0,
     TASK_PRIORITY = 50,
     TIME_SLICE    = 0,
     BUSY_LAMP_OFF = 0,
     ABORT_REQUEST = 0,
     PAUSE_REQUEST = 0;
DEFAULT_GROUP = 1,*,*,*,*;
CONTROL_CODE  = 00000000 00000000;
/APPL
/MN
1: ;
2:  !****************************** ;
3:  !*                            * ;
4:  !*     ESSE PROGRAMA FOI      * ;
5:  !*      FEITO PELA CODE       * ;
6:  !*    AUTOMACAO E ROBOTICA    * ;
7:  !*                            * ;
8:  !****************************** ;
9:  ;
10: ! DEFININDO A PR[1] COMO CARTESIANA ;
11: PR[1]=LPOS ;
12: ;
13: ! ---UTOOL 1--- ;
14: ;
15: PR[1,1] = 1231 ;
16: PR[1,2] = 43142 ;
17: PR[1,3] = 154 ;
18: PR[1,4] = 5498 ;
19: PR[1,5] = 453 ;
20: PR[1,6] = 4965 ;
21: UTOOL[1]=PR[1] ;
22: ;
23: ! ---PAYLOAD 1--- ;
24: ! ---(RODAR EM COLD START)--- ;
25: ;
26: $PLST_GRP1[1].$PAYLOAD = 45 ;
27: $PLST_GRP1[1].$PAYLOAD_X = 5451 ;
28: $PLST_GRP1[1].$PAYLOAD_Y = 456 ;
29: $PLST_GRP1[1].$PAYLOAD_Z = 659 ;
30: $PLST_GRP1[1].$PAYLOAD_IX = 123 ;
31: $PLST_GRP1[1].$PAYLOAD_IY = 4124 ;
32: $PLST_GRP1[1].$PAYLOAD_IZ = 5325 ;
/POS
/END
