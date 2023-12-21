### nav2


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
