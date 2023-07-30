from yolox.yolox_onnx import YoloxONNX
import cv2 as cv
import time
import csv
import copy

def main():
    # 변수 설정 #################################################################
    model_path = "yolox/yolox_nano.onnx"
    input_shape = (416,416)
    score_th = 0.75
    nms_th = 0.45
    nms_score_th = 0.1
    with_p6 = False

    # 이미지 불러오기 ###############################################################

    img = cv.imread('testImg.png')

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

    yolox.test()

    # label 설정 ###########################################################
    with open('../setting/labels.csv', encoding='utf8') as f:
        labels = csv.reader(f)
        labels = [row for row in labels]

    debug_image = copy.deepcopy(img)

    bboxes, scores, class_ids = yolox.inference(img)

    for bbox, score, class_id in zip(bboxes, scores, class_ids):
        # 반복문을 통해 가장 높은 점수의 클래스 찾기
        class_id = int(class_id) + 1
        if score < score_th:  # score_th보다 높다면 바운딩 박스 그리기
            continue

        # 바운딩 박스 그리기 ###################################################
        x1, y1 = int(bbox[0]), int(bbox[1])
        x2, y2 = int(bbox[2]), int(bbox[3])

        cv.putText(
            debug_image, 'ID:' + str(class_id) + ' ' +
                         labels[class_id][0] + ' ' + '{:.3f}'.format(score),
            (x1, y1 - 15), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2,
            cv.LINE_AA)  # 예측한 클래스 바운딩 박스 위에 그리기
        cv.rectangle(debug_image, (x1, y1), (x2, y2), (255, 255, 0), 2)  # 바운딩 박스
        break

    cv.imshow('NARUTO HandSignDetection Simple Demo', debug_image)
    cv.waitKey(0)


if __name__ == '__main__':
    main()