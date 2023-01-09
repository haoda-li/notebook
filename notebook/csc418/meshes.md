# Meshes


## Triangle Meshes
In order to save bandwidth and disk spaces, the goal is to represent a surface as a network of triangles that connect to one another through shared vertices and edges. 

## Mesh Topology (Manifold)
A 2D __manifold__ is a surface in which a small neighborhood around any point could be smoothed out into a bit of flat surface. 

To verify a 2D mesh, we check that 
 1. every edge is shared by exactly two triangles
 2. Every vertex has a single, complete loop of triangles around it 
 
Note that a mesh may not be closed, so that on the __boundaries__ of a mesh with relaxed requirements, we check that 
 1. Every edge is used by either one or two triangles.
 2. Every vertex connects to a single edge-connected set of triangles

### Mesh orientation
The orientation defines the "front/outside" and "back/inside" of a mesh. The front will have _counterclockwise_ order. A connected mesh is __consistently oriented__ if its triangles all agree on which side is front, or equivalently every pair of adjacent triangles is consistently oriented. 

### Indexed Meshes
The simplest way to store a geometry is to store $n$ vertices as

$$V = \{v_{0},..., v_{n-1}\}, v_i \in \mathbb R^3$$

and $m$ faces/meshes as 

$$F = \{F_{0}, ..., F_{m-1}\}, F_{m_1} = (i, j, k) \in \{0, ..., n-1\}^3$$

Note that $i,j,k$ can also define the orientation of the mesh triangles

### Texture Mapping 
Texture mapping is a process of mapping image information onto a surface, i.e. 

$$T:\mathbb R^2 \rightarrow \mathbb R^3$$

Note that a flat surface is very easy to map (as a bilinear interpolation).

### [.OBJ Files](https://en.wikipedia.org/wiki/Wavefront_.obj_file)

__Geometric vertex__  
A vertex can be specified in a line starting with the letter v. That is followed by $(x,y,z[,w])$ coordinates. $W$ is optional and defaults to 1.0. 
```
# List of geometric vertices, with (x, y, z [,w]) coordinates, 
# w is optional and defaults to 1.0.
v 0.123 0.234 0.345 1.0
v ...
...
```

__Parameter space vertices__  
A free-form geometry statement can be specified in a line starting with the string vp. Define points in parameter space of a curve or surface. u only is required for curve points, u and v for surface points and control points of non-rational trimming curves, and u, v and w (weight) for control points of rational trimming curves.

```
# Parameter space vertices in ( u [,v] [,w] ) form; 
# free form geometry statement ( see below )
vp 0.310000 3.210000 2.100000
vp ...
...
```

__Face elements__  
Faces are defined using lists of vertex, texture and normal indices in the format vertex_index/texture_index/normal_index for which each index starts at 1 and increases corresponding to the order in which the referenced element was defined. Polygons such as quadrilaterals can be defined by using more than three indices.

OBJ files also support free-form geometry which use curves and surfaces to define objects, such as NURBS surfaces.

__Vertex indices__  
A valid vertex index matches the corresponding vertex elements of a previously defined vertex list. If an index is positive then it refers to the offset in that vertex list, starting at 1. If an index is negative then it relatively refers to the end of the vertex list, -1 referring to the last element.

Each face can contain three or more vertices.

__Vertex texture coordinate indices__
Optionally, texture coordinate indices can be used to specify texture coordinates when defining a face. To add a texture coordinate index to a vertex index when defining a face, one must put a slash immediately after the vertex index and then put the texture coordinate index. No spaces are permitted before or after the slash. A valid texture coordinate index starts from 1 and matches the corresponding element in the previously defined list of texture coordinates. Each face can contain three or more elements.

__Vertex normal indices__
Optionally, normal indices can be used to specify normal vectors for vertices when defining a face. To add a normal index to a vertex index when defining a face, one must put a second slash after the texture coordinate index and then put the normal index. A valid normal index starts from 1 and matches the corresponding element in the previously defined list of normals. Each face can contain three or more elements.

```
# List of texture coordinates, in (u, [,v ,w]) coordinates,
# these will vary between 0 and 1. v, w are optional and default to 0.
vt 0.500 1 [0]
vt ...
...
# List of vertex normals in (x,y,z) form; 
# normals might not be unit vectors.
vn 0.707 0.000 0.707
vn ...
...

# Polygonal face element
f 1 2 3
f 3/1 4/2 5/3
f 6/4/1 3/5/3 7/6/5
f 7//1 8//2 9//3
f ...
...
```




__Line element__
Records starting with the letter "l" specify the order of the vertices which build a polyline.
```
l 5 8 1 2 4 9
```


```python title="Quad face cube"
--8<-- "csc418/scripts/meshes.py:cube"
```

![cube texture](./assets/meshes/rubiks-cube.png)

<iframe src="./assets/meshes/cube.html" width="100%" height=600 />

### Sphere Mapping
Note that a sphere centered at $c = (c_x, c_y, c_z)$ and radius $r$ can be represented as the image of 

$$S:\mathbb  [0, 2\pi) \times [0, \pi]\rightarrow \mathbb R^3:= (\theta, \phi) = c + r(\sin\phi\cos\theta, \sin\phi\sin\theta, \cos\phi)$$

Therefore, we can sample evenly take $u\times v$ values from the domain


```python title="Quad face sphere"
--8<-- "csc418/scripts/meshes.py:sphere"
```

![sphere texture](./assets/meshes/earth-square.png)

<iframe src="./assets/meshes/sphere.html" width="100%" height=600 />
