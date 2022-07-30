#!/bin/bash

folders1=`ls -d */`
#echo $folders1

for fold1 in $folders1
do
	echo $fold1
	cd $fold1
	folders2=`ls -d */`
   	for fold2 in $folders2
   	do
		echo $fold2
		cd $fold2
		tgz_file=`ls *.tgz`
		tar -xvzf $tgz_file
		cd ../
	done
	cd ../
done

