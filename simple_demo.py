import csv
import time
import copy

import cv2 as cv
from utils import playEffect
from model.yolox.yolox_onnx import YoloxONNX


def main():
    # 변수 설정 #################################################################
    cap_device = 1
    cap_width = 960
    cap_height = 540
    fps = 60
    skip_frame = 0

    model_path = "model/yolox/yolox_nano.onnx"
    input_shape = (416,416)
    score_th = 0.75
    nms_th = 0.45
    nms_score_th = 0.1
    with_p6 = False

    frame_count = 0
    play_effect_count = 0
    tmp_class_id = 1

    # 웹캠 설정 ###############################################################
    cap = cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    # 모델 가져오기 #############################################################
    yolox = YoloxONNX(
        model_path=model_path,
        input_shape=input_shape,
        class_score_th=score_th,
        nms_th=nms_th,
        nms_score_th=nms_score_th,
        with_p6=with_p6,
        providers=['CPUExecutionProvider'],
    )

    # label 설정 ###########################################################
    with open('setting/labels.csv', encoding='utf8') as f:
        labels = csv.reader(f)
        labels = [row for row in labels]

    while True:
        start_time = time.time()

        # 웹캠 캡처 #####################################################
        ret, frame = cap.read()
        if not ret: # 캡처가 안됬을때
            continue
        debug_image = copy.deepcopy(frame) # frame(원본)은 모델 예측에 필요하기 때문에

        frame_count += 1
        if (frame_count % (skip_frame + 1)) != 0: # 스킵할 프레임 범위에 있다면
            continue

        # 모델에 캡처한 사진을 예측받기 #############################################################
        bboxes, scores, class_ids = yolox.inference(frame)

        for bbox, score, class_id in zip(bboxes, scores, class_ids):
            # 반복문을 통해 가장 높은 점수의 클래스 찾기
            class_id = int(class_id) + 1
            if score < score_th: # score_th보다 높다면 바운딩 박스 그리기
                continue

            # 바운딩 박스 그리기 ###################################################
            x1, y1 = int(bbox[0]), int(bbox[1])
            x2, y2 = int(bbox[2]), int(bbox[3])

            cv.putText(
                debug_image, 'ID:' + str(class_id) + ' ' +
                labels[class_id][0] + ' ' + '{:.3f}'.format(score),
                (x1, y1 - 15), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2,
                cv.LINE_AA) # 예측한 클래스 바운딩 박스 위에 그리기
            cv.rectangle(debug_image, (x1, y1), (x2, y2), (255, 255, 0), 2) # 바운딩 박스

            if play_effect_count == 0:
                playEffect()
                play_effect_count += 1
                tmp_class_id = class_id
            elif tmp_class_id != class_id:
                play_effect_count = 0
            # print(f"class_id: {class_id}")
            # print(f"tmp_class_id: {tmp_class_id}")
            # print(f"play_effect_count: {play_effect_count}")
            break

        # 종료 버튼(ESC) #################################################

        key = cv.waitKey(1)
        if key == 27:  # ESC
            break

        # FPS 조정 #############################################################
        elapsed_time = time.time() - start_time # 경과 시간
        sleep_time = max(0, ((1.0 / fps) - elapsed_time)) # 프레임 조정을 위해
        time.sleep(sleep_time)

        cv.putText(
            debug_image,
            "Elapsed Time:" + '{:.1f}'.format(elapsed_time * 1000) + "ms",
            (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv.LINE_AA)

        # 출력 #############################################################
        cv.imshow('NARUTO HandSignDetection Simple Demo', debug_image)

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
