import tkinter as tk
from tkinter import ttk

def Click_here():
    global extra_window
    extra_window = tk.Toplevel()
    ttk.Label(extra_window, text="The built in functions").grid()
    extra_window.geometry("600x600")
    ttk.Label(extra_window,text='''
    1. Python abs():
           return absolute value of a number    
    2. Python all():
        return true when all element in iterable is true
    3. Python any():
        check if any element of an iterable is true 
    4. Python ascii():
        return string containing printable representation 
    5. Python bin():
        convert integer to binary string 
    6. Python bool():
         convert a value to a boolean 
    7. Python bytearray():
         return array of given byte size
    8. Python bytes():
         return immutable bytes object 
    9. Python callable():
         check if the object is callable
    10. Python chr():
           returns a character(a string) from an integer
    11. Python classmethod():
            return class method for given function
    12. Python compile():
           return a python code object
    13. Python complex():
           creates a complex number
    14. Python delattr():
           Delete attribute from the object
    15. Python dict():
            creates a dictionary 
    16. Python dir():
            tries to return attribute of object
   ''',font=("Andalus",10)).grid(row=0,column=0)

    ttk.Label(extra_window, text='''
     17. Python divmod():
            returns a tuple of Quotient
    18. Python enumerate():
            Return an enumerate object
    19. Python eval():
            runs Python code within program 
    20. Python exec():
           executes dynamically created program
    21. python filter():
           constructs iterator from elements which are true
    22. python float():
            return floating point number string
    23. python format():
            return formatted representation of a value
    24. python frozenset():
            return immutable frozenset object
    25. python getattr():
            return value of named attribute of an object
    26. python globals():
            return dictionary of current global symbol table
    27. python hasattr():
            return whether object has named attribute 
    28. python hash():
            return hash value of an object 
    29. python help():
            invokes the built in help system 
    30. python hex():
            converts to integer to hexadecimal
    31. python id():
            returns identify of an object 
    32. python input():
            reads and returns a line of a string 
    ''',font=("Andalus",10)).grid(row=0,column=3)

    ttk.Label(extra_window,text='''
    33. python int():
            returns integer from a number or a string 
    34. python isinstance():
            check if an object is an instance od class
    35. python iter():
            returns an iterator
    36. python len():
            returns length of an object 
    37.python list():
            creates a list in python 
    38. python locals():
            returns dictionary of a current local symbol table
    39.python map():
           applies function and returns a list 
    40. python max():
           return a largest Item
    41. python memoryview():
           returns memory view of an argument
    42. python min():
           return the smallest value
    43. python next():
           retrieves next item from the iterator
    44. python object():
           creates a featureless object
    45. python oct():
           return the octal representation of an integer
    46. python open():
           returns a file object 
    47. python ord():
           returns an integer of the unicode character
    48. python pow():
           returns the powers of a number
    ''',font=("Andalus",10)).grid(row=0,column=6)

    ttk.Label(extra_window,text=''' 
     49. python print():
           prints the given object
    50. python property():
           return the property attribute 
    51. python range():
           return a sequence of integer 
    52. python repr():
           returns a printable representation of the object 
    53. python reversed():
           returns the reversed iterator of a sequence
    54. python round():
           rounds a number to specified decimal
    55. python set():
           constructs and returns a set 
    56. python setattr():
           sets the value of an attribute of an object
    57. python slice():
           returns a slice object
    58. python sorted():
           returns a sorted list from the given iterator
    59. python staticmethod():
           transforms a method into a staticmethod 
    60. python str():
           returns the string version of the object
    61. python sum():
           adds item of an iterable
    62. python super():
           returns a proxy object of the base class 
    63. python tuple():
           returns a tuple
    64. python type():
           returns the type of the object 
    ''',font=("Andalus",10)).grid(row=0,column=9)

    ttk.Label(extra_window,text='''
    65. python vars():
           returns the __dict__ attribute
     66. python zip():
           returns an iterator of tuples 
    67. python __import__():
           function called by the import statement
    65. python vars():
           returns the __dict__ attribute
    66. python zip():
           returns an iterator of tuples 
    67. python __import__():
           function called by the import statement''',font=("Andalus",10)).grid(row=0,column=10)
def enter_here():
    extra_window = tk.Toplevel()
    ttk.Label(extra_window,text="fibonacci numbers",foreground="red",font=("Constantia",36)).pack()
    extra_window.geometry("600x500")
    ttk.Label(extra_window,text='''def fibonacci(num):
                       if num == 1:
                           return 1
                       if num == 0:
                           return 0
                       else:
                           return fibonacci(num-1) + fibonacci(num-2)
                    
                    for i in range(1,8):
                        print(fibonacci(i)''',font=("Andalus",30),foreground="black",background="gray").pack(expand=True)
def press_here():
    extra_window = tk.Toplevel()
    ttk.Label(extra_window, text="Information about the GUI application in Python").pack()
    extra_window.geometry("600x500")
    ttk.Label(extra_window, text='''
                                            GUI ?
     رابطه گرافیکی پایتون(GUI) یک رابطه کاربری است که بر اساس اجزای گرافیکی مانند  دکمه ها فرم ها منو ها
      و سایر اشیا ها طراحی شده اند تا با استفاده از آن کاربر بتواند با برنامه و سیستم ها تعامل کنند.  
                              1- رابطه گرافیکی Tkinter:
     یک رابطه گرافیکی پایتون است که برای ایجاد رابطه گرافیکی ساده بکار میرود این پکیج بر پایه کتابخانه های TCl و  Tkinter ساخته شده است و به عنوان یکی از ابزار های پر کاربرد یرای ساخت رابطه های
                             کاربری GUI در Python شناخته می شود.
                            
                               مهم ترین ویژگی های TKinter عبارتند از:
     سادگی tkintrer: بسیار ساده برای استفاده است و به کاربران امکان می دهد به راحتی رابط های گرافیکی ساده و حتی پیچیده تر را ایجاد کنند.
      قابلیت انتقال به سیستم عامل ها مانند‍؛windows,macos, linux هستند؛ بدون نیاز به تغییر کود منبع.
      پیشتیبانی از ویجت های مختلف؛ویجت های مختلفی رااز جمله بنر,دکمه,برچسپ,ورودی متن,لیست باکس,وغیره...فراهم می کند
                    که امکان ایجاد رابط های گرافیکی متنوع راایجاد می کند.
      
                              2-رابط گرافیکی  PYQT
    یک رابط گرافیکی پایتون است و یک پیاده سازی است python از QT می باشد که برنامه نویسان را امکان می دهد رابط های گرافیکی پیچیده و حرفه ای را با استفاده از python ایجاد کنند.
    و QT یک فرم ورک قدرتمند توسعه رابط های کاربری است که توسط شرکت Digia توسعه یافته و حمایت می شود
    که کاملا به زبان برنامه python متصل است و امکانات گسترده را برای ایجاد برنامه های با
    رابط گراافیکی پیشرفته در اختیار برنامه نویسان قرار می دهد.     
                              ویژگی هایPYQT
    قابلیت چند پلتفرمی: بر روی انواع مختلفی از سیستم عامل ها از جمله MACOS,WINDOWS,LINUX, و حتی تلفن های همراه قابل استفاده است.
    تنوع ویجت هاPYQT: امکانات بسیار گسترده ای را برای ایجاد و سفارشی سازی ویجت ها(عناصر رابط کاربری مانند دکمه ها پنجره ها منوهاو...)
    فراهم می کند. این ویژگی امکان طراحی رابط های کاربری گوناگون و پیچیده را فراهم می آورد.
    پشتیبانی از زبان های متعدد: به طور رسمی از زبان python پشتیبانی می کند اما می توان از انواع دیگر زبان های برنامه نویسی مانند c++ نیز برای توسعه برنامه های pyqt استفاده کرد.
    پرفورمنس بالا: qt به عنوان یک فرم ورک پرفورمنس بالا شناخته می شود و PYQT نیز به از این قابلیت بهره می برد
    
                                   رابطه گرافیکی PYGTK:
    یک رابطه گرافیکی پایتون است و یک پیاده سازی PYTHON از کتابخانه GTK+ می باشد. +GTK یک کتابخانه معروف و قدرتمند برای توسعه برنامه های با رابط کاربری گرافیکی در محیط های مختلف مانند LINUX استفاده می شود
    و PYGTK با استفاده از ورژن های مختلف +GTK امکانات بسیاری را برای برنامه نویسان PYTHON فراهم می کند تا بتوانند برنامه هایی با را با رابط  کاربری گرافیکی  پویا و قابل تعامل ایجاد کنند.
                     امکانات و ویژگی های مهم PYGTK شامل موارد ذیل است:
    قابلیت چند پلتفرمی ,تنوع ویجت ها,تطابق با استندرد ها,پشتیبانی از زبانی PYHTON,مستندات کامل .
                                  رابط گرافیکی WXPYTHON
      یک رابط گرافیکی پایتون است یکی از پر قدرتمند ترین و کاربردترین کتابخانه های GUI برای زبان برنامه نویسی PYTHON است
      این کتابخانه براساس WXWIDGETS ساخته شده است که یک کتابخانه متن باز برای توسعه برنامه های چند پلتفرمی است.با WXPYTHON برنامه نویسان می توانند به راحتی 
      رابط های کاربری گرافیکی زیبا و قابل تعامل با برنامه های خود ایجاد کنند.
      همچنان WXPYTHON دارای مجموعه ای گسترده از ویجت ها و ابزار گرافیکی است که برنامه نویسان می توانند از آنها برای ساخت رابط های کاربری گوناگون و با استایل های 
      مختلف استفاده کنند.
      
      رابط گرافیکی KIVY 
     یک رابط گرافیکی پایتون است و یک چارچوب توسعه رابط های کاربری چند لسمی(MULTI TOUCH ) می باشد که به برنامه نویسان امکان می دهد برنامه هایی با رابط گرافیکی بصری و 
     جذاب را برای انواع مختلف دستگاه ها ایجاد کنند چارچوب KIVY از زبان برنامه نویسی پایتون استفاده می کنند
     و برنامه های از جمله برنامه های موبایل,برنامه های دیسک تاپ و حتی برنامه های بازی را می توانند ایجاد کنند
     ویژگی ها وامکانات مهم KIVY عبارتند از:
     قابلیت چند پلتفرمی , تعامل چند لمسی 
     پشتیبانی از زبان های دیگر: علاوه بر KIVY و PYTHON از زبان های دیگری مانند CYTHON و LUA نیز پشتیبانی می کند که به برنامه نویسان
      امکان می دهد که برنامه  های خود را با استفاده از این زبان ها توسعه دهند.
      و KIVY داری زبان MARKUP خود بنام KV است که به برنامه نویسان امکان می دهد رابط های کاربری را به صورت تصریحی و از طریق انتخاب خواث خواص و ویژگی ها را تعریف کنند
      این رویکرد از جدا کردن طراحی از کد برنامه, توسعه را سریعتر و مدیریت پذیر تر می کند.
''').pack(expand=True)


window = tk.Tk()
window.title("The all of home works ")
window.geometry("700x600")

button1 = ttk.Button(window, text="first home work", command=Click_here)
button1.pack(expand=True)

button2 = ttk.Button(window, text="Second home work", command=enter_here)
button2.pack(expand=True)

button3 = ttk.Button(window, text="third home work", command=press_here)
button3.pack(expand=True)
window.mainloop()
