export PATH=$PATH:/usr/local/cuda/bin
export LD_LIBRARY_PATH=/usr/local/cuda/lib64


export GLM_INCLUDE_DIR=/orions4-zfs/projects/jingweih/glm
export CFLAGS="-I$GLM_INCLUDE_DIR -I. -I/usr/local/cuda/include"
export DFLAGS="-L/usr/local/cuda/lib64"

# build source
g++ -std=c++11 -c main.cpp $CFLAGS -O2 -o main.o -fPIC
g++ -std=c++11 -c buffer.cpp $CFLAGS -O2 -o buffer.o -fPIC
nvcc -std=c++11 -c render.cu $CFLAGS -D_FORCE_INLINES -O2 -o render.o --compiler-options '-fPIC'

# test buffer
g++ -std=c++11 main.o buffer.o render.o $CFLAGS $DFLAGS -O2 -o libRender.so -shared -fPIC -lcudart

#g++ -std=c++11 main.o buffer.o loader.o render.o $CFLAGS $DFLAGS -o render -lcudart

#rm *.o
