#import turtle module
import turtle

#استدعا شاشة اللعبة
wind = turtle.Screen()
#داله احدد عنوان للشاشه
wind.title("Ping pong By affi")
#الان تعديل الالوان والطول والعرض
wind.bgcolor("black")
wind.setup(width=800,height=600)
#يمنع الشاشه من عمل تحديث
wind.tracer(0)

madrab1 = turtle.Turtle() #لرسم المضرب
madrab1.speed(0) #سرعة رسم المضرب
madrab1.shape("square") #تحديد شكل المضرب
madrab1.color("blue") #تحديد لون المضرب 
madrab1.penup() #تمنع ظهور الخطوط
madrab1.goto(-350,0)
madrab1.shapesize(stretch_wid=5,stretch_len=1) #تعديلات حجم المضرب

madrab2 = turtle.Turtle() #لرسم المضرب
madrab2.speed(0) #سرعة رسم المضرب
madrab2.shape("square") #تحديد شكل المضرب
madrab2.color("red") #تحديد لون المضرب 
madrab2.penup() #تمنع ظهور الخطوط
madrab2.goto(350,0)
madrab2.shapesize(stretch_wid=5,stretch_len=1) #تعديلات حجم المضرب

madrab3 = turtle.Turtle() #لرسم المضرب
madrab3.speed(0) #سرعة رسم الكرة
madrab3.shape("square") #تحديد شكل المضرب
madrab3.color("white") #تحديد لون المضرب 
madrab3.penup() #تمنع ظهور الخطوط
madrab3.goto(0,0)
madrab3.dx= 0.2 #اتجاه تحريك الكرة
madrab3.dy = 0.2

#عداد النقاط
score1 = 0
score2 = 0
scor = turtle.Turtle()
scor.speed(0)#سرعة الرسم
scor.color("white")
scor.penup()
scor.hideturtle()
scor.goto(0, 260)
scor.write("player 1:0 player 2:0", align="center", font=("Courier", 24,"normal"))

#function
def madrab1_up():
    y = madrab1.ycor() #بيجيب لي مكان المضرب الاول
    y +=20
    madrab1.sety(y) #تخزين مكان المضرب الجديد

def madrab1_down():
    y = madrab1.ycor() #بيجيب لي مكان المضرب الاول
    y -=20
    madrab1.sety(y) #تخزين مكان المضرب الجديد

def madrab2_up():
    y = madrab2.ycor() #بيجيب لي مكان المضرب الاول
    y +=20
    madrab2.sety(y) #تخزين مكان المضرب الجديد

def madrab2_down():
    y = madrab2.ycor() #بيجيب لي مكان المضرب الاول
    y -=20 #تحريك المضارب
    madrab2.sety(y) #تخزين مكان المضرب الجديد

#نربط الكيبورد بدالة حركة المضرب
wind.listen() #بيعرف المتغير انتظار الازرار
wind.onkeypress(madrab1_up,"w") #اذا ظغط على الحرف شغل الداله الموجوده
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"Up") #اذا ظغط على الحرف شغل الداله الموجوده
wind.onkeypress(madrab2_down,"Down")


while True:
    wind.update()
    #تحريك الكرة
    madrab3.setx(madrab3.xcor()+ madrab3.dx) #الكره تبدا عند الصفر وتزيد بمقار 0,2
    madrab3.sety(madrab3.ycor()+ madrab3.dy)
    #ارتداد الكرة
    if madrab3.ycor() > 290: #ارتداد الكره من اليمين 
        madrab3.sety(290) 
        madrab3.dy *= -1 #عكس رقم موقع الكرة واعادتها للصفر
    if madrab3.ycor() < -290:
        madrab3.sety(-290)
        madrab3.dy *= -1
    if madrab3.xcor() > 390 :
        madrab3.goto(0, 0)
        madrab3.dx *= -1
        score1 +=1 #في كل مره تخرج الكره يزيد بواحد
        scor.clear()
        scor.write("player 1:{} player 2:{}".format(score1, score2), align="center", font=("Courier", 24,"normal"))
         #format هذه الداله بتاخذ المتغيرات الي في الاقواس وبتحطها مكان {} الي قبلها 

    if madrab3.xcor() < -390 :
        madrab3.goto(0, 0)
        madrab3.dx *= -1
        score2 +=1 
        scor.clear()
        scor.write("player 1:{} player 2:{}".format(score1, score2), align="center", font=("Courier", 24,"normal"))
    #ارتداد الكره من المضارب
    if (madrab3.xcor() > 340 and madrab3.xcor() < 350 and (madrab3.ycor() < madrab2.ycor() + 40 and madrab3.ycor() > madrab2.ycor() - 40)):
        madrab3.setx(340)
        madrab3.dx *= -1
    if (madrab3.xcor() < -340 and madrab3.xcor() > -350 and (madrab3.ycor() < madrab1.ycor() + 40 and madrab3.ycor() > madrab1.ycor() - 40)):
        madrab3.setx(-340)
        madrab3.dx *= -1
