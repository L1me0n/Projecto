from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

class MyApp(App):
	def build(self):
		bbbl=BoxLayout(orientation='vertical', padding=[0,0,0,100])
		bbl=BoxLayout(orientation='horizontal', spacing=100, size_hint=[1, 5])
		bl=BoxLayout(orientation='vertical', padding=[0, 0, 0, 100])
		bls=BoxLayout(orientation='vertical', padding=[0, 90, 0, 100])
		bl.add_widget(Label(text="Введите число"))
		self.txt=TextInput(multiline=False)
		bl.add_widget(self.txt)
		self.ten=Button(text="10", on_press=self.btn_press, background_color=[1,0,0,1], background_normal='')
		self.eight=Button(text="8", on_press=self.btn_press, background_color=[1,0,0,1], background_normal='')
		self.two=Button(text="2", on_press=self.btn_press, background_color=[1,0,0,1], background_normal='')
		self.sixt=Button(text="16", on_press=self.btn_press, background_color=[1,0,0,1], background_normal='')
		bl.add_widget(self.ten)
		bl.add_widget(self.eight)
		bl.add_widget(self.two)
		bl.add_widget(self.sixt)
		self.tens=Button(text="10", on_press=self.btn_press, background_color=[1,0,0,1], background_normal='')
		self.eights=Button(text="8", on_press=self.btn_press, background_color=[1,0,0,1], background_normal='')
		self.twos=Button(text="2", on_press=self.btn_press, background_color=[1,0,0,1], background_normal='')
		self.sixts=Button(text="16", on_press=self.btn_press, background_color=[1,0,0,1], background_normal='')
		bls.add_widget(self.tens)
		bls.add_widget(self.eights)
		bls.add_widget(self.twos)
		bls.add_widget(self.sixts)
		self.lbl=Label(text="Результат", size_hint=[1, .2], font_size=48)
		bbl.add_widget(bl)
		bbl.add_widget(bls)
		bbbl.add_widget(bbl)
		bbbl.add_widget(self.lbl)
		return bbbl

	def btn_press(self, instance):
		def abc(a, r, x):
			if a//x==0:
				for z in range(10, 16):
					y="ABCDEF"
					if x==16 and(a//x==z or a%x==z):
						r=y[z-10]+r
				if a%x<10 or a%x>15:
					r=str(a%x)+r
				return r
			else:
				for z in range(10, 16):
					y="ABCDEF"
					if x==16 and a%x==z:
						r=y[z-10]+r
						break
				if a%x<10 or a%x>15:
					r=str(a%x)+r
				a=a//x
				return abc(a, r, x)
		f=0
		if instance.text=="10" and instance==self.ten:
			t=10
			self.eight.background_color=[1,0,0,1]
			self.two.background_color=[1,0,0,1]
			self.sixt.background_color=[1,0,0,1]
			instance.background_color=[0,1,0,1]
		if instance.text=="8" and instance==self.eight:
			t=8
			self.ten.background_color=[1,0,0,1]
			self.two.background_color=[1,0,0,1]
			self.sixt.background_color=[1,0,0,1]
			instance.background_color=[0,1,0,1]
		if instance.text=="2" and instance==self.two:
			t=2
			self.eight.background_color=[1,0,0,1]
			self.ten.background_color=[1,0,0,1]
			self.sixt.background_color=[1,0,0,1]
			instance.background_color=[0,1,0,1]
		if instance.text=="16" and instance==self.sixt:
			t=16
			self.eight.background_color=[1,0,0,1]
			self.two.background_color=[1,0,0,1]
			self.ten.background_color=[1,0,0,1]
			instance.background_color=[0,1,0,1]
		if instance.text=="10" and instance==self.tens:
			f=10
			self.eights.background_color=[1,0,0,1]
			self.twos.background_color=[1,0,0,1]
			self.sixts.background_color=[1,0,0,1]
			instance.background_color=[0,1,0,1]
		if instance.text=="8" and instance==self.eights:
			f=8
			self.tens.background_color=[1,0,0,1]
			self.twos.background_color=[1,0,0,1]
			self.sixts.background_color=[1,0,0,1]
			instance.background_color=[0,1,0,1]
		if instance.text=="2" and instance==self.twos:
			f=2
			self.eights.background_color=[1,0,0,1]
			self.tens.background_color=[1,0,0,1]
			self.sixts.background_color=[1,0,0,1]
			instance.background_color=[0,1,0,1]
		if instance.text=="16" and instance==self.sixts:
			f=16
			self.eights.background_color=[1,0,0,1]
			self.twos.background_color=[1,0,0,1]
			self.tens.background_color=[1,0,0,1]
			instance.background_color=[0,1,0,1]
		if f!=0 and self.txt.text!="":
			a=self.txt.text
			if self.ten.background_color==[0,1,0,1]:
				a=int(a)
				if f==16 and a>=10 and a<=15:
					for z in range(10, 16):
						y="ABCDEF"
						if a==z:
							self.lbl.text=y[z-10]
				else:	
					r=""
					self.lbl.text=abc(a, r, f)
			elif self.eight.background_color==[0,1,0,1]:
				a=int(a)
				if self.tens.background_color==[0,1,0,1]:
					a=str(a)[-1::-1]
					d=0
					sum=0
					while len(a)>0:
						sum=sum+(8**d)*int(a[0])
						a=a[1:]
						d=d+1
					self.lbl.text=str(sum)
				elif self.twos.background_color==[0,1,0,1]:
					a=str(a)[-1::-1]
					d=0
					sum=0
					while len(a)>0:
						sum=sum+(8**d)*int(a[0])
						a=a[1:]
						d=d+1
					r=""
					self.lbl.text=abc(sum, r, 2)
				elif self.sixts.background_color==[0,1,0,1]:
					a=str(a)[-1::-1]
					d=0
					sum=0
					while len(a)>0:
						sum=sum+(8**d)*int(a[0])
						a=a[1:]
						d=d+1
					r=""
					self.lbl.text=abc(sum, r, 16)
				else:
					self.lbl.text=self.txt.text
			elif self.two.background_color==[0,1,0,1]:
				a=int(a)
				if self.tens.background_color==[0,1,0,1]:
					a=str(a)[-1::-1]
					d=0
					sum=0
					while len(a)>0:
						sum=sum+(2**d)*int(a[0])
						a=a[1:]
						d=d+1
					self.lbl.text=str(sum)
				elif self.eights.background_color==[0,1,0,1]:
					a=str(a)[-1::-1]
					d=0
					sum=0
					while len(a)>0:
						sum=sum+(2**d)*int(a[0])
						a=a[1:]
						d=d+1
					r=""
					self.lbl.text=abc(sum, r, 8)
				elif self.sixts.background_color==[0,1,0,1]:
					a=str(a)[-1::-1]
					d=0
					sum=0
					while len(a)>0:
						sum=sum+(2**d)*int(a[0])
						a=a[1:]
						d=d+1
					r=""
					self.lbl.text=abc(sum, r, 16)
				else:
					self.lbl.text=self.txt.text
			else:
				if self.tens.background_color==[0,1,0,1]:
					a=a[-1::-1]
					d=0
					sum=0
					while len(a)>0:
						g=False
						for z in range(10, 16):
							y="ABCDEF"
							if (y[z-10]==a[0]):
								sum=sum+(16**d)*z
								g=True
						if g==False:
							sum=sum+(16**d)*int(a[0])
						a=a[1:]
						d=d+1
					self.lbl.text=str(sum)
				elif self.eights.background_color==[0,1,0,1]:
					a=a[-1::-1]
					d=0
					sum=0
					while len(a)>0:
						g=False
						for z in range(10, 16):
							y="ABCDEF"
							if (y[z-10]==a[0]):
								sum=sum+(16**d)*z
								g=True
						if g==False:
							sum=sum+(16**d)*int(a[0])
						a=a[1:]
						d=d+1
					r=""
					self.lbl.text=abc(sum, r, 8)
				elif self.twos.background_color==[0,1,0,1]:
					a=a[-1::-1]
					d=0
					sum=0
					while len(a)>0:
						g=False
						for z in range(10, 16):
							y="ABCDEF"
							if (y[z-10]==a[0]):
								sum=sum+(16**d)*z
								g=True
						if g==False:
							sum=sum+(16**d)*int(a[0])
						a=a[1:]
						d=d+1
					r=""
					self.lbl.text=abc(sum, r, 2)
				else:
					self.lbl.text=self.txt.text
if __name__=="__main__":
	MyApp().run()	