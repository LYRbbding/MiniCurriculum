from data import campus_items_list,building_items_list,classroom_items_list,course_items_list,week_items_list,date_items_list,section_items_list,classTable,date_count,section_count
import mysql.connector
conn = mysql.connector.connect(user='Huang', password='password', database='schooltimetable')
cursor = conn.cursor()

def get_query_str(w_s=0,w_e=15,d_s=0,d_e=4,s_s=0,s_e=13,classroom=".",course="."):
    week = "((,|^)" + str(w_s+1) + "(,|周))"
    date = str(date_items_list[d_s])
    section = str(section_items_list[s_s])
    for i in range(w_s+2,w_e+2):
        week = week + "|((,|^)" + str(i) + "(,|周))"
    for i in range(d_s+1,d_e+1):
        date = date + "|" + str(date_items_list[i])
    for i in range(s_s+1,s_e+1):
        section = section + "|" + str(section_items_list[i])
    t = (week,date,section,classroom,course)
    return t

week_start=0
week_end=6
date_start=0
date_end=2
section_start=0
section_end=9
classroom="主-421"
course='.'

query_str = get_query_str(week_start,week_end,date_start,date_end,section_start,section_end,classroom,course)
cursor.execute('select * from schedule where 上课周次 regexp %s and 星期 regexp %s and 节次 regexp %s and 教室 regexp %s and 课程名称 regexp %s order by 课程名称', query_str)
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
#('周三','教三楼','3-211','(,|^)16(,|周)',校区，教学楼，教室，上课周次*，星期*，节次*，课程名称，授课教师，上课班级)
