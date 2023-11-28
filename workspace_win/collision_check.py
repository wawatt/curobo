# Third Party
import torch
# cuRobo
from curobo.types.base import TensorDeviceType
from curobo.wrap.model.robot_world import RobotWorld, RobotWorldConfig

robot_file = "franka.yml"

# create a world from a dictionary of objects
# cuboid: {} # dictionary of objects that are cuboids
# mesh: {} # dictionary of objects that are meshes
world_config = {
    "cuboid": {
        "table": {"dims": [2, 2, 0.2], "pose": [0.4, 0.0, 0.3, 1, 0, 0, 0]},
        "cube_1": {"dims": [0.1, 0.1, 0.2], "pose": [0.4, 0.0, 0.5, 1, 0, 0, 0]},
    },
    "mesh": {
        "scene": {
            "pose": [1.5, 0.080, 1.6, 0.043, -0.471, 0.284, 0.834],
            "file_path": "scene/nvblox/srl_ur10_bins.obj",
        }
    },
}

tensor_args = TensorDeviceType()
config = RobotWorldConfig.load_from_config(robot_file, world_config,
                                          collision_activation_distance=0.0)
curobo_fn = RobotWorld(config)


import datetime
print(datetime.datetime.now()) 
# create spheres with shape batch, horizon, n_spheres, 4.
q_sph = torch.randn((10, 1, 1, 4), device=tensor_args.device, dtype=tensor_args.dtype)
q_sph[...,3] = 0.2 # radius of spheres

d = curobo_fn.get_collision_distance(q_sph)
# print(d)

q_s = curobo_fn.sample(3, mask_valid=False)
print(q_s)

q_s = torch.torch.FloatTensor([[0, 0, 0, 0, 0, 0, 1.0]]).cuda()

d_world, d_self = curobo_fn.get_world_self_collision_distance_from_joints(q_s)
print(d_world)
print(d_self)
# state = curobo_fn.get_kinematics(q_s)
print(datetime.datetime.now()) 