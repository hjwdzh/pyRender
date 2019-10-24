import numpy as np
import sys
import skimage.io as sio
import os
import sys
import shutil
from objloader import LoadTextureOBJ

libpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(libpath + '/../lib')
import render
import objloader


input_obj = sys.argv[1]

if input_obj[-3:] == 'obj':
	V, F, VT, FT, VN, FN, face_mat, kdmap = objloader.LoadTextureOBJ(input_obj)
else:
	V, F = objloader.LoadOff(input_obj)

print(np.min(V), np.max(V))

# set up camera information
info = {'Height':480, 'Width':640, 'fx':575, 'fy':575, 'cx':319.5, 'cy':239.5}
render.setup(info)

# set up mesh buffers in cuda
context = render.SetMesh(V, F)

cam2world = np.array([[ 0.85408425,  0.31617427, -0.375678  ,  0.56351697 * 2],
	   [ 0.        , -0.72227067, -0.60786998,  0.91180497 * 2],
	   [-0.52013469,  0.51917219, -0.61688   ,  0.92532003 * 2],
	   [ 0.        ,  0.        ,  0.        ,  1.        ]], dtype=np.float32)

world2cam = np.linalg.inv(cam2world).astype('float32')

# the actual rendering process
render.render(context, world2cam)

# get depth information
depth = render.getDepth(info)

# get information of mesh rendering
# vindices represents 3 vertices related to pixels
# vweights represents barycentric weights of the 3 vertices
# findices represents the triangle index related to pixels
vindices, vweights, findices = render.getVMap(context, info)
print(findices.shape)
vis_face = findices.astype('float32') / np.max(findices)
sio.imsave('face.png',vis_face)
sio.imsave('vertex.png',vweights)
'''
#Example: render texture based on the info, loop in python is inefficient, consider move to cpp
uv = np.zeros((findices.shape[0], findices.shape[1], 3), dtype='float32')
for j in range(2):
	uv[:,:,j] = 0
	for k in range(3):
		vind = FT[findices][:,:,k]
		uv_ind = VT[vind][:,:,j]
		uv[:,:,j] += vweights[:,:,k] * uv_ind

mask = np.sum(vweights, axis=2) > 0
mat = face_mat[findices]
diffuse = np.zeros((findices.shape[0],findices.shape[1],3), dtype='uint8')
for i in range(findices.shape[0]):
	for j in range(findices.shape[1]):
		if mask[i,j] == 0:
			diffuse[i,j,:] = 0
			continue
		elif kdmap[mat[i,j]].shape == (1,1,3):
			diffuse[i,j,:] = kdmap[mat[i,j]][0,0]
		else:
			img = kdmap[mat[i,j]]
			x = uv[i,j,0]
			y = 1 - uv[i,j,1]
			x = x - int(x)
			y = y - int(y)
			while x >= 1:
				x -= 1
			while x < 0:
				x += 1
			while y >= 1:
				y -= 1
			while y < 0:
				y += 1

			#uv[i,j,0] = x
			#uv[i,j,1] = y
			x = x * (img.shape[1] - 1)
			y = y * (img.shape[0] - 1)
			px = int(x)
			py = int(y)
			rx = px + 1
			ry = py + 1
			if ry == img.shape[0]:
				ry -= 1
			if rx == img.shape[1]:
				rx -= 1
			wx = (x - px)
			wy = y - py

			albedo = (img[py,px,:] * (1 - wx) + img[py,rx,:] * wx) * (1 - wy) + (img[ry,px,:] * (1 - wx) + img[ry,rx,:]*wx) * wy
			diffuse[i,j,:] = albedo

render.Clear()

sio.imsave('../resources/depth.png', depth / np.max(depth))
sio.imsave('../resources/vweights.png', vweights)
sio.imsave('../resources/diffuse.png', diffuse)
'''
