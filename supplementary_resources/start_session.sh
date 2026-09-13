#!/bin/bash

echo "Updating course repository..."

git pull origin main

mkdir -p student_space/

echo "Repository updated."


echo ""
echo "Work inside: student_space/"