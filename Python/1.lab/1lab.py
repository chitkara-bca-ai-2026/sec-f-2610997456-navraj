tuition_fee = float(input("enter tuition fee: "))
lab_fee = float(input("enter lab fee: "))
library_fee = float(input("enter library fee: "))
exam_fee = float(input("enter exam fee: "))
discount_amount = float(input("enter discounted amount: "))

total_before_discount = tuition_fee + lab_fee + library_fee + exam_fee

total_after_discount = total_before_discount - discount_amount

anual_fee = total_after_discount * 2
monthly_instalment = anual_fee / 12

print("tuition fee: {tuition_fee}\nlab fee: {lab_fee}\nlibrary fee: {library_fee}\nexam fee: {exam_fee}\ntotal fee: {total_before_discount}\ndiscount: {discount_amount}\nFee after Discount: {Total_after_discount}\nAnnual Fee: {Anual_fee}\nMonthly Installment: {Monthly_instalment}")
