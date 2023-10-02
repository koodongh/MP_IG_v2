# MP_IG_v2
# 엔비젼 SDK
https://drive.google.com/file/d/1jBTOzNma-OTvPM2qyRAIB40FuQjDYuMu/view?usp=drive_link

# 해당폴더 복사
1. send.py
2. main.py
3. _run.py

# 시스템 실행백업
crontab -e
* * * * * sudo python3 /home/user/cam/share/Python/_run.py > /home/user/cam.log 2>&1
* 21 * * * sudo reboot
* 00 * * * sudo reboot
* 04 * * * sudo reboot
