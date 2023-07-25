# Sensor-Data-ROS-Arduino-
Upload ino file in NodeMcu and set the parameter like ip address and port accordingly your laptop ip address, then open roscore in one terminal and type in another terminal rosrun rosserial_python serial_node.py tcp, now run subscrtiber file in backend which will save all data to csv file coming from sensor
roscore
rosrun rosserial_python serial_node.py tcp
python3 Sensor_Data_Subscriber.py
