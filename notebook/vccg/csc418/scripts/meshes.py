import numpy as np
import matplotlib.pyplot as plt


def write_obj(V, F, UV, UF, NV, filename:str):
    """
    Write a triangle or quad mesh to a .obj file
    
    V:  #V by 3 numpy array of vertex positions
    F:  #F by poly=(3 or 4) numpy array of mesh face indices into V
    UV  #UV by 2 numpy array of UV positions
    UF  #F by poly numpy array of mesh face indices into UV
    NV  #F by 3 numpy array of normal vectors
    """
    if not filename.endswith(".obj"):
        raise NotImplementedError("File extension not supported")
        
    with open(filename, "w") as f:
        for i in range(V.shape[0]):
            f.write(f"v {V[i, 0]} {V[i, 1]} {V[i, 2]}\n")
        for i in range(UV.shape[0]):
            f.write(f"vt {UV[i, 0]} {UV[i, 1]}\n")
        for i in range(NV.shape[0]):
            f.write(f"vn {NV[i, 0]} {NV[i, 1]} {NV[i, 2]}\n")
        for i in range(F.shape[0]):
            f.write("f")
            for j in range(F.shape[1]):
                f.write(f" {F[i,j]+1}/{UF[i,j]+1}")
            f.write("\n")
            
            
# --8<-- [start:cube]
def cube():
    # The 8 vertices
    V = np.array([
        [1, -1, 1], [-1, -1, 1], [-1, 1, 1], [1, 1, 1], 
        [1, 1, -1], [-1, 1, -1], [-1, -1, -1], [1, -1, -1]])
    # The 6 faces
    F = np.array([
        [0, 7, 4, 3], [0, 3, 2, 1], [1, 2, 5, 6],
        [7, 6, 5, 4], [3, 4, 5, 2], [0, 1, 6, 7]
    ])
    
    # 14 points on the cube
    UV = np.array([
        [0.  , 0.25], [0.25, 0.25], [0.25, 0.  ], [0.5 , 0.  ],
        [0.5 , 0.25], [0.75, 0.25], [1.  , 0.25], [1.  , 0.5 ],
        [0.75, 0.5 ], [0.5 , 0.5 ], [0.5 , 0.75], [0.25, 0.75],
        [0.25, 0.5 ], [0.  , 0.5 ]
    ])
    
    # Map the 14 UV points onto the endpoints of the face
    UF = np.array([
        [ 1,  4,  9, 12], [12,  9, 10, 11], [ 5,  6,  7,  8],
        [ 1,  2,  3,  4], [ 4,  5,  8,  9], [ 0,  1, 12, 13]
    ])
    
    # The normal direction of each face
    NV = np.array([
        [ 1,  0,  0], [ 0,  0,  1], [-1,  0,  0], 
        [ 0,  0, -1], [ 0,  1,  0], [ 0, -1,  0]
    ])
    
    return V, F, UV, UF, NV
# --8<-- [end:cube]

# --8<-- [start:sphere]
def sphere(num_faces_u=16, num_faces_v=16):
    thetas = np.tile(np.linspace(0, 2 * np.pi, num_faces_u+1), num_faces_v)[:, None]
    phis = np.repeat(np.linspace(0, np.pi, num_faces_v), num_faces_u+1)[:, None]

    V = np.hstack([
        np.sin(phis) * np.cos(thetas),
        np.sin(thetas) * np.sin(phis),
        np.cos(phis)
    ])
    
    f_base = np.tile(np.arange(1, num_faces_u+1), num_faces_v)
    f_base = f_base + (num_faces_v)* np.repeat(np.arange(num_faces_v), num_faces_u)
    
    F = np.hstack([
        f_base[:, None], 
        f_base[:, None] + 1, 
        f_base[:, None] + num_faces_u + 1, 
        f_base[:, None] + num_faces_u
    ])

    UV = np.hstack([
        np.tile(np.linspace(0, 1, num_faces_u+1), num_faces_v)[:, None],
        np.repeat(np.linspace(0, 1, num_faces_u+1), num_faces_v)[:, None]
    ])

    UF = F

    # We approx the normal by the top left vertex
    NV = -V
    return V, F, UV, UF, NV
# --8<-- [end:sphere]

write_obj(*cube(), filename="../assets/meshes/cube.obj")
write_obj(*sphere(), filename="../assets/meshes/sphere.obj")