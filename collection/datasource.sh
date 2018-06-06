#!/bin/bash

export datasource_json=$(cat datasource.json|tr "\n" " ")

curl http://admin:admin@localhost:3000/api/datasources -X POST -H 'Content-Type: application/json;charset=UTF8' --data-binary ''"$datasource_json"''
