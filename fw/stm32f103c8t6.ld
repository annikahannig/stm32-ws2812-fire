
__estack = 0x20005000;


MEMORY
{
	rom (rx) : ORIGIN = 0x08000000, LENGTH = 64K
	ram (rwx) : ORIGIN = 0x20000000, LENGTH = 20K
}


/* Include the common ld script. */
INCLUDE libopencm3_stm32f1.ld

