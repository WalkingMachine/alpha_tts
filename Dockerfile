FROM osrf/ros:foxy-desktop

RUN mkdir -p ~/dev/src/alpha_tts

COPY . /root/dev/src

WORKDIR /root/dev

RUN colcon build

RUN sed -i "$d" /ros_entrypoint.sh
RUN echo 'source "/root/dev/install/setup.bash"' >> /ros_entrypoint.sh
RUN echo 'exec "$@"' >> /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
