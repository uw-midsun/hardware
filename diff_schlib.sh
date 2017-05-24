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
  branch=${1}
  mkdir "schlib-${branch}"
  cd "schlib-${branch}"

  filename="Schematic Diagrams.SchLib"

  url_arg=$(git rev-parse --verify "${branch}^{commit}")
  if [ $? -ne 0 ]; then
    url_arg=${branch}
  fi

  wget -q "https://raw.githubusercontent.com/uw-midsun/hardware/${url_arg}/altium-lib/${filename}"
  python3 -c "import olefile; [print(x[0]) for x in olefile.OleFileIO('${filename}').listdir(streams=False, storages=True)]"

  cd ..
  rm -rf "schlib-${branch}"
}

diff --suppress-common-lines -y <(read_schlib "${1}") <(read_schlib "${2}")
