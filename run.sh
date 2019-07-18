#!/bin/sh

# first get the current working directory
CODEDIR=$(pwd);

# use timestamp as temporary folder name
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S");

mkdir ../srun/$TIMESTAMP
cp -r $CODEDIR ../srun/$TIMESTAMP/code

cd ../srun/$TIMESTAMP

# make sure nohup.out doesn't exist
touch nohup.out
rm nohup.out

NPARSIM=$1;
NCORES=$2;
MEMGB=$3;

nohup ./code/run_local.sh $TIMESTAMP $CODEDIR $NPARSIM $NCORES $MEMGB &

