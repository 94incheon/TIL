import pandas as pd
from pathlib import Path
import os
import zipfile
import platform


file_path = "submit/classification_submission.csv"

def check_load_self_review():
    return reset_result()


def load_submit_file():
    submit = pd.read_csv(file_path, index_col="todo")
    return submit


def reset_result():
    try:
        submit = load_submit_file()
        submit.flag = False
        submit.to_csv(file_path)
        print("셀프리뷰 파일이 정상로드 되었습니다. 이어서 진행하셔도 좋습니다.")
        return submit
    except:
        return False


def save_result(i):
    try:
        if i >= 1 and i < 7:
            submit = load_submit_file()
            submit.loc[i, "flag"] = True
            submit.to_csv(file_path)
    except:
        return False


def check_null_up(df):
    try:
        null_val = df["요단백"].isnull().sum()
        if null_val == 0:
            print("요단백의 결측치를 잘 채워주셨습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(1)
        else:
            print("요단백의 결측치를 채워주세요.")
    except:
        print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')


def check_ldl_median(df):
    try:
        ldl_val = df["LDL콜레스테롤"].isnull().sum()
        if ldl_val == 0:
            print("LDL콜레스테롤의 결측치를 잘 채워주셨습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(2)
        else:
            print("LDL콜레스테롤의 결측치를 채워주세요.")
    except:
        print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')



def check_null(df):
    try:
        null_count = df.isnull().sum().sum()
        if null_count == 0:
            print("결측치를 잘 채워주셨습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(3)
        else:
            print("결측치를 채워주세요.")
    except:
        print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')


def check_split_dataset(train, test):
    try:
        if train is None and test is None :
            return False

        if train.shape[0] == 8000 and test.shape[0] == 2000:
            print("train, test 데이터셋을 잘 나누어 주셨습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(4)
        else:
            print("train, test 만개의 데이터셋을 8:2 의 비율로 나눠주세요.")
    except:
        print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')


def valid_model(model):
    try:
        if model.__class__.__name__ == "RandomForestClassifier":
            print("랜덤포레스트 분류기를 잘 설정해 주셨습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(5)
        else:
            print("랜덤포레스트 분류기를 설정해 주세요.")
    except:
         print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')


def check_score(score):
    try:
        if score > 72.0:
            print('모델 성능이 기준치를 넘었습니다! 이어서 진행하셔도 좋습니다.')
            return save_result(6)
        else:
            print("Test Accuracy가 낮습니다. Model의 구조와 Data Input, Output을 확인해주세요.")
    except:
        print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')



def check_submit():
    submit = pd.read_csv(file_path, index_col="todo")
    not_valid = submit[submit.flag == False]
    check_count = not_valid.shape[0]
    if check_count > 0:
        print("[ Self-Check ] 평가기준을 통과하지 못했습니다. 다음 항목을 참고하세요!")
        return not_valid
    else:
        return make_submission()


def make_submission():
    try:
        plat_system = platform.system()
        project_path = Path().cwd().absolute()
        file_name = str(list(project_path.glob("*-project*.ipynb"))[0].relative_to(project_path))
        submit_file = project_path / file_name
        output_path = project_path / "submit"

        sub_string = f"jupyter nbconvert {str(submit_file)} --to html --output {file_name.split('-')[1]}_submission --output-dir={output_path}"
        os.system(sub_string)
        print(f"[ Self-Check ] Submit 파일 생성완료! 위치: '{(output_path).relative_to(project_path)}'")

        if not output_path.exists():
            output_path.mkdir()

        print(f"[ Self-Check ] 시스템: {plat_system}")

        # zip files
        files = list(output_path.glob("*submission.*"))

        with zipfile.ZipFile("submit.zip", "w") as zip_handle:
            for f in files:
                zip_handle.write(str(f.relative_to(project_path)))
        print("[ Self-Check ] submit.zip 생성 완료!")
        print("[ Self-Check ] 모든 평가기준을 통과했습니다. 압축파일을 제출해주세요!")
    except:
        print("[ Self-Check ] 제출 파일이 생성되지 않습니다. 다시 시도해보세요!")
