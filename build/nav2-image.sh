export ROS_DISTRO=humble
git clone https://github.com/ros-planning/navigation2.git --branch humble
docker build --tag navigation2:$ROS_DISTRO \
  --build-arg FROM_IMAGE=ros:$ROS_DISTRO \
  --build-arg OVERLAY_MIXINS="release ccache lld" \
  --cache-from ghcr.io/ros-planning/navigation2:main \
  ./navigation2