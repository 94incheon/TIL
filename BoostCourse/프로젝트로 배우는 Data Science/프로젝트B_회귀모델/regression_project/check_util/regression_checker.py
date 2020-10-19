import pandas as pd
import numpy as np
from pathlib import Path
import os
import zipfile
import platform


file_path = "submit/regression_submission.csv"

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
        print("셀프리뷰 파일이 로드되지 않았습니다. 셀프리뷰 파일의 경로를 확인해 주세요.")
        return False


def save_result(i):
    try:
        if i >= 1 and i < 7:
            submit = load_submit_file()
            submit.loc[i, "flag"] = True
            submit.to_csv(file_path)
    except:
        return False


def check_estimator(estimators):
    try:
        estimator_names = []
        for estimator in estimators:
            estimator_names.append(estimator.__class__.__name__)

        check_names = ['DecisionTreeRegressor',
                       'RandomForestRegressor',
                       'GradientBoostingRegressor']

        diff = set(check_names) - set(estimator_names)
        if len(diff) > 0:
            print(f"{diff} 모델을 estimators에 추가로 정의해 주세요.")
            return
        else:
            print("모델을 잘 정의해 주셨습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(1)
            return
    except:
         print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')


def check_max_depth(param_distributions):
    try:
        max_depth_list = param_distributions["max_depth"]
        max_depth_list_len = len(max_depth_list)
        max_depth_type = max_depth_list.dtype
        if max_depth_list_len != 10:
            print("max_depth의 원소 10개가 되도록 구현해 주세요.")
            return
        elif max_depth_type != np.int:
            print("max_depth는 트리의 깊이로 int 형식으로 구현해 주세요.")
            return
        else:
            print("max_depth를 잘 구현해 주셨습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(2)
    except:
         print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')


def check_max_features(param_distributions):
    try:
        max_features_list = param_distributions["max_features"]
        max_features_list_len = len(max_features_list)
        max_features_type = max_features_list.dtype
        if max_features_list_len != 10:
            print("max_features의 원소 10개가 되게 구현해 주세요.")
            return
        elif max_features_type != np.float:
            print("max_features는 피처의 비율로 float 형식으로 구현해 주세요.")
            return

        else:
            print("max_features를 잘 구현해 주셨습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(3)
    except:
         print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')


def check_cv(regressor):
    try:
        n = 3
        if regressor.cv < n:
            print(f"cross validation 조각을 {n}개 이상으로 구현해 주세요.")
            return
        else:
            print("cross validation을 여러개의 조각으로 잘 나누어 주셨습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(4)
    except:
         print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')


def check_rmse(rmse):
    try:
        n = 5
        if rmse < n:
            print("rmse 스코어가 기준점수보다 낮습니다. 이 값은 낮을 수록 오차가 작습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(5)
        else:
            print("rmse 스코어가 기준점수보다 높습니다. 이 값은 낮을 수록 오차가 작습니다. 다시 검토하시기 바랍니다.")
            return
    except:
         print('체크 함수를 실행하는 도중에 문제가 발생했습니다. 코드 구현을 완료했는지 다시 검토하시기 바랍니다.')


def check_r2_score(r2):
    try:
        if r2 > 0.7:
            print("r2 스코어가 기준점수 보다 높습니다. 이 값은 1에 가까울수록 오차가 작습니다. 이어서 진행하셔도 좋습니다.")
            return save_result(6)
        else:
            print("r2 스코어가 기준점수 보다 낮습니다. 이 값은 1에 가까울수록 오차가 작습니다.다시 검토하시기 바랍니다.")
            return
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
