FROM etswalkingmachine/alpha_interfaces:dev

RUN mkdir -p ~/dev/src/alpha_tts

COPY . /root/dev/src/alpha_tts

RUN apt-get update
RUN bash src/alpha_tts/install_dependencies.bash

RUN rosdep install -i --from-path src --rosdistro foxy -y

RUN colcon build --packages-select alpha_tts