# vacuum_cmd
commuication for control solenoid valve.

---

## Communicate Using pyFirmata

### 1. Upload StandardFirmata.ino into Arduino Uno.

<br>

### 2. Connect Arduino uno into vacuum system.

Check the suction gripper manual page.

https://www.notion.so/Suction-Gripper-61775be6f6b241709b4bf4eefb0ca258#ff778a6f20524d41809ff8164e29a848

<br>

### 3. Import rosserial package to launch file.

In vacuum_planner.launch, write down below line

```
<node pkg="unld_indy_planner" type="vacuum_controller.py" name="vacuum_controller" output="log"/>
```

<br>

### 4. Check if the entire system works.

---

## Communicate Using Rosserial

### 0. Install dependencies

```
sudo apt-get install ros-noetic-rosserial-python
```

<br>

### 1. Upload vacuum_cmd.ino into Arduino Uno.

Currently, solenoid valve No. 1, 2, 3, 4, 5, 6 is connected to pin number 5, 3, 9, 6, 11, 10, respectively.
You can manually change them, but they must be in digital pin.

<br>

### 2. Connect Arduino uno into vacuum system.

Check the suction gripper manual page.

https://www.notion.so/Suction-Gripper-61775be6f6b241709b4bf4eefb0ca258#ff778a6f20524d41809ff8164e29a848

<br>

### 3. Import rosserial package to launch file.

In vacuum_planner.launch, change below line

```
<node pkg="unld_indy_planner" type="vacuum_controller.py" name="vacuum_controller" output="log"/>
```

into

```
    <node pkg="rosserial_python" type="serial_node.py" name="serial_node">
        <param name="port" value="/dev/ttyACM0"/>
        <param name="baud" value="57600"/>
    </node>
```

<br>

### 4. Check if the entire system works.
