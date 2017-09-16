#!/usr/bin/env bash

ROOT_DIR=$(pwd)
SLEUTH_3_0="SLEUTH3.0beta_p01_linux"
SLEUTH_GA="SLEUTHGA"


echo "Sleuth compiling script"
echo "Options are:"
echo "1. Sleuth3.0 2. SleuthGA"
echo "Otherwise it does nothing"
echo "ROOT DIR IS: ${ROOT_DIR}"


compile () {
make clean
make
}

check () {
if [[ $1 == "Sleuth3.0" ]]; then
SLEUTH_DIR=${SLEUTH_3_0}
elif [[ $1 == "SleuthGA" ]]; then
SLEUTH_DIR=${SLEUTH_GA}
else
echo "DEBUG: sleuth_dir var ${SLEUTH_DIR}, script parameter: $1"
echo "Wrong parameter used, quitting"
exit 1
fi
}

main () {
check

cd "${ROOT_DIR}/${SLUETH_DIR}/Whirlgif"
compile
cd "${ROOT_DIR}/${SLEUTH_DIR}/GD"
compile
cd "${ROOT_DIR}/${SLEUTH_DIR}"
compile
cd "${ROOT_DIR}"
}

# Main flow of script
main