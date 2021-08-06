#! /usr/bin/env bash
#
# Create and/or activate Python environment for the project
#

RED='\033[1;31m'
CYAN='\033[1;36m'
NC='\033[0m' # No Color

if ! (return 0 2>/dev/null) ; then
    # If return is used in the top-level scope of a non-sourced script,
    # an error message is emitted, and the exit code is set to 1
    echo
    echo -e $RED"This script should be sourced like"$NC
    echo "    . ./activate.sh"
    echo
    exit 1  # we detected we are NOT source'd so we can use exit
fi

ENV_NAME="fastapi-playground"
ENV_FILE="environment.yml"

if type conda 2>/dev/null; then
    if conda info --envs | grep "\b${ENV_NAME}\s"; then
      echo -e $CYAN"activating environment ${ENV_NAME}"$NC
    else
      if [[ -z $(conda list --name base | grep mamba) ]]; then
        echo "..installing mamba.."
        conda install mamba --name base
      fi
      echo -e $CYAN"..creating environment ${ENV_NAME} with ${PYTHON}.."$NC
      conda create -y -n ${ENV_NAME} ${PYTHON}
      conda activate ${ENV_NAME}
      echo "..installing dependencies from ${ENV_FILE}.."
      mamba env update --quiet -n ${ENV_NAME} -f ${ENV_FILE}
      conda deactivate  # RE-activate conda env so python will have access to conda installed deps
    fi
else
    echo
    echo -e $RED"(!) Please install anaconda"$NC
    echo
    return 1  # we are source'd so we cannot use exit
fi

conda activate ${ENV_NAME}
