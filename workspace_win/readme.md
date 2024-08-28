# RUN CUROBO ON WIN10/11 OS

## installation

1. python environment with pytorch >= 1.10.

2. install git-lfs, run 
```
git lfs install
```
1. modify for win11 OS (finished on this branch) 
- src/curobo/curobolib/cpp/self_collision_kernel.cu, modify 【official repo changed from v0.7.4】
    ```
    {.d = 0.0, .i = 0, .j = 0};
    ```
    to
    ```
    {0.0, 0, 0};
    ```
- src/curobo/util/usd_helper.py
    When the function join_path is used for connecting frames on Win OS, it is not compatible. Therefore, we wrote a join_tree function and used it to replace some join_path functions to solve the problem.
    ```
    def join_tree(path1, path2):
        return path1+"/"+path2
    ```
1. build with log
```
pip install -e . --no-build-isolation --log log_install.txt
```
1. verify that all unit tests pass
```
pip install pytest
python -m pytest . 
```



## install in isaac_sim-4.0.0
1. install cuda11.8
2. restart NVIDIA Omniverse, after installation, CUDA_HOME will be detected automatically.
3. run
    ```
    set TORCH_CUDA_ARCH_LIST=8.6+PTX // for RTX 3050ti
    set TORCH_CUDA_ARCH_LIST=8.9+PTX // for RTX 4060ti
    set omni_python=/path/to/isaac_sim-4.0.0/python.bat
    %omni_python% -m pip install tomli wheel ninja
    %omni_python% -m pip install -e .[isaacsim] --no-build-isolation --log log_install.txt
    ```
    Don't worry about WARNING and pip's dependency errors

## demos
1. generate usd file
    ```
    %omni_python% examples/isaac_sim/util/convert_urdf_to_usd.py --robot step.yml --save_usd
    ```
2. open usd file with Issac Sim src\curobo\content\assets\robot\ur_description.ur5e_new.usd
   
3. export to yaml with sphere

4. test Robot Configuration
    ```
    %omni_python% examples/isaac_sim/motion_gen_reacher.py --robot ur5e.yml --visualize_spheres
    ```

   