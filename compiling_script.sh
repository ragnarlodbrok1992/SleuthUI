#!/usr/bin/env bash

ROOT_DIR=$(pwd)

compile () {
make clean
make
}
echo ROOT DIR IS: ${ROOT_DIR}

main () {
cd ${ROOT_DIR}/SLEUTHGA/Whirlgif
compile
cd ${ROOT_DIR}/SLEUTHGA/GD
compile
cd ${ROOT_DIR}/SLEUTHGA
compile
}

# Main flow of script
main