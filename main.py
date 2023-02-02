import os
import sys
from pydicom import dcmread
from pydicom.pixel_data_handlers import convert_color_space
import cv2


def main():
    # 作業ディレクトリを自身のファイルのディレクトリに変更
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    ds = dcmread("20220930104109/0000111122223333_20220930_103352_1.dcm")

    print(ds)
    print(ds.PatientID)
    print(ds.Laterality)
    print(ds.StudyDate)

    for x in ds.dir():
        print(x)

    bgr = convert_color_space(ds.pixel_array, "YBR_FULL", "RGB", per_frame=True)
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    cv2.imwrite("./example.png", rgb)
    return


if __name__ == '__main__':
    main()
