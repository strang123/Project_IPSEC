#!/bin/bash

for(( i=0;i<5;i++ )) do
	python controller.py $(($i)) $(($i)) $(($i)) $(($i))
	sleep 2
	#python tester.py $(($i)) $(($i)) $(($i)) $(($i)) 
done
