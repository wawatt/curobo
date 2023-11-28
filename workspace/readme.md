# RUN CUROBO ON WIN10/11 OS

## installation

1. python environment with pytorch >= 1.10.

2. install git-lfs, run 
```
git lfs install
```
3. modify for win11 OS (finished on this branch)
- src/curobo/curobolib/cpp/self_collision_kernel.cu, modify
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
4. build with log
```
pip install -e . --no-build-isolation --log log_install.txt
```
5. verify that all unit tests pass
```
pip install pytest
python -m pytest . 
```



## install in isaac_sim-2023.1.0-hotfix.1
```
C:/Users/XXX/AppData/Local/ov/pkg/isaac_sim-2023.1.0-hotfix.1/python.bat -m pip install tomli wheel  (maybe)
C:/Users/XXX/AppData/Local/ov/pkg/isaac_sim-2023.1.0-hotfix.1/python.bat -m pip install -e .[isaac_sim] --no-build-isolation --log log_install.txt
```
Don't worry about WARNING and pip's dependency errors

## demos
1. generate usd file
    ```
    C:/Users/XXX/AppData/Local/ov/pkg/isaac_sim-2023.1.0-hotfix.1/python.bat examples/isaac_sim/util/convert_urdf_to_usd.py --robot ur5e_new.yml --save_usd
    ```
2. open usd file with Issac Sim src\curobo\content\assets\robot\ur_description.ur5e_new.usd
   
3. export to yaml with sphere

4. test Robot Configuration
    ```
    C:/Users/XXX/AppData/Local/ov/pkg/isaac_sim-2023.1.0-hotfix.1/python.bat examples/isaac_sim/motion_gen_reacher.py --robot ur5e_new.yml --visualize_spheres
    ```

   