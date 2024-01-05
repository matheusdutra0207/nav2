### nav2
```
sudo ./nav2-rviz2-container.sh
source opt/ros/humble/setup.bash
cd opt/ros/humble/share/nav2_bringup/maps
ros2 launch nav2_bringup localization_launch.py map:=labsea_slam_toolbox.yaml
```

### Slan-toolbox

To launch slan-toolbox

```
sudo docker run -it --rm --name=slan-toolbox --network=host matheusdutra0207/slan-toolbox:v1 bash
```

```
source opt/ros/humble/setup.bash
git clone https://github.com/matheusdutra0207/nav2.git
ros2 launch slam_toolbox online_async_launch.py params_file:=./nav2/slam_toolbox/params/mapper_params_online_async.yaml use_sim_time:=false

```
