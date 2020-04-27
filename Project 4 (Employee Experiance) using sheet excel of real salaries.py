'''بسم الله الرحمن الرحيم'''               

                            #Project 4 (Employee Experiance) using sheet excel of real salaries
#import liberaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#export sheet excel by command for example(df = pd.csv (r'Path where the Excel file is stored\File name.csv') #for an earlier version of Excel, you may need to use the file extension of 'xls')
data=pd.read_csv(r"F:\deploma\PYTHON\sample sheets\Salary_Data.csv")
#تم الان عملية الimport لشيت الإكسيل
#الشيت بالنسبة ليا جاهز (لانة مكون من 2 عمود وفقط وصفوف)فمش محتاج اعمل علية تعديل..لو محتاج اعمل علية تعديل كنت هشتغل بال (i.lock) او بال (.drop)
#دلوقتى انا محتاج احدد عمود يكون هوة الinput بتاعى وعمود يكون هوة الoutput بتاعى 
#دلوقتى انا هحدد ان الinput بتاعى هيكون عمود رقم 1 (لانة المرتبات) والoutput هيكون عمود رقم 0 (عدد سنوات الخبرة) 
#أما اذا كان index الاعمدة او الصفوف (مسميات) فكتب المسمى للتخزين داخل X OR Y كالاتى
#دلوقتى انا هرمز للinput ب الX
X=data["YearsExperience"]
#ودلوقتى انا هرمز للoutput بالY
Y=data["Salary"]
#to import specific multiple columns & Rows in new variables
#دلوقتى انا محتاج اعمل import لمكتبة الskilearn عشان استعمل منها functions معينة
#ولكن لن اعمل لها import لانها كبيرة جدا..إية الحل؟
import sklearn
#الحل: إنى اعمل import للfunctions اللى انا عايزها بس منهامثل الfunction(train&test&split)2..كالاتى: 
#ماهى الfunction of "train_test_split؟ 
#هي function يتم بيها عمل الخط الخاص بالlinear regression
#معنى الكلام دة:انا عندى عمود مسمية X وعندى عمود تانى مسمية Y
#عايز اخد محموعد من الdata من الA واعمل بيها تيست معين-هجرب بشكل عشوائي مثلا عشات اطلع معادلة تنبوء predictation (ولكن هحافظ على باقى البيانات عشان اجري عليها الاختبار بعد ماتاكد من ان المعادلة للتبوء مظبوطة)
#البيانات اللى اخدناها عشان نجري عليها الاختبار بنسميها test
#باقى البيانات اللى (بعد ماتاكد من اختبارى فى التنبوء) شايلها على جمب بنسميها train
#بالنسبة لعملية الsplit فهى بتفصل البيانات بين عملية الtrain و الtest
from sklearn.model_selection import train_test_split
x=np.array(X).reshape(-1,1)
y=np.array(Y).reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#دلوقتى خلاص تم تجهيز الداتا واصبح عندى A & C جاهزين لانى اعمل عليهم عمليات الlinear regression (وهو عمل خط عشوائي بين البيانات ثم عمل عملية التعديل على الخط العشوائي ليكون فى المكان الافضل لتمثيل الداتا)
#ولعمل هذة العميلة محتاج اعمل استدعاء لfunction من داخل مكتبة الskilearn
from sklearn.linear_model import LinearRegression
#دلوقتى محتاج اعمل object عشان اشتغل علية فى الLinearRegression عشان اعمل تحليل للبيانات
reg=LinearRegression()
#دلوقتى هنستدعى function بتساعد فى عملية تحليل البيانات حيث تقوم بعملية التدريب
#وهنعمل على الinput-X اللى هيا الداتا اللى هيتعلم عليها والoutput-Y الل هيا النتيجة اللى هيتعلم عليها
reg.fit(x_train,y_train)
#دى مرتابت لمجموعة من الاشخاص اللى اخذتهم random من الشيت الاساسى عشان اعمل عليهم تيست(بس دول انا مخبيهم عن الكومبيلر عشان اشوف نتيجة توقثعاتة هتطلع زي ماهى مرتباتهم الفعلية ولا لأ)
print(y_test)
#ودلوقتى دى خبرات نفس الاشخاص اللى فى Y_test
print(x_test)
#انا هديلة خبرات الناس فى اللى في x_test وهقولة بالمعادلة اللى عملتها توقعلى مرتباتهم وهبدا اقارن المرتبات اللى طلهم فى cpred هل هيا قريبة من المرتبات اللى كنت مخبايها فى  Y_test 
#وبكدة هيككون هوة رسم خط linear regression عشوائى وفى الغالب بيكون بعيد عن التوقعات المظبوطة اللى انا عايزها
ypred=reg.predict(x_test)
print(ypred)
#دلوقتى عايزين نشوف برسم بيانى اية اللى حصل..فهنكتب function يطلع ليا نقاط تمثل الsalary على محور الx ونقاط تمثل الYearsExperiance على محور الy 
plt.scatter(x,y)
#وبعدين هطلب منة يرسم ليا خط الlinear regression اللى هوة رسمة على نقاط كنوع التنبوء
#فال x تمثل النقاط على محور x و y وهى التقاء الsalary with YearsExperiance و (reg.predict(x)q) لتمثيل خط التنبوء على النقاط 
plt.plot(x,reg.predict(x))
plt.show()