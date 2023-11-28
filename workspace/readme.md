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
pip install -e . --no-build-isolation --log log_install.txt
```
4. verify that all unit tests pass
```
python -m pytest . 
```


# windows OS build setting
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

# install in Issac Sim on windows OS
```
C:/Users/XXX/AppData/Local/ov/pkg/isaac_sim-2022.2.1/python.bat -m pip install tomli wheel
C:/Users/XXX/AppData/Local/ov/pkg/isaac_sim-2022.2.1/python.bat -m pip install -e .[isaac_sim] --no-build-isolation --log log_install.txt
```

# make yaml 
1. gen usd file
```
C:/Users/XXX/AppData/Local/ov/pkg/isaac_sim-2022.2.1/python.bat examples/isaac_sim/util/convert_urdf_to_usd.py --robot ur5e_new.yml --save_usd
```

2. open usd file with Issac Sim src\curobo\content\assets\robot\ur_description.ur5e_new.usd
   
3. export to yaml with sphere

4. test Robot Configuration
```
C:/Users/XXX/AppData/Local/ov/pkg/isaac_sim-2023.1.0-hotfix.1/python.bat examples/isaac_sim/motion_gen_reacher.py --robot ur5e_new.yml --visualize_spheres
```

   