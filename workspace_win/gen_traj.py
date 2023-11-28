# cuRobo
from curobo.geom.sdf.world import CollisionCheckerType
from curobo.types.base import TensorDeviceType
from curobo.types.math import Pose
from curobo.types.robot import JointState, RobotConfig
from curobo.util_file import (
    get_robot_configs_path,
    get_world_configs_path,
    join_path,
    load_yaml,
    )
from curobo.wrap.reacher.motion_gen import MotionGen, MotionGenConfig, MotionGenPlanConfig

tensor_args = TensorDeviceType()
world_file = "collision_table.yml"
robot_file = "franka.yml"
motion_gen_config = MotionGenConfig.load_from_robot_config(
    robot_file,
    world_file,
    tensor_args,
    interpolation_dt=0.01,
)
motion_gen = MotionGen(motion_gen_config)
motion_gen.warmup(enable_graph=True)
robot_cfg = load_yaml(join_path(get_robot_configs_path(), robot_file))["robot_cfg"]
robot_cfg = RobotConfig.from_dict(robot_cfg, tensor_args)
retract_cfg = motion_gen.get_retract_config()

state = motion_gen.rollout_fn.compute_kinematics(
    JointState.from_position(retract_cfg.view(1, -1))
)

retract_pose = Pose(state.ee_pos_seq.squeeze(), quaternion=state.ee_quat_seq.squeeze())
start_state = JointState.from_position(retract_cfg.view(1, -1) + 0.3)
result = motion_gen.plan_single(
    start_state, retract_pose, MotionGenPlanConfig(max_attempts=1)
)
print(result.optimized_plan.position.shape)
traj = result.get_interpolated_plan()
print("Trajectory Generated: ", result.success, result.optimized_dt.item())