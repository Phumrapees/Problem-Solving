#เมื่อรันเสร็จจะมีไฟล์ calculator เกิดขึ้นมา
import streamlit as st

def get_number_input(label):
    return st.number_input(label, value=0.0, step=0.1, format="%.2f")

def get_operator_input(label):
    valid_operators = ['+', '-', '*', '/', '%']
    return st.selectbox(label, valid_operators)

def calculate(num1, num2, operator):
    #copy โค้ดฟังก์ชั่น calculate มาใส่
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/" | "%":
            if num2 == 0:
                st.error("Can't Divde by ZERO!!")
                return None
            else:
                result = eval(str(num1)+operator+str(num2))
            
        #case "%":
         #   result = num1 % num2
    return result








st.title('My Calculator')

# Get inputs from the user
num1 = get_number_input("ป้อนตัวเลขแรก:")
num2 = get_number_input("ป้อนตัวเลขที่สอง:")
operator = get_operator_input("เลือกตัวดำเนินการ:")

# Perform calculation when the button is clicked
if st.button('คำนวณ'):
    result = calculate(num1, num2, operator)
    if result is not None:
        st.success(f"ผลลัพธ์: {num1:.3f} {operator} {num2:.3f} = {result:.3f}")
