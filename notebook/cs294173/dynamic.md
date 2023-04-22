# Aspects of Dynamic 3D Capture

1. Fusing seen content
2. hallucinate unseen content


Baseline
t-NeRF: add time to input 


Though a deformation network

Deform xyz to canonical coordinate frame and apply nerf (Nerfie, DNerf, Deformable-NeRF)

# HyperNeRF

issues with arap on 3d fields: arap on ambient space is not well defined. 
arap works on surface, while nerf is the ambient space (the volume minus the actual surface)


use quaso-static / synthetic monocular sequence from multiview rig to get the best results

how difficult is a dynamic sequence? 
static camera -> static scene


co-visibility

correspondence is not considered
