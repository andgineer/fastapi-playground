#! /usr/bin/env bash
#
# Create and/or activate Python environment for the project
#

ENV_NAME="fastapi-playground"
ENV_FILE="environment.yml"
PRIMARY_PYTHON_VERSION="3.12"  # sync with .github/workflows/static.yml

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

# Detect conda installation (prefer Miniforge which includes mamba)
CONDA_BASE=""
if [[ -d "$HOME/miniforge3/" ]] ; then
  CONDA_BASE="$HOME/miniforge3"
  echo -e $CYAN"Using Miniforge (includes mamba)"$NC
elif [[ -d "$HOME/mambaforge/" ]] ; then
  CONDA_BASE="$HOME/mambaforge"
  echo -e $CYAN"Using Mambaforge (includes mamba)"$NC
elif [[ -d "$HOME/anaconda3/" ]] ; then
  CONDA_BASE="$HOME/anaconda3"
  echo -e $CYAN"Using Anaconda"$NC
elif [[ -d "$HOME/miniconda3/" ]] ; then
  CONDA_BASE="$HOME/miniconda3"
  echo -e $CYAN"Using Miniconda"$NC
else
  echo -e $RED"(!) Please install Miniforge (recommended): https://github.com/conda-forge/miniforge"$NC
  echo -e $RED"    Or Anaconda: https://docs.anaconda.com/anaconda/install/"$NC
  return 1  # we are source'd so we cannot use exit
fi

source "$CONDA_BASE/bin/activate"
conda init

if conda info --envs | grep "\b${ENV_NAME}\s"; then
  echo -e $CYAN"activating environment ${ENV_NAME}"$NC
else
  # Only install mamba if not already available (Miniforge/Mambaforge have it built-in)
  if ! command -v mamba &> /dev/null; then
    echo -e $CYAN"..installing mamba.."$NC
    conda install mamba>=2.0.5 --name base --channel conda-forge --yes
  fi
  echo -e $CYAN"..creating environment ${ENV_NAME} with ${PRIMARY_PYTHON_VERSION}.."$NC
  conda create -y -n ${ENV_NAME} python="${PRIMARY_PYTHON_VERSION}"
  conda activate ${ENV_NAME}
  echo -e $CYAN"..installing dependencies from ${ENV_FILE}.."$NC
  mamba env update --quiet -n ${ENV_NAME} -f ${ENV_FILE}
  pip install -e .
  conda deactivate  # RE-activate conda env so python will have access to conda installed deps
fi

conda activate ${ENV_NAME}
