import serial
import time

# 設定 Arduino 串口（視你的系統調整）
ARDUINO_PORT = "COM3"  # Windows: "COM3", Linux/Mac: "/dev/ttyUSB0"
BAUD_RATE = 115200

# 連接 Arduino
arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # 等待 Arduino 初始化

def move_mouse_to_target(target_x, target_y, screen_w=1920, screen_h=1080):
    """
    透過 Arduino 移動滑鼠到指定座標。
    :param target_x: 目標 X 座標
    :param target_y: 目標 Y 座標
    """
    screen_center_x = screen_w / 2
    screen_center_y = screen_h / 2

    dx = int(target_x - screen_center_x)
    dy = int(target_y - screen_center_y)

    # 限制最大移動距離
    dx = max(min(dx, 300), -300)
    dy = max(min(dy, 300), -300)

    command = f"M {dx} {dy}\n"
    arduino.write(command.encode())  # 發送指令給 Arduino
    time.sleep(0.05)  # 給 Arduino 反應時間

def auto_fire():
    """
    透過 Arduino 觸發滑鼠點擊。
    """
    arduino.write(b"C\n")  # 發送 "C" 命令
    time.sleep(0.05)

if __name__ == "__main__":
    print("3 秒後移動滑鼠到 (960, 540)")
    time.sleep(3)
    move_mouse_to_target(960, 540)

    print("1 秒後開槍！")
    time.sleep(1)
    auto_fire()
