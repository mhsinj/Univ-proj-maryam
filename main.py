import itertools
import math
#test for commit
#main file of project
######################
#Part number one for moneer - banner and inputs to ask user what type of list number,numbers with letters , num,letters, special characters 




##################################
#part number 2 for yousef - function if it  is just numbers








######################################
#Part 3 for najeeb-  function of numbers with letters
def letters_with_numbers():  
    # تعريف دالة وظيفتها توليد كلمات من حروف و ارقام

    names = input("Enter names (comma separated): ").split(",")
    # يطلب من المستخدم إدخال أسماء مفصولة بفاصلة
    # عشان نقدر نتعامل مع كل مدخل على حدىsplit(",") يحول الإدخال من نص إلى قائمة أسماء

    numbers = input("Enter numbers/years (comma separated): ").split(",")
    # يطلب من المستخدم إدخال أرقام أو سنوات مفصولة بفاصلة
    # ويتم تحويلها إلى قائمة

    names = [n.strip() for n in names if n.strip()]
    # يمر على كل اسم في القائمة
    # strip() يحذف المسافات الزائدة
    # if n.strip() يتجاهل القيم الفارغة

    numbers = [num.strip() for num in numbers if num.strip()]
    # يمر على كل اسم في القائمة
    # strip() يحذف المسافات الزائدة
    # if num.strip() يتجاهل القيم الفارغة

    result = []
    # إنشاء قائمة فارغة لتخزين جميع النتائج

    for name in names:
        # حلقة تمر على كل اسم في قائمة الأسماء

        for num in numbers:
            # حلقة داخلية تمر على كل رقم
            # يتم دمج كل اسم مع كل رقم

            result.append(name + num)
            # إضافة الاسم مع الرقم (مثال: Ahmed2001)

            result.append(name.lower() + num)
            # إضافة الاسم بحروف صغيرة مع الرقم (ahmed2001)

            result.append(name.capitalize() + num)
            # إضافة الاسم مع أول حرف كبير (Ahmed2001)

            result.append(num + name)
            # إضافة الرقم ثم الاسم (2001Ahmed)

            result.append(num + name.lower())
            # إضافة الرقم ثم الاسم بحروف صغيرة (2001ahmed)

    print("\nGenerated combinations:")
    # طباعة عنوان قبل عرض النتائج

    for r in result:
        # حلقة تمر على كل كلمة تم توليدها

        print(r)
        # طباعة كل كلمة

    return result
    # إرجاع القائمة لاستخدامها في أجزاء أخرى من المشروع


######################################
#Part 4 (me)- function of numbers with letters with special characters 







######################################
#Part 5 for haroon- function to save the output to file 









######################################
#Part 6 (me)- Create Random listwith letters numbers and special characters #











#########################################
#part 7 (me)- feauter of pdf
def mix():
    names = input("Enter names => ").split(",")
    years = input("Enter years => ").split(",")

    names = [n.strip().lower() for n in names if n.strip()]
    years = [y.strip() for y in years if y.strip()]
    symbols = [ "_", "", "@"]
    templates = [
        "{name}{year}",
        "{name}_{year}",
        "{name}{symbol}{year}"
    ]

    leet = {
        "a": ["a", "@"],
        "e": ["e", "3"],
        "i": ["i", "1"],
        "o": ["o", "0"],
        "s": ["s", "$"],
    }

    max_words = 10000
    max_length = 14
    min_entropy = 2.5


######################################
#Part 8-  Main function  

def main():
    print("main function...")


main()
