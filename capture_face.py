import cv2
import os
import time

print("调用相机中...")
cap = cv2.VideoCapture(0)
while True:
    filename = input("请输入姓名拼音，以回车结束：")
    dirt = 'D:/faceImages/' + filename
    os.makedirs(dirt)
    print("人脸信息子文件夹创建成功")
    print('调整姿势\n正常速度转动头部，保证脸部每个角度都有照片\n按下，y再打回车，弹窗出现即自动开始拍照')
    while True:
        state = input()
        if state == 'y':
            break

    flag = 1
    num = 1
    while(cap.isOpened()):
        ret_flag, Vshow = cap.read()
        cv2.imshow("Capture_Test", Vshow)
        pic_name = '/'  + str(num) +  '.jpg'
        cv2.imwrite(dirt + pic_name, Vshow)
        print('%s.jpg done'%(num))
        num += 1
        if num == 601:
            break
        k = cv2.waitKey(1) & 0xFF
        if k == ord('o'):
            break
        if k == ord('p'):
            print('暂停中，按c继续')
            while True:
                ret_flag, Vshow = cap.read()
                cv2.imshow("Capture_Test", Vshow)
                k = cv2.waitKey(1) & 0xFF
                if k == ord('c'):
                    break
        time.sleep(0.02)  # 延时0.2s,每隔0.2s拍摄一张

    print('拍照进程结束，继续按a后回车，退出按q后回车')
    k = input()
    if k == 'a':
        i = 0
    if k == 'q':
        break

cap.release()
cv2.destroyAllWindows()


