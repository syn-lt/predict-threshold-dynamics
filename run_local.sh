#!/bin/sh

echo ""
echo ""
echo "Running " $1
echo ""

if $8
then
    TESTFLAG='-t'
    DESTINATION='tests'
else
    TESTFLAG=''
    DESTINATION='completed'
fi


if $6
then
   echo "doing local"
   python -m code.model.main -c $3 $TESTFLAG
else
   echo "doing nonlocal"
   srun -p $7 -c $4 --mem $5 --time 29-00 python -m code.model.main -c $3 $TESTFLAG
fi

cp code/run_analysis.sh .

echo "Done."

CRDIR=$(pwd);

mkdir -p ../../$DESTINATION/
mv $CRDIR ../../$DESTINATION/$1

#echo "Not cleaning up, remove manually"





