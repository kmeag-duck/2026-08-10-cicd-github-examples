#!/usr/bin/env bash

if [ $1 -lt 0 ]
then
  echo "Energy must be positive"
  exit 59
else
  exit 0
fi
