#! /bin/bash

# Flush the old volumes and tables if any
hadoop fs -rm -r -f /demo-tables
hadoop fs -rm -r -f /demo-streams
hadoop fs -rm -r -f /demo-files

# Create Volumes
maprcli volume create -name demo-tables -path /demo-tables -readAce 'p' -writeAce 'p'
maprcli volume create -name demo-streams -path /demo-streams -readAce 'p' -writeAce 'p'
maprcli volume create -name demo-streams -path /demo-files -readAce 'p' -writeAce 'p'

# Create Tables - expecting CDC since we need to be notified of a new image
maprcli table create -path /demo-tables/raw-images -tabletype json

# Create Streams - CDC and processed data
maprcli stream create -path /demo-streams/dbchanges -produceperm p -consumeperm p -topicperm p -ischangelog true
maprcli stream topic create -path /demo-streams/dbchanges -topic topic1 -partitions 3

# Set up table change propagation
maprcli changelog add -path /demo-tables/raw-images -changelog /demo-streams/dbchanges:topic1
