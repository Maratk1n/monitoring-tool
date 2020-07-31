#!/bin/bash

for i in {1..10}
do
  temperature=$(( ( RANDOM % 6 ) + 22 ))
  pressure=$(( ( RANDOM % 2 ) + 3 ))
  engine_speed=$(( ( RANDOM % 20 ) + 300 ))
  fuel_level=$(( ( RANDOM % 7 ) + 70 ))

  curl --header "Content-Type: application/json" \
    --request POST \
    --data "{\"temperature\":$temperature.0,\"pressure\":$pressure.0,\"engine_speed\":$engine_speed,\"fuel_level\":$fuel_level}" \
    http://localhost:5000/data

  sleep 0.1
done


