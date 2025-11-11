import os # os指的是內建的module或package
import random
import csv


def get_names(file_name): # 自訂get_names函式，參數file_name是檔案名稱
    current_dir = os.path.dirname(os.path.abspath("__file__"))
    file_path = os.path.join(current_dir,'assets',file_name) 
    
    with open(file_path, encoding="utf-8") as file:
        content = file.read()

    return content.split('\n') #return回傳以換行符號分隔的列表

def get_scores(names, num=10):
    stu_names = random.sample(names,num)
    scores = []
    for name in stu_names:
        info = {"姓名":name,
                "國文":random.randint(50, 100),
                "英文":random.randint(50, 100),
                "數學":random.randint(50, 100)
                }
        scores.append(info)
    return scores

def save_csv(students,filename):
    fieldnames = students[0].keys()
    current_dir = os.path.dirname(os.path.abspath("__file__"))
    file_path = os.path.join(current_dir,'assets',filename)

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for d in students:
            writer.writerow(d)

names = get_names("names.txt")
num = int(input("請輸入學生數量:")) #請使用者輸入學生數量
students = get_scores(names,num=num) 
# 呼叫get_scores函式並傳入參數 第一個num是指使用者輸入的數字 第二個num指是get_scores(names, num=10)數量

save_csv(students,'students.csv')