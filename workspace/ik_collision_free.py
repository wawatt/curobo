# Third Party
import torch

# cuRobo
from curobo.geom.types import WorldConfig
from curobo.types.base import TensorDeviceType
from curobo.types.math import Pose
from curobo.types.robot import RobotConfig
from curobo.util_file import (
    get_robot_configs_path,
    get_world_configs_path,
    join_path,
    load_yaml,
    )
from curobo.wrap.reacher.ik_solver import IKSolver, IKSolverConfig

tensor_args = TensorDeviceType()
world_file = "collision_cage.yml"

robot_file = "franka.yml"
content_yml = load_yaml(join_path(get_robot_configs_path(), robot_file))

robot_cfg = RobotConfig.from_dict(
    content_yml["robot_cfg"]
)
world_cfg = WorldConfig.from_dict(load_yaml(join_path(get_world_configs_path(), world_file)))
ik_config = IKSolverConfig.load_from_robot_config(
    robot_cfg,
    world_cfg,
    rotation_threshold=0.05,
    position_threshold=0.005,
    num_seeds=20,
    self_collision_check=True,
    self_collision_opt=True,
    tensor_args=tensor_args,
    use_cuda_graph=True,
)
ik_solver = IKSolver(ik_config)

q_sample = ik_solver.sample_configs(50)
kin_state = ik_solver.fk(q_sample)
goal = Pose(kin_state.ee_position, kin_state.ee_quaternion)
result = ik_solver.solve_batch(goal)
q_solution = result.solution[result.success]