#!/bin/bash

folders1=`ls -d */`
count=1

for fold1 in $folders1
do
	echo $fold1
	cd $fold1
	folders2=`ls -d */`
	count1=1
   	for fold2 in $folders2
   	do
		echo $fold2
		cd $fold2
		fold3=`ls -d */`
		cd $fold3
		fes_file=`ls *.fes`
		tail -n +6 $fes_file > freeE.csv
		cp ../../../avg_rmsd.py .
		avg_rmsd=`python avg_rmsd.py`
		echo $avg_rmsd
		echo trial_$count1 $avg_rmsd >> ../../pose_score_pose_$count.dat
		let count1=count1+1
		rm freeE.csv avg_rmsd.py
		cd ../../
	done
	cp pose_score_pose_$count.dat ..
	let count=count+1
	cd ../
done

