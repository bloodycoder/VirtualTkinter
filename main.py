# -*- coding: cp936 -*-
#-*- coding: utf8 -*-
spaces='    '
save_time=0
from string import *
from Tkinter import *
from ttk import *
from math import sqrt
root=Tk()
win=[root]
bu_foreground=StringVar()
bu_background=StringVar()
root_x=StringVar()
root_y=StringVar()
root_x.set(500)
root_y.set(500)
bu_foreground.set('black')
bu_background.set('white')
root.title('Visual Tkinter')
Style().configure("TButton", padding=2, relief="flat",
   background="#ccc")
#定义全局变量
s = '#代码由vitual tkinter 生成\nfrom Tkinter import * \nroot=Tk()\n'
#画图的类
class draw:
    img5  =PhotoImage(file='pic\oval.gif')
    img6 =PhotoImage(file='pic\circle.gif')
    img7 =PhotoImage(file='pic/rectangle.gif')
    img8 =PhotoImage(file='pic/polygon.gif')
    img9 =PhotoImage(file='pic/line.gif')
    img10  =PhotoImage(file='pic\canvas.gif')
    tag_ing=0   #    0就是没有选中
    total  =0   #   total 是计数器，生成标签
    all_tag=[]
    drawwhat=0 # 0 就不画 ，1 画 圆              5 画多边形
    poly_num=0             #多边形个数
    save_dic=dict()       #用于保存多边形
    wid=StringVar()
    iv=IntVar()
    iv.set(1)
    wid.set(1)
    out=StringVar()
    out.set('black')
    fil=StringVar()
    fil.set('blue')
    x_tag=StringVar()
    y_tag=StringVar()    
    x_tag.set(0)
    y_tag.set(0)
    x0=0
    y0=0
    x1=0
    y1=0
    cv=Canvas(root,bg='gray',width=500)
    poly=[]
    def setxy0(self,event):
        draw_canvas.x0=event.x
        draw_canvas.y0=event.y
        print 'you click','x',event.x,'y',event.y
        if self.drawwhat==5:
            self.poly.append((event.x,event.y))
            self.draw()
        print self.poly
    def setxy1(self,event):
        draw_canvas.x1=event.x
        draw_canvas.y1=event.y
        print 'you reliese','x',event.x,'y',event.y
        if self.drawwhat!=5:
            draw_canvas.draw()
    def changedraw(self,i):
        draw_canvas.drawwhat=i
        #poly 变为空数组
    def set_poly(self) :
        self.drawwhat=5
        self.poly=[]
    def draw(self):
        if self.drawwhat==1:
            self.total+=1
            ji=self.total
            if abs(self.x0-self.x1)>=3  or abs(self.y0-self.y1)>=3:
                self.cv.create_oval(self.x0,self.y0,self.x1,self.y1,width=self.wid.get(),outline=self.out.get(),fill=self.fil.get(),tags=str(self.total))
                self.cv.tag_bind(str(ji),'<Button-1>',self.choosetag)        
            else:
                self.total-=1
        elif self.drawwhat==2:
            self.total+=1
            ji=self.total
            if abs(self.x0-self.x1)>=3 or  abs(self.y0-self.y1)>=3:
                r=cal_dis(self.x0,self.y0,self.x1,self.y1)
                self.cv.create_oval(self.x0-r/sqrt(2),self.y0-r/sqrt(2),self.x0+r/sqrt(2),self.y0+r/sqrt(2),width=self.wid.get(),outline=self.out.get(),fill=self.fil.get(),tags=str(self.total))
                self.cv.tag_bind(str(ji),'<Button-1>',self.choosetag)                
            else:
                self.total-=1
        elif self.drawwhat==3:
            self.total+=1
            ji=self.total
            if abs(self.x0-self.x1)>=3 or abs(self.y0-self.y1)>=3:
                self.cv.create_line(self.x0,self.y0,self.x1,self.y1,width=self.wid.get(),fill=self.fil.get(),tags=str(self.total))
                self.cv.tag_bind(str(ji),'<Button-1>',self.choosetag)               
            else:
                self.total-=1
        elif self.drawwhat==4:
            self.total+=1
            ji=self.total
            if abs(self.x0-self.x1)>=3  or abs(self.y0-self.y1)>=3:
                self.cv.create_rectangle(self.x0,self.y0,self.x1,self.y1,width=self.wid.get(),outline=self.out.get(),fill=self.fil.get(),tags=str(self.total))
                self.cv.tag_bind(str(ji),'<Button-1>',self.choosetag)        
            else:
                self.total-=1
        elif self.drawwhat==5:
            #n是边数
            n=len(self.poly)
            self.total+=1
            ji=self.total
            print n
            #  self.poly[0]    self.poly[n-1]         cal_dis2(self.poly[0] ,self.poly[n-1])<100
            if  cal_dis2(self.poly[0] ,self.poly[n-1])<5 and n>=3:
                self.cv.create_polygon(self.poly,width=self.wid.get(),outline=self.out.get(),fill=self.fil.get(),tags=str(self.total))
                self.cv.tag_bind(str(ji),'<Button-1>',self.choosetag)
                self.save_dic[self.poly_num]=self.poly
                self.poly_num+=1
                self.poly=[]
        
            else:
                if n>=2:
                    self.cv.create_line((self.poly[n-1],self.poly[n-2]),width=self.wid.get(),fill=self.fil.get(),tags=str(self.total))
                self.total-=1   
    def choosetag(self,event):
        if  self.iv.get()==1:
            print 'ok'
            self.tag_ing=self.cv.gettags('current')
            print self.cv.bbox(self.tag_ing[0])
            print self.tag_ing[0]
            wid=self.cv.itemcget(self.tag_ing[0], 'width')
            fil=self.cv.itemcget(self.tag_ing[0], 'fill')
            if self.cv.type(self.tag_ing[0])!='line':
                out=self.cv.itemcget(self.tag_ing[0], 'outline')        
            self.wid.set(wid)
            self.fil.set(fil)
            if self.cv.type(self.tag_ing[0])!='line':
                self.out.set(out)   
    def setnew(self):
        self.cv.itemconfigure(self.tag_ing[0],width=self.wid.get())
        self.cv.itemconfigure(self.tag_ing[0],fill=self.fil.get())
        self.cv.itemconfigure(self.tag_ing[0],outline=self.out.get())
        self.cv.move(self.tag_ing[0],self.x_tag.get(),self.y_tag.get())
    def setnew2(self,event):
        self.cv.itemconfigure(self.tag_ing[0],width=self.wid.get())
        self.cv.itemconfigure(self.tag_ing[0],fill=self.fil.get())
        self.cv.itemconfigure(self.tag_ing[0],outline=self.out.get())
        self.cv.move(self.tag_ing[0],self.x_tag.get(),self.y_tag.get())
    def delete(self):
        self.cv.delete(self.tag_ing[0])

    def draw_button(self):
        Button(root,text='Canvas ',compound='left',image=self.img10,command=self.draw_tan,width=5).place(relx=0.88,rely=0.92)
    def draw_tan(self):

        #paper 将来会变root
        self.cv.pack(side=LEFT,fill=Y)
        control=Toplevel(root)
        control.title('control')
        Button(control,image=self.img5,command=lambda: self.changedraw(1),width=5).grid(row=0,column=0)
        Button(control,image=self.img6,command=lambda: self.changedraw(2),width=5).grid(row=0,column=1)
        Button(control,image=self.img9,command=lambda: self.changedraw(3),width=5).grid(row=0,column=2)
        Button(control,image=self.img7,command=lambda: self.changedraw(4),width=5).grid(row=0,column=3)
        Button(control,image=self.img8,command= self.set_poly,width=5).grid(row=0,column=4) 
        Checkbutton(control,variable = self.iv,text='select').grid(row=5,column=3)
        Label(control,text='width  ').grid(row=2,column=2)
        sc=Scale(control,from_=1,to=50,orient=HORIZONTAL,variable=self.wid)
        sc.grid(row=2,column=3)
        sc.bind('<B1-Motion>',self.setnew2)
        
        Label(control,text='outline').grid(row=2,column=0)
        cb2=Combobox(control,textvariable=self.out,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow'])
        cb2.grid(row=2,column=1)
        Label(control,text='fill   ').grid(row=3,column=0)
        cb1=Combobox(control,textvariable=self.fil,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow'])
        cb1.grid(row=3,column=1)
        Label(control,text='x_move ').grid(row=4,column=0)
        Entry(control,textvariable=self.x_tag,width=5).grid(row=4,column=1)
        Label(control,text='y_move ').grid(row=4,column=2)
        Entry(control,textvariable=self.y_tag,width=5).grid(row=4,column=3)
        Button(control,text='Set ',command=self.setnew,width=5).grid(row=5,column=2)
        self.cv.bind('<Button-1>',draw_canvas.setxy0)
        self.cv.bind('<ButtonRelease-1>',draw_canvas.setxy1)
        Button(control,text='delete ',command=self.delete,width=5).grid(row=5,column=1)
    def create_draw(self):
        if self.total>=1:
            s_add1='\ncv=Canvas(root,width=500,height=500)\ncv.pack()'
        #cv.create_oval(self.x0,self.y0,self.x1,self.y1,width=self.wid.get(),tags=str(self.total))
            for tag in range(1,self.total+1):
                if self.cv.type(str(tag))=='oval':
                    add_s='\ncv.create_%s(%s,width=%s,outline="%s",fill="%s")'%(self.cv.type(str(tag)),self.cv.bbox(str(tag)),self.cv.itemcget(str(tag), 'width'),self.cv.itemcget(str(tag), 'outline'),self.cv.itemcget(str(tag), 'fill'))
                if self.cv.type(str(tag))=='line':
                    zuobiao=self.cv.bbox(str(tag))
                    if (self.y1-self.y0)/self.x1-self.x0 <0:
                        add_s='\ncv.create_%s(%s,width=%s,fill="%s")'%(self.cv.type(str(tag)),self.cv.coords(str(tag)),self.cv.itemcget(str(tag), 'width'),self.cv.itemcget(str(tag), 'fill'))
                    elif  (self.y1-self.y0)/self.x1-self.x0 >0:
                        print 'change'
                        zuobiao=[self.x0,self.y1,self.x1,self.y0]
                        zuobiao=tuple(zuobiao)
                        add_s='\ncv.create_%s(%s,width=%s,fill="%s")'%(self.cv.type(str(tag)),self.cv.coords(str(tag)),self.cv.itemcget(str(tag), 'width'),self.cv.itemcget(str(tag), 'fill'))
                if self.cv.type(str(tag))=='rectangle':
                    add_s='\ncv.create_%s(%s,width=%s,outline="%s",fill="%s")'%(self.cv.type(str(tag)),self.cv.bbox(str(tag)),self.cv.itemcget(str(tag), 'width'),self.cv.itemcget(str(tag), 'outline'),self.cv.itemcget(str(tag), 'fill'))                        
                if self.cv.bbox(str(tag))!=None:
                    s_add1=join([s_add1,add_s])
            for po in range(self.poly_num):
                add_s='\ncv.create_polygon(%s,width=%s,fill="%s")'%(self.save_dic[po],self.cv.itemcget(str(self.total), 'width'),self.cv.itemcget(str(self.total), 'fill'))
                s_add1=join([s_add1,add_s])
            return s_add1
        else:
            return '\n'
# 计算两点之间的距离
def cal_dis(x0,y0,x1,y1):
    return ((x0-x1)**2+(y1-y0)**2)**(1.0/2)
def cal_dis2((x0,y0),(x1,y1)):
    return ((x0-x1)**2+(y1-y0)**2)**(1.0/2)  

#得到坐标
def get_xy(event):
    t2 = Toplevel(root)
    t2.title('the point you click')
    f2=Frame(t2,width=100,height=50)
    f2.pack()
    Label(f2,text='you clicked (%s,%s)'%(str(event.x),str(event.y))).pack()

#文件名
e=StringVar()
v=StringVar()
com=StringVar()
frame_x=StringVar()
frame_y=StringVar()

#保存字符串 s
def save(s,save_time,f_name):
    s2=draw_canvas.create_draw()
    print type(s2)
    s=s+s2
    s_add='\nroot.geometry("%sx%s+0+0")\nroot.mainloop()'%(root_x.get(),root_y.get())
    s=join([s,s_add])
    f_name=f_name+'.py'
    f=open(f_name,'w')
    f.write(s)
    f.close()

    print 'hello'
#-----------------------------------------------------------------------------------tan  懂吗----------------------------------------------------------------------
#-----------------------------------------------------------------------------------tan  懂吗----------------------------------------------------------------------
#save的弹出框
import  tkFileDialog
def save_tan():
    e.set('youwillneverknow')
    e.set(tkFileDialog.asksaveasfilename())
    if e.get()!='':
        tran_save()
    


#button 弹出框 调用了全局变量 
def button_tan():
    global win
    e.set('picard')
    frame_x.set(12)
    frame_y.set(12)
    com.set('NONE')
#增加输入坐标功能

#输入坐标功能结束   
    t2 = Toplevel(root)
    t2.title('adjust your button here')
    Label(t2,text='-text           ').grid(row=0,column=0)
    entry=Entry(t2,textvariable=e,width=5)
    entry.grid(row=0,column=1)
    
    om= OptionMenu(t2,v,'root')
    for x in range(len(win)):
        if x !=0:
            om['menu'].insert('end','command',label=str(win[x]),command=lambda:button_tan_son(str(win[x])))
    om.grid(row=1,column=1)
    Label(t2,text='-position       ').grid(row=1,column=0)
    Label(t2,text='-(x,y)   ').grid(row=2,column=0)
    Label(t2,text='-command ').grid(row=3,column=0)
    Label(t2,text='-foreground ').grid(row=4,column=0)
    Combobox(t2,textvariable=bu_foreground,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=4,column=1)
    Entry(t2,textvariable=frame_x,width=5).grid(row=2,column=1,pady=5)
    Entry(t2,textvariable=frame_y,width=5).grid(row=2,column=2,pady=5)
    Entry(t2,textvariable=com,width=5).grid(row=3,column=2,pady=5)
    v.set('root')
    Button(t2,text='OK.',command=tran_button).grid(row=11,column=2)

def button_tan_son(name):
        v.set(name)

#size of Screen的弹出框
def frame_tan():
    frame_x.set(12)
    frame_y.set(12)
    t2=Toplevel(root)
    f=Frame(t2,width=200,height=150)
    f.pack()
    Label(f,text='width').place(relx=0.05,rely=0.05)
    entry1=Entry(f,textvariable=root_x,width=5)
    entry1.place(relx=0.3,rely=0.05)
    Label(f,text='height').place(relx=0.05,rely=0.25)
    entry2=Entry(f,textvariable=root_y,width=5)
    entry2.place(relx=0.3,rely=0.25)
    Button(f,text='OK.').place(relx=0.5,rely=0.5)

#size of label的弹出框
def label_tan():
    e.set('picard')
    frame_x.set(12)
    frame_y.set(12)
    com.set('NONE')
    t2=Toplevel(root)
    Label(t2,text='-text                ').grid(row=0,column=0)
    entry1=Entry(t2,textvariable=e,width=5)
    entry1.grid(row=0,column=1)
    Button(t2,text='OK.',command=tran_label).grid(row=4,column=3,pady=5)
    Label(t2,text='-(x,y)               ').grid(row=1,column=0)
    Label(t2,text='-textvariable').grid(row=2,column=0)
    Label(t2,text='-foreground ').grid(row=3,column=0)
    Combobox(t2,textvariable=bu_foreground,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=3,column=1,pady=5,padx=5
                                                                                                                )
    Entry(t2,textvariable=frame_x,width=5).grid(row=1,column=1,pady=5,padx=5)
    Entry(t2,textvariable=frame_y,width=5).grid(row=1,column=2,pady=5,padx=5)
    Entry(t2,textvariable=com,width=5).grid(row=2,column=1)


#size of label的弹出框
def entry_tan():
    e.set('picard')
    frame_x.set(12)
    frame_y.set(12)
    t2=Toplevel(root)
    Label(t2,text='-textvariable').grid(row=0,column=0,pady=5)
    
    entry1=Entry(t2,textvariable=e,width=5)
    entry1.grid(row=0,column=1)
    Button(t2,text='OK.',command=tran_entry).grid(row=11,column=3,pady=5)
    Label(t2,text='-(x,y)               ').grid(row=1,column=0)
    Entry(t2,textvariable=frame_x,width=5).grid(row=1,column=1,pady=5,padx=5)
    Entry(t2,textvariable=frame_y,width=5).grid(row=1,column=2,padx=5,pady=5)
    Label(t2,text='-foreground ').grid(row=2,column=0)
    Combobox(t2,textvariable=bu_foreground,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=2,column=1,pady=5,padx=5)
    Label(t2,text='-background ').grid(row=3,column=0)
    Combobox(t2,textvariable=bu_background,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=3,column=1,pady=5,padx=5)
                    
         
#size of checkbutton的弹出框
def checkbutton_tan():
    e.set('picard')
    frame_x.set(12)
    frame_y.set(12)
    t2=Toplevel(root)
    Label(t2,text='-textvariable').grid(row=0,column=0,pady=5)
    
    entry1=Entry(t2,textvariable=e,width=5)
    entry1.grid(row=0,column=1)
    Button(t2,text='OK.',command=tran_checkbutton).grid(row=11,column=3,pady=5)
    Label(t2,text='-(x,y)               ').grid(row=1,column=0)
    Entry(t2,textvariable=frame_x,width=5).grid(row=1,column=1,pady=5,padx=5)
    Entry(t2,textvariable=frame_y,width=5).grid(row=1,column=2,padx=5,pady=5)
    Label(t2,text='-foreground ').grid(row=2,column=0)
    Combobox(t2,textvariable=bu_foreground,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=2,column=1,pady=5,padx=5)
    Label(t2,text='-background ').grid(row=3,column=0)
    Combobox(t2,textvariable=bu_background,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=3,column=1,pady=5,padx=5)
                    
def radiobutton_tan():
    e.set('picard')
    frame_x.set(12)
    frame_y.set(12)
    t2=Toplevel(root)
    Label(t2,text='-textvariable').grid(row=0,column=0,pady=5)
    
    entry1=Entry(t2,textvariable=e,width=5)
    entry1.grid(row=0,column=1)
    Button(t2,text='OK.',command=tran_radiobutton).grid(row=11,column=3,pady=5)
    Label(t2,text='-(x,y)               ').grid(row=1,column=0)
    Entry(t2,textvariable=frame_x,width=5).grid(row=1,column=1,pady=5,padx=5)
    Entry(t2,textvariable=frame_y,width=5).grid(row=1,column=2,padx=5,pady=5)
    Label(t2,text='-foreground ').grid(row=2,column=0)
    Combobox(t2,textvariable=bu_foreground,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=2,column=1,pady=5,padx=5)
    Label(t2,text='-background ').grid(row=3,column=0)
    Combobox(t2,textvariable=bu_background,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=3,column=1,pady=5,padx=5)
def scale_tan():
    e.set('picard')
    frame_x.set(12)
    frame_y.set(12)
    t2=Toplevel(root)
    Label(t2,text='-textvariable').grid(row=0,column=0,pady=5)
    
    entry1=Entry(t2,textvariable=e,width=5)
    entry1.grid(row=0,column=1)
    Button(t2,text='OK.',command=tran_scale).grid(row=11,column=3,pady=5)
    Label(t2,text='-(x,y)               ').grid(row=1,column=0)
    Entry(t2,textvariable=frame_x,width=5).grid(row=1,column=1,pady=5,padx=5)
    Entry(t2,textvariable=frame_y,width=5).grid(row=1,column=2,padx=5,pady=5)
    Label(t2,text='-foreground ').grid(row=2,column=0)
    Combobox(t2,textvariable=bu_foreground,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=2,column=1,pady=5,padx=5)
    Label(t2,text='-background ').grid(row=3,column=0)
    Combobox(t2,textvariable=bu_background,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=3,column=1,pady=5,padx=5)
       
def spinbox_tan():
    e.set('picard')
    frame_x.set(12)
    frame_y.set(12)
    t2=Toplevel(root)
    Label(t2,text='-textvariable').grid(row=0,column=0,pady=5)
    
    entry1=Entry(t2,textvariable=e,width=5)
    entry1.grid(row=0,column=1)
    Button(t2,text='OK.',command=tran_spinbox).grid(row=11,column=3,pady=5)
    Label(t2,text='-(x,y)               ').grid(row=1,column=0)
    Entry(t2,textvariable=frame_x,width=5).grid(row=1,column=1,pady=5,padx=5)
    Entry(t2,textvariable=frame_y,width=5).grid(row=1,column=2,padx=5,pady=5)
    Label(t2,text='-foreground ').grid(row=2,column=0)
    Combobox(t2,textvariable=bu_foreground,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=2,column=1,pady=5,padx=5)
    Label(t2,text='-background ').grid(row=3,column=0)
    Combobox(t2,textvariable=bu_background,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=3,column=1,pady=5,padx=5)
def text_tan():
    e.set('picard')
    frame_x.set(12)
    frame_y.set(12)
    t2=Toplevel(root)
    Label(t2,text='-textvariable').grid(row=0,column=0,pady=5)
    
    entry1=Entry(t2,textvariable=e,width=5)
    entry1.grid(row=0,column=1)
    Button(t2,text='OK.',command=tran_text).grid(row=11,column=3,pady=5)
    Label(t2,text='-(x,y)               ').grid(row=1,column=0)
    Entry(t2,textvariable=frame_x,width=5).grid(row=1,column=1,pady=5,padx=5)
    Entry(t2,textvariable=frame_y,width=5).grid(row=1,column=2,padx=5,pady=5)
    Label(t2,text='-foreground ').grid(row=2,column=0)
    Combobox(t2,textvariable=bu_foreground,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=2,column=1,pady=5,padx=5)
    Label(t2,text='-background ').grid(row=3,column=0)
    Combobox(t2,textvariable=bu_background,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=3,column=1,pady=5,padx=5)
def scrollbar_tan():
    e.set('picard')
    frame_x.set(12)
    frame_y.set(12)
    t2=Toplevel(root)
    Label(t2,text='-textvariable').grid(row=0,column=0,pady=5)
    
    entry1=Entry(t2,textvariable=e,width=5)
    entry1.grid(row=0,column=1)
    Button(t2,text='OK.',command=tran_scrollbar).grid(row=11,column=3,pady=5)
    Label(t2,text='-(x,y)               ').grid(row=1,column=0)
    Entry(t2,textvariable=frame_x,width=5).grid(row=1,column=1,pady=5,padx=5)
    Entry(t2,textvariable=frame_y,width=5).grid(row=1,column=2,padx=5,pady=5)
    Label(t2,text='-foreground ').grid(row=2,column=0)
    Combobox(t2,textvariable=bu_foreground,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=2,column=1,pady=5,padx=5)
    Label(t2,text='-background ').grid(row=3,column=0)
    Combobox(t2,textvariable=bu_background,width=5,values=['blue','yellow','gray','black','red','green','brown','violet','pink','white','snow']).grid(row=3,column=1,pady=5,padx=5)
       

#---------------------------------------------------------------------tran-------------------------------------------------------------------------------------
#---------------------------------------------------------------------tran--------------------------------------------------------------------------------------
#所有全局变量的聚集地: i =1 代表save ，i=2 代表加一行框架（屏幕大小）
# i=3 代表增加一行button
def all_var(i):
    global s,save_time,e
    f_name=e.get()
    if i==1 :
        save(s,save_time,f_name)
        save_time+=1
    if i==2 :
        s=create_frame(s)
    if i==3 :
        s=create_bu(s)
    if i==4 :
        s=create_label(s)
    if i==5 :
        s=create_entry(s)    
    if i==6:
        s=create_checkbutton(s)
    if i==7:
        s=create_radiobutton(s)
    if i==8:
        s=create_scale(s)
    if i==9:
        s=create_spinbox(s)
    if i==10:
        s=create_text(s)
    if i==11:
        s=create_scrollbar(s)
                        
#所有的中转函数
def tran_save():
    all_var(1)

def tran_frame():
    all_var(2)
def tran_button():
    all_var(3)
def tran_label():
    all_var(4)
def tran_entry():
    all_var(5)
def tran_checkbutton():
    all_var(6)
def tran_radiobutton():
    all_var(7)
def tran_scale():
    all_var(8)
def tran_spinbox():
    all_var(9)
def tran_text():
    all_var(10)
def tran_scrollbar():
    all_var(11)
#所有弹出框的集合


#-----------------------------------------------------------------------------create-------------------------------------------------------------------------
#-----------------------------------------------------------------------------create-------------------------------------------------------------------------
#为s增加一行创建按钮的代码
def create_bu(s):
    B_text=e.get()
    s_add='\nButton(text= "%s"+"%s").place(x=%s,y=%s)' %(B_text,bu_foreground.get(),frame_x.get(),frame_y.get())
    eval(s_add)
    s_add='\nButton(text= "%s",foreground="%s",command=%s).place(x=%s,y=%s)' %(B_text,bu_foreground.get(),com.get(),frame_x.get(),frame_y.get())
    s=join([s,s_add])
    return s

#为s增加一行创建frame的代码
def create_frame(s):
    x = frame_x.get()
    y = frame_y.get()
    s_add1='\nf1=Frame(root,width=%s,height=%s,bg="grey")'%(x,y)
    s_add2='\nf1.pack()'
    f1=Frame(root_frame,width=x,height=y,bg="grey")
    f1.place(relx=0.5,rely=0.5,anchor=CENTER)
    f1.bind('<Button-1>',get_xy)
    win.append('f1')
    return join([s,s_add1+s_add2])
#为s增加一行创建label的代码
def create_label(s):
    B_text=e.get()
    s_add='\nLabel(text= "%s"+"%s").place(x=%s,y=%s)' %(B_text,bu_foreground.get(),frame_x.get(),frame_y.get())
    eval(s_add)
    if com.get()!='NONE':
        s_add='\n%s=StringVar()\nLabel(text= "%s",textvariable=%s,foreground="%s").place(x=%s,y=%s)' %(com.get(),B_text,com.get(),bu_foreground.get(),frame_x.get(),frame_y.get())
    else:
        s_add='\n%s=StringVar()\nLabel(text= "%s",foreground="%s").place(x=%s,y=%s)' %(com.get(),B_text,bu_foreground.get(),frame_x.get(),frame_y.get())
    s=join([s,s_add])
    return s
#为s增加一行创建entry的代码
def create_entry(s):
    B_text=e.get()
    s_add='\n%s=StringVar()\nEntry(textvariable= %s,foreground="%s",background="%s").place(x=%s,y=%s)' %(B_text,B_text,bu_foreground.get(),bu_background.get(),frame_x.get(),frame_y.get())
    s=join([s,s_add])
    s_add='\nEntry().place(x=%s,y=%s)' %(frame_x.get(),frame_y.get())
    eval(s_add)
    return s
#为s增加一行创建checkbutton的代码
def create_checkbutton(s):
    B_text=e.get()
    s_add='\nCheckbutton(foreground="%s",background="%s").place(x=%s,y=%s)' %(bu_foreground.get(),bu_background.get(),frame_x.get(),frame_y.get())
    s=join([s,s_add])
    s_add='\nCheckbutton().place(x=%s,y=%s)' %(frame_x.get(),frame_y.get())
    eval(s_add)
    return s
def create_radiobutton(s):
    B_text=e.get()
    s_add='\nRadiobutton(foreground="%s",background="%s").place(x=%s,y=%s)' %(bu_foreground.get(),bu_background.get(),frame_x.get(),frame_y.get())
    s=join([s,s_add])
    s_add='\nRadiobutton().place(x=%s,y=%s)' %(frame_x.get(),frame_y.get())
    eval(s_add)
    return s
def create_scale(s):
    B_text=e.get()
    s_add='\nScale(foreground="%s",background="%s").place(x=%s,y=%s)' %(bu_foreground.get(),bu_background.get(),frame_x.get(),frame_y.get())
    s=join([s,s_add])
    s_add='\nScale().place(x=%s,y=%s)' %(frame_x.get(),frame_y.get())
    eval(s_add)
    return s
def create_spinbox(s):
    B_text=e.get()
    s_add='\nSpinbox(foreground="%s",background="%s").place(x=%s,y=%s)' %(bu_foreground.get(),bu_background.get(),frame_x.get(),frame_y.get())
    s=join([s,s_add])
    s_add='\nSpinbox().place(x=%s,y=%s)' %(frame_x.get(),frame_y.get())
    eval(s_add)
    return s
def create_text(s):
    B_text=e.get()
    s_add='\nText(foreground="%s",background="%s").place(x=%s,y=%s)' %(bu_foreground.get(),bu_background.get(),frame_x.get(),frame_y.get())
    s=join([s,s_add])
    s_add='\nText(width=40,height=20).place(x=%s,y=%s)' %(frame_x.get(),frame_y.get())
    eval(s_add)
    return s
def create_scrollbar(s):
    B_text=e.get()
    s_add='\nScrollbar().place(x=%s,y=%s)' %(frame_x.get(),frame_y.get())
    s=join([s,s_add])
    s_add='\nScrollbar().place(x=%s,y=%s)' %(frame_x.get(),frame_y.get())
    eval(s_add)
    return s
#Ui时间到

#做菜单栏
menubar=Menu(root)
menubar.add_command(label = 'save',command =save_tan)
root['menu'] = menubar

#做框架
root_frame=Frame(root,width=500,height=500)

#所有弹出框的集合
tool_frame=Frame(root,width=80,height=500,relief=RAISED)


#为菜单栏添加菜单
img  =PhotoImage(file='pic\ha.gif')
img1 =PhotoImage(file='pic\size.gif')
img2 =PhotoImage(file='pic\label.gif')
img3 =PhotoImage(file='pic\entry.gif')
img4 =PhotoImage(file='pic/checkbu.gif')
img5 =PhotoImage(file='pic/radiobutton.gif')
img6 =PhotoImage(file='pic/spinbox.gif')
img7 =PhotoImage(file='pic/text.gif')
img8 =PhotoImage(file='pic/scrollbar.gif')
img9 =PhotoImage(file='pic/scale.gif')
# 鼠标松开的函数（拖动）  i 用于判断是什么按钮
class release:
    x0=0
    y0=0
    def setxy(self,event):
        self.x0=event.x
        self.y0=event.y
        print 'hello'
        print self.x0,' ',self.y0
    def button_release(self,event):
        self.setxy(event)
        if self.x0<=0:
            button_tan()
            frame_x.set(self.x0+530)
            frame_y.set(self.y0)
    def label_release(self,event):
        self.setxy(event)
        if self.x0<=0:
            label_tan()
            frame_x.set(self.x0+530)
            frame_y.set(self.y0+100)

    def entry_release(self,event):
        self.setxy(event)
        if self.x0<=0:
            entry_tan()
            frame_x.set(self.x0+530)
            frame_y.set(self.y0+130)
    def checkbutton_release(self,event):
        self.setxy(event)
        if self.x0<=0:
            checkbutton_tan()
            frame_x.set(self.x0+530)
            frame_y.set(self.y0+190)
    def radiobutton_release(self,event):
        self.setxy(event)
        if self.x0<=0:
            radiobutton_tan()
            frame_x.set(self.x0+530)
            frame_y.set(self.y0+220)
    def scale_release(self,event):
        self.setxy(event)
        if self.x0<=0:
            scale_tan()
            frame_x.set(self.x0+530)
            frame_y.set(self.y0+270)
    def spinbox_release(self,event):
        self.setxy(event)
        if self.x0<=0:
            spinbox_tan()
            frame_x.set(self.x0+500)
            frame_y.set(self.y0+330)
    def text_release(self,event):
        self.setxy(event)
        if self.x0<=0:
            text_tan()
            frame_x.set(self.x0+500)
            frame_y.set(self.y0+230)
    def scrollbar_release(self,event):
        self.setxy(event)
        if self.x0<=0:
            scrollbar_tan()
            frame_x.set(self.x0+500)
            frame_y.set(self.y0+410)
drag= release()
root.geometry('600x500+0+0')
bu1=Button(root,text='button',compound='left',image=img,command=button_tan,width=5)
bu1.place(relx=0.88,rely=0.02)
bu1.bind('<ButtonRelease-1>',drag.button_release)
bu2=Button(text='size  ',compound='left',image=img1,command=frame_tan,width=5)
bu2.place(relx=0.88,rely=0.11)
bu3=Button(text='Label ',compound='left',image=img2,command=label_tan,width=5)
bu3.place(relx=0.88,rely=0.20)
bu3.bind('<ButtonRelease-1>',drag.label_release)
bu4=Button(text='Entry ',compound='left',image=img3,command=entry_tan,width=5)
bu4.place(relx=0.88,rely=0.29)
bu4.bind('<ButtonRelease-1>',drag.entry_release)
bu4=Button(text='checkbutton ',compound='left',image=img4,command=checkbutton_tan,width=5)
bu4.place(relx=0.88,rely=0.38)
bu4.bind('<ButtonRelease-1>',drag.checkbutton_release)
bu4=Button(text='radiobutton ',compound='left',image=img5,command=radiobutton_tan,width=5)
bu4.place(relx=0.88,rely=0.47)
bu4.bind('<ButtonRelease-1>',drag.radiobutton_release)
bu4=Button(text='scale',compound='left',image=img5,command=scale_tan,width=5)
bu4.place(relx=0.88,rely=0.56)
bu4.bind('<ButtonRelease-1>',drag.scale_release)
bu4=Button(text='spinbox',compound='left',image=img6,command=spinbox_tan,width=5)
bu4.place(relx=0.88,rely=0.65)
bu4.bind('<ButtonRelease-1>',drag.spinbox_release)
bu4=Button(text='text        ',compound='left',image=img7,command=text_tan,width=5)
bu4.place(relx=0.88,rely=0.74)
bu4.bind('<ButtonRelease-1>',drag.text_release)
bu4=Button(text='scrollbar',compound='left',image=img8,command=scrollbar_tan,width=5)
bu4.place(relx=0.88,rely=0.83)
bu4.bind('<ButtonRelease-1>',drag.scrollbar_release)
draw_canvas=draw()
draw_canvas.draw_button()
root.mainloop()




    


