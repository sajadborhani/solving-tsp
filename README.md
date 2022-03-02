https://www.ijeat.org/wp-content/uploads/papers/v4i6/F4173084615.pdf

linke to the article testing diffrent methodes for solving the tsp and proposing
the greedy algorithem


برای اجرای برنامه مراحل زیر را انجام دهید

1- اطمینان حاصل کنید که پکیج های مورد نیاز را نصب دارید در غیر اینصورت دستورات پایین را کپی کنید و در ترمینال وارد کنید
2- از طریق ترمینال وارد پوشه برنامه شوید. برای مثال:
 cd D:solve_tsp
3- دستور زیر را وارد کنید
python main.py


to run the program follow this steps:
1- make sure to install pakages befor running the code ( pip install matplotlib )
2- open directory on you'r terminal and run main.py with this command
    $python main.py


نصب پکیج های مورد نیاز:

pip install matplotlib

I used 2 diffrent method to solve this problem.now I represent a short description for each method in farsi
If you are intrested in more details search for each method and you will find plenty of data in any language you want

در این روش با توجه به اینکه نیاز به یک دور کامل داریم و الگوریتم موجود نقطه شروع اهمیتی ندارد
 الگوریتم جسورانه به شکل زیر عمل میکند:

 1- تمام مسیر های موجود را از کوتاه ترین به بلند ترین مسیر مرتب میکند
 2-کوتاه ترین مسیر موجود را انتخاب میکند، در صورتی که این مسیر با دو شرط مورد قبول است :
 شرط اول:
 اگر با اضافه شدن این مسِیر، بیشتر از دو مسیر به یک ایستگاه متصل نشود
( اگر  باعث رد شدن دوباره از یک ایستگاه نشود)
 شرط دوم:
 3- اگر با اضافه شدن این مسیر از تمامی ایستگاه ها عبور کرده باشیم الگوریتم به پایان میرسد و در غیر این صورت مرحله 2 مجددا تکرار میشود

 این روش برای شروع 
1-از نقطه ی شروع یا همان انبار شروع میکند 
2- و پس از آن مسیر متصل به نزدیک ترین ایستگاه را انتخاب میکند
اگر قبلا از نزدیک ترین ایستگاه عبور کرده باشد این مسیر را رد کرد مسیر متصل به نزدیک ترین ایستگاه بعدی را انتخاب میکند
تا زمانی این کار را ادامه میدهد تا از تمامی ایستگاه ها عبور کند و پس از ان به ایستگاه اول باز میگردد