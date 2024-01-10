import os
import asyncio
import aiohttp

async def upload_file(session, code):
    # 업로드할 이미지 파일 경로
    image_file_path = f'/home/user/_SEND/M{code}.jpg'

    # 업로드할 URL
    upload_url = f'http://202.31.101.253:{code}/upload'

    if os.path.exists(image_file_path):
        async with session.post(upload_url, data={'file': open(image_file_path, 'rb')}) as response:
            if response.status == 200:
                res_data = await response.json()
                print('Result', res_data.get('message', ''))
                if res_data['message'] == 'IG':
                    r_ = '/home/user/IG_'
                    if os.path.exists(r_):
                        pass
                    else:
                        os.mkdir(r_)
                    r = '/home/user/IG_/log.txt'
                    with open(r, 'w') as f:
                        f.write('----NONE' + '/n')
                    f.close()
                else:
                    print('PASS')
            else:
                print('Error:', response.status)

async def main():
    try:
        code = 2901
        await asyncio.wait_for(upload_file(session, code), timeout=10.0)  # 10초 동안 응답을 기다림
    except asyncio.TimeoutError:
        print("응답이 없어 타임아웃 발생")
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession()
    loop.run_until_complete(main())
