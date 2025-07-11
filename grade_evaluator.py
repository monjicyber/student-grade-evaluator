mark1 = float(input("ارجوك معدل الماده الاولى: "))
mark2 = float(input("ارجوك معدل الدرجه الثانيه: "))
mark3 = float(input("ارجوك معدل الدرجه الثالثه: "))

average = (mark1 + mark2 + mark3) / 3
print("معدلك هو", round(average, 2))

if average >= 16:
    print("تقييمك جيد")
elif average >= 12:
    print("تقييمك مقبول")
elif average >= 10:
    print("تقييمك متوسط")
else:
    print("تقييمك ضعيف")
