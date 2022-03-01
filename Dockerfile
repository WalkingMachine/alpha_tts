FROM osrf/ros:foxy-desktop

RUN mkdir -p root/dev/src

COPY . root/dev/src

RUN cd root/dev

RUN colcon build

RUN sed -i "$d" /ros_entrypoint.sh
RUN echo 'source "/root/dev/install.bash"' >> /ros_entrypoint.sh
RUN echo 'exec "$@"' >> /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
