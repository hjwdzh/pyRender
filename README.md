# pyRender
Lightweight Cuda Renderer with Python Wrapper.

### Compile
```
cd lib
sh compile.sh
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