#!/bin/bash

module unload freesurfer
module load freesurfer/5.3.0
source /N/soft/cle4/freesurfer/5.3.0/FreeSurferEnv.sh

curl -X POST -H "Content-Type: application/json" -d "{\"msg\":\"Importing nifti\"}" $SCA_PROGRESS_URL

#open config.json and pull source_dir containing raw input files

#use isnifti provided by freesurfer to find nifti (create symlinks on the current task dir)

#create products.json containing something like
#{"files": [{"filename": "10142_3_MPRAGE.nii"}], "type": "nifti"}


