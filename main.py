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
   
    try:
        # إدخال أسماء المستخدم مفصولة بفواصل وتحويلها لقائمة
        names_input = input("Enter names (comma separated): ").split(",")  

        # إدخال أرقام المستخدم مفصولة بفواصل وتحويلها لقائمة
        numbers_input = input("Enter numbers (comma separated): ").split(",")  

        # تنظيف أسماء المستخدم: إزالة المسافات الزائدة والتحقق أن كل اسم يحتوي على حروف فقط
        names = [n.strip() for n in names_input if n.strip().isalpha()]  

        # تنظيف أرقام المستخدم: إزالة المسافات الزائدة والتحقق أن كل رقم يحتوي على أرقام فقط
        numbers = [num.strip() for num in numbers_input if num.strip().isdigit()]  

        # التحقق من أن هناك أسماء وأرقام صالحة
        if not names or not numbers:  
            raise Exception("you entered wrong input")  # إذا أي قائمة فارغة → رسالة خطأ

        # دالة للتحقق من أن النص أو الرقم ليس ضعيفًا
        # تعتبر ضعيفة إذا كل الحروف أو الأرقام مكررة (مثال: aaaaa أو 11111)
        def is_weak(word):
            return all(c == word[0] for c in word)  # True إذا كل الحروف/الأرقام نفسها

        wordlist = set()  # استخدام set لتخزين النتائج وإزالة أي تكرار تلقائي

        # دمج كل اسم مع كل رقم
        for name in names:  
            if is_weak(name):  # إذا الاسم ضعيف جدًا
                print(f'The name "{name}" is too weak')  # رسالة للمستخدم
                continue  # تجاهل الاسم الضعيف والانتقال للاسم التالي

            for num in numbers:  
                if is_weak(num):  # إذا الرقم ضعيف جدًا
                    print(f'The number "{num}" is too weak')  # رسالة للمستخدم
                    continue  # تجاهل الرقم الضعيف

                # إنشاء جميع التركيبات الممكنة بين الاسم والرقم
                variants = [
                    name + num,           # الاسم أولاً ثم الرقم
                    name.lower() + num,   # الاسم بحروف صغيرة + الرقم
                    name.capitalize() + num, # أول حرف كبير + الرقم
                    num + name,           # الرقم أولاً ثم الاسم
                    num + name.lower()    # الرقم + الاسم بحروف صغيرة
                ]

                # إضافة كل كلمة إلى set → أي تكرار يُلغى تلقائيًا
                for w in variants:
                    wordlist.add(w)

        # طباعة عدد الكلمات الناتجة
        print(f"\nGenerated {len(wordlist)} unique words:")  

        # طباعة كل كلمة في سطر مستقل (مرتبة)
        for r in sorted(wordlist):
            print(r)  

        # إعادة القائمة لاستخدامها في أجزاء أخرى من المشروع
        return wordlist  

    except Exception:  
        # إذا كان الإدخال فارغ أو غير صالح، تظهر هذه الرسالة
        print("you entered wrong input")  


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
