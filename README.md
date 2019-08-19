# pyRender
Lightweight Cuda Renderer with Python Wrapper.

<!-- ## Processing Result -->
![pyRender Teaser](https://github.com/hjwdzh/pyRender/raw/master/resources/teaser.jpg)

### Compile
Change compile.sh line 5 to the glm library include path. This library can be downloaded from this [**link**](https://github.com/g-truc/glm).
```
cd lib
sh compile.sh
```
Please remember to set the library path correctly through
```
export LD_LIBRARY_PATH=/your/cuda/library/path
```

### Example
```
cd src
python example.py ../resources/occlude.obj
```
You will be able to see the rendered images in resources folder.

## Author
- [Jingwei Huang](mailto:jingweih@stanford.edu)

&copy; 2019 Jingwei Huang All Rights Reserved

**IMPORTANT**: This code is part of the following paper. If you use this code please cite the following in any resulting publication:
```
@article{huang2019framenet,
  title={FrameNet: Learning Local Canonical Frames of 3D Surfaces from a Single RGB Image},
  author={Huang, Jingwei and Zhou, Yichao and Funkhouser, Thomas and Guibas, Leonidas},
  journal={arXiv preprint arXiv:1903.12305},
  year={2019}
}
```
