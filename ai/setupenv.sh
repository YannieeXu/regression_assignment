#!/bin/bash
export CONDA_YES_ACCEPT_TERMS_OF_SERVICE=true
conda env create -f environment.yml
conda activate regression_env
echo "Environment regression_env created and activated."
