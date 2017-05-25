#!/bin/bash

# Usage: ./diff_schlib.sh branch_a branch_b
#
# Example: ./diff_schlib.sh master elec_135_elec_161_chaos
#
# Also supports specific commits!
#
# Example: ./diff_schlib.sh 1fef master

pip3 install olefile > /dev/null

read_schlib() {
  branch=
  filename="Schematic Diagrams.SchLib"

  commit_hash=$(git rev-parse --verify "${1}^{commit}")
  if [ $? -ne 0 ]; then
    exit 1
  fi

  wget -q "https://raw.githubusercontent.com/uw-midsun/hardware/${commit_hash}/altium-lib/${filename}" -O "${commit_hash}.SchLib"
  python3 -c "import olefile; [print(x[0]) for x in olefile.OleFileIO('${commit_hash}.SchLib').listdir(streams=False, storages=True)]" | sort

  rm -f "${commit_hash}.SchLib"
}

YELLOW=$(tput bold && tput setaf 3)
GREEN=$(tput bold && tput setaf 2)
RED=$(tput bold && tput setaf 1)
CLEAR=$(tput sgr0)

NEW='\+'
DEL='\-'

lib_diff="${1}! !${2}\n"
lib_diff+=$(comm -3 --output-delimiter='!' <(read_schlib "${1}" | sort) <(read_schlib "${2}" | sort) | sed -r "s/!/ !${NEW}!/; s/^([^ ].*)$/\1!${DEL}!/")

echo -e "${lib_diff}" | column -s '!' -t | sed -r "s/^${1}([[:space:]]+)${2}$/${YELLOW}${1}\1${2}${CLEAR}/; s/ ${DEL}/ ${RED}${DEL}${CLEAR}/; s/ ${NEW}/ ${GREEN}${NEW}${CLEAR}/"
