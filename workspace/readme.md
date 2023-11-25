# installation
https://curobo.org/source/getting_started/1_install_instructions.html

1.  python environment with pytorch >= 1.10.

2.  install git-lfs, run 
```
git lfs install
```
3. build
```
git clone https://github.com/NVlabs/curobo.git 
pip install -e . --no-build-isolation
```
4. verify that all unit tests pass
```
python -m pytest . 
```


# windows
src\curobo\curobolib\cpp\self_collision_kernel.cu
```
{.d = 0.0, .i = 0, .j = 0};
```
to
```
{0.0, 0, 0};
```

# visualize
```
pip install urdfpy
```