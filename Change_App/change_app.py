def change_money(amount, stock):
    # 1. รับจำนวนเงินที่ต้องทอน → amount (รับจาก parameter)

    # 2. ตรวจสอบว่าจำนวนเงินรวมในสต็อกเพียงพอหรือไม่
    total_stock_value = 0
    for denom, qty in stock.items():
        total_stock_value += denom * qty

    if amount > total_stock_value:
        return "ไม่สามารถทอนได้: จำนวนเงินที่ต้องทอนมากกว่าเงินรวมในสต็อก"

    original_amount = amount
    result = {}

    # 3–5. วนหาชนิดเงินที่มากที่สุดที่สามารถทอนได้
    while amount > 0:

        used = False  # ตรวจว่ารอบนี้ใช้เงินได้หรือไม่

        # เรียงชนิดเงินจากมากไปน้อย
        sorted_denoms = sorted(stock.keys(), reverse=True)

        for denom in sorted_denoms:

            # ข้ามถ้ามูลค่ามากกว่าเงินที่ต้องทอน
            if denom > amount:
                continue

            # ข้ามถ้าไม่มีสต็อก
            if stock[denom] <= 0:
                continue

            # หาเงินชนิดนี้ที่สามารถใช้ได้มากที่สุด
            max_use_by_amount = amount // denom
            max_can_use = max_use_by_amount

            if max_can_use > stock[denom]:
                max_can_use = stock[denom]

            # ถ้าใช้ไม่ได้เลยก็ข้ามชนิดนี้
            if max_can_use <= 0:
                continue

            # ใช้เงินชนิดนั้น
            amount -= denom * max_can_use
            stock[denom] -= max_can_use

            if denom not in result:
                result[denom] = 0
            result[denom] += max_can_use

            used = True

        # ถ้าไม่มีชนิดเงินที่สามารถใช้ได้ในรอบนี้ → ตัน → ทอนไม่ได้
        if not used:
            return "ไม่สามารถทอนเงินได้: ค้างอยู่ " + str(amount) + " บาท"

    # 6. ถ้าเงินที่ต้องทอนเหลือ 0 แสดงว่าทอนสำเร็จ
    return {
        "status": "ทอนสำเร็จ",
        "ทอน": result,
        "จากยอด": original_amount
    }


# ตัวอย่างสต็อก
stock = {
    500: 1,
    100: 3,
    50: 2,
    20: 5,
    10: 10,
    5: 10,
    2: 10,
    1: 10
}

# ทดสอบฟังก์ชัน
print(change_money(786, stock.copy()))
