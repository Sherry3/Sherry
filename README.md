exp6 running

exp1, exp2, exp3, exp4, exp5 completed(time is not used)

-------------------------------------------------------
Versions:-

4.2	- stable
5.0	- time included
-------------------------------------------------------

exp1	- irqbalance off
	- big files
 
exp2	- irqbalance off
	- core 3 isolated
	- all interrupts to core 3 
	- big files

exp3	- irqbalance off
	- all interrupts to core 3 
	- big files

exp4	- irqbalance off
	- all interrupts to core 3 
	- big files
	- stress 8 cores for 500s

exp5	- irqbalance off
	- core 3 isolated
	- all interrupts to core 3 
	- big files
	- stress 8 cores for 500s

exp6	- equivalent to exp4 with time
	- irqbalance off
	- all interrupts to core 3 
	- big files
	- stress 8 cores for 500s

exp7	- equivalent to exp5 with time
	- irqbalance off
	- core 3 isolated
	- all interrupts to core 3 
	- big files
	- stress 8 cores for 500s

