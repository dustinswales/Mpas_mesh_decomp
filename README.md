This repository contains a workflow that does the following:

Install METIS (and dependencies) => Downloads MPAS graph file => Create decomposition files => Store as GitHub artifact

MPAS Graph files are retrieved from: https://www2.mmm.ucar.edu/projects/mpas/site/downloads/meshes.html 

To change/add the mesh and decompositions created, modify .github/workflows/build_decomp.yml
