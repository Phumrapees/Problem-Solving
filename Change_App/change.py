# %%
import random

# %%
import random

cash_stock = {
    "500": [],
    "100": [],
    "50": [],
    "20": [],
    "10": [],
    "5": [],
    "2": [],
    "1": [],
}

for pointer in cash_stock:
    pointer_val = int(pointer)
    add_amount_remain = random.randint(0,5)
    cash_stock[pointer].append(add_amount_remain)
    cash_stock[pointer].append(pointer_val*add_amount_remain)
values_total = 0
for value in cash_stock:
    values_total += cash_stock[value][1]

for show in cash_stock:
    print(f"เงิน {show} บาท : จำนวนคงเหลือ {cash_stock[show][0]}")
#print(f"มูลค่ารวม {values_total} บาท")

# %%
status = True
while status:
    change = input("จำนวนเงินทอน 0 - 999 : ")
    if(change != ""):
        try:
            change = int(change)
        except ValueError:
            print("กรุณากรอกเงินทอนเป็นตัวเลข...")
            continue
        if change > 999:
            print("เงินทอนมีได้ไม่เกิน 999 บาท...")
            continue
        else:
            print(f"เงินทอน : {change}\nเงินคงเหลือ : {values_total}")

            def show_result():
                if change != 0:
                    print("จำนวนชนิดเงินไม่เพียงพอสำหรับทอนเงิน!!")
                else:
                    print(f"ทอนเงินเสร็จสิ้น {show_change} บาท ชนิดเงินที่ใช้ไปดังนี้ :")
                    for index, val in enumerate(cash_stock):
                        cash_stock[val][0] = cash_stock[val][0] - stock_used[index]
                        cash_stock[val][1] = int(val) * cash_stock[val][0]
                        print(f"{val} บาท จำนวนที่ใช้ไป {stock_used[index]} คงเหลือ {cash_stock[val][0]}")

            stock_used_val = 0
            show_change = change
            stock_used = []
            
            check_can_change = True
            for pointer in (cash_stock):
                if change > values_total:
                    print("เงินคงเหลือไม่เพียงพอ!!")
                    check_can_change = False
                    break
                else:
                    current_value = int(pointer)
                    current_amount = cash_stock[pointer][0]
                    use_item = change // current_value
                    if use_item > current_amount:
                        use_item = current_amount
                    stock_used.append(use_item)
                    change -= use_item*current_value
            if check_can_change:
                show_result()
    else:
        print("จบการทำงาน...")
        status = False



# %%



