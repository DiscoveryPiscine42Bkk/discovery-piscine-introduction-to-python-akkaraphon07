
while True:
    user_input = input("พิมพ์ข้อความ(พิมพ์ STOP เพื่อหยุด): ")
    
    if user_input == "STOP":
        break 
    else:
        print(f"คุณพิมพ์ว่า: {user_input}")