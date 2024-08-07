import os
import csv
from configs.load_config import LoadConfig

APP_CFG = LoadConfig()

def csv2txt(csv_link):
    data_text = ''
    with open(csv_link, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Lấy thông tin từ mỗi hàng của file CSV
            MAJORS_CODE = row['ma_nganh']  # Thay 'Code' bằng tên cột chứa mã code sản phẩm trong file CSV của bạn
            MAJORS_NAME = row['Nganh']  # Thay 'Tên Sản Phẩm' bằng tên cột chứa tên sản phẩm trong file CSV của bạn
            MAJORS_COMBINATION = row['to_hop']  # Thay 'ID' bằng tên cột chứa ID sản phẩm trong file CSV của bạn
            MAJORS_POINT = row['diem']  # Thay 'Code' bằng tên cột chứa mã code sản phẩm trong file CSV của bạn
            MAJORS_TIME = row['thoi_gian_dao_tao']
            MAJORS_PRICE = row['hoc_phi']
            GRADUATE_SALARY = row['luong_ra_truong']
            INTRODUCT = row['gioi_thieu']
            JOB_OPPORTUNITIES = row['co_hoi_viec_lam']
            POLICY = row['chinh_sach_ho_tro']
            SCHOLARSHIP = row['hoc_bong']
            # In ra văn bản theo định dạng mong muốn
            s = f"""Ngành: {MAJORS_NAME} : {INTRODUCT} \n
            Mã ngành là: {MAJORS_CODE} \n
            Tổ hợp môn xét tuyển là: {MAJORS_COMBINATION}, 
            Điểm chuẩn là: {MAJORS_POINT} \n
            Thời gian đào tạo:{MAJORS_TIME} \n 
            Học phí là: {MAJORS_PRICE} \n
            Học bổng là : {SCHOLARSHIP} \n 
            Chính sách hỗ trợ:{POLICY} \n 
            Cơ hội việc làm:{JOB_OPPORTUNITIES} \n
            Lương sau khi ra trường:{GRADUATE_SALARY}\n"""
            data_text = data_text + s
            # print(s)
    return data_text


def convert_csv_to_txt():
    directory_txt = APP_CFG.text_product_directory
    directory_csv = APP_CFG.csv_product_directory

    files = [f for f in os.listdir(directory_csv) if os.path.isfile(os.path.join(directory_csv, f))]
    csv_files = [f for f in files if f.endswith('.csv')]

    for csv_file in csv_files:
        # Đọc file CSV
        csv_path = os.path.join(directory_csv, csv_file)
        txt_file = csv_file.replace('.csv', '.txt')
        txt_path = os.path.join(directory_txt, txt_file)
        data_text = csv2txt(csv_path)
        with open(txt_path, "w", encoding='utf-8') as file:
            file.write(data_text)