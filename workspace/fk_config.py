# Third Party
import torch

# cuRobo
from curobo.cuda_robot_model.cuda_robot_model import CudaRobotModel, CudaRobotModelConfig
from curobo.types.base import TensorDeviceType
from curobo.types.robot import RobotConfig
from curobo.util_file import get_robot_path, join_path, load_yaml


tensor_args = TensorDeviceType()

config_file = load_yaml(join_path(get_robot_path(), "franka.yml"))["robot_cfg"]
robot_cfg = RobotConfig.from_dict(config_file, tensor_args)
kin_model = CudaRobotModel(robot_cfg.kinematics)

# compute forward kinematics:
# torch random sampling might give values out of joint limits
q = torch.rand((10, kin_model.get_dof()), **vars(tensor_args))
out = kin_model.get_state(q)


q_cpu = q.cpu().numpy()
cfg = {}
for i, jn in enumerate(kin_model.joint_names):
    cfg[jn] = q_cpu[:,i]
    print(q_cpu[:,i])
    
import os
import yourdfpy
urdf_file = config_file["kinematics"]["urdf_path"]  
urdf_file2 = os.path.join("src/curobo/content/assets", urdf_file)
from urdfpy import URDF
robot = URDF.load(urdf_file2)
robot.animate(cfg_trajectory=cfg)