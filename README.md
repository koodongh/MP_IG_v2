# MP_IG_v2
# 엔비젼 SDK
https://drive.google.com/file/d/1jBTOzNma-OTvPM2qyRAIB40FuQjDYuMu/view?usp=drive_link
auto lo
iface lo inet loopback

auto eth0 
iface eth0 inet static 
address 202.31.99.229
netmask 255.255.255.0
gateway 202.31.99.1

auto eth1 
iface eth1 inet static 
address 169.253.5.100
netmask 255.255.255.0
gateway 169.253.5.1

sudo ./MVviewer.run force 

# 해당폴더 복사
1. send.py
2. main.py
3. _run.py

# 시스템 실행백업
crontab -e
* * * * * sudo python3 /home/user/cam/share/Python/_run.py > /home/user/cam.log 2>&1
00 21 * * * sudo reboot
00 01 * * * sudo reboot
00 03 * * * sudo reboot
00 06 * * * sudo reboot
00 09 * * * sudo reboot
00 15 * * * sudo reboot


# 환경변수선언
export OPENBLAS_CORETYPE=ARMV8
