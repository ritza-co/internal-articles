#!/bin/bash

for file in *.md; do
  basename=${file%.md}
  echo "https://ritza.co/articles/gen-articles/$basename"
done

