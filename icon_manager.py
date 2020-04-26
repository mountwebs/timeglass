from PIL import Image, ImageDraw
import os, sys

class Icon_manager():
	def __init__(self, initial_seconds):
		self.icon_width = 30
		self.icon_height = 30
		self.image = Image.new("RGBA",(self.icon_width,self.icon_height),(0,0,0,0))
		self.draw = ImageDraw.Draw(self.image)
		self.icon_steps = 88 # 1-89
		self.icon_counter = 1
		self.active = False
		self.icon_interval = initial_seconds / self.icon_steps
		self.path = "Icons/"
		self.icon_path = self.get_icon_path()


	def set_icon_interval(self,seconds):
		self.icon_interval = seconds / self.icon_steps

	def reset(self):
		self.active = False
		self.icon_counter = 1

	# def get_icon_path(self):
	# 	if self.active:
	# 		return "{}timeglass{}.png".format(self.path,self.icon_counter)
	# 	else:
	# 		return "{}timeglass.png".format(self.path)

    #return os.path.join(os.environ.get("_MEIPASS2",os.path.abspath(".")),relative)

	# def resource_path(self, relative_path):
	#     """ Get absolute path to resource, works for dev and for PyInstaller """
	#     try:
	#         # PyInstaller creates a temp folder and stores path in _MEIPASS
	#         base_path = sys._MEIPASS
	#     except Exception:
	#         base_path = os.path.abspath(".")

	#     return os.path.join(base_path, relative_path)

	def resource_path(self,relative_path):
	    """ Get absolute path to resource, works for dev and for PyInstaller """
	    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
	    return os.path.join(base_path, relative_path)

	def get_icon_path(self):
		if self.active:
			filename = os.path.join(self.path,f"timeglass{self.icon_counter}.png")
		else:
			filename = os.path.join(self.path,"timeglass.png")

		icon_path = os.path.join(self.resource_path(filename))
		return icon_path


	def draw_squares (self, initial_sec, remaining_sec):
		hours_remaining = int((remaining_sec / 60)/60)
		minutes_remaining = (remaining_sec - (hours_remaining * 60 * 60))/60
		print(hours_remaining)

		self.image = Image.new("RGBA",(self.icon_width,self.icon_height),(0,0,0,0))
		self.draw = ImageDraw.Draw(self.image)

		h = 2 # height
		pb = 3 # padding between
		op = 1 # outer padding
		for i in range(hours_remaining):
			x1 = op
			y1 = op + i * (h + pb)
			x2 = 29 - op
			y2 = y1 + h
			#self.draw.rectangle([x1,y1,x2,y2], outline = (0,0,0,255), fill = (0,0,0,0))
			print("I {} h {}".format(i,hours_remaining))
			if i + 1 <= hours_remaining:
				self.draw.rectangle([x1,y1,x2,y2], outline = (0,0,0,255), fill = (0,0,0,255))
			#print(hours)

		#elif i + 1 == hours_remaining + 1:
		x_fill = int(26 * (minutes_remaining / 60))
		print("x:",x_fill)
		if x_fill > 0:
			x1 = op
			y1 = op + hours_remaining * (h + pb)
			y2 = y1 + h
			self.draw.rectangle([x1,y1,x_fill,y2], outline = (0,0,0,255), fill = (0,0,0,255))
		
		file_name = "icon.tiff"
		path = "{}{}".format(self.path,file_name)
		#self.image.show()
		self.image.save(path, 'TIFF')
		return path


	def draw_icon(self, lines):
		max_line = 29
		self.draw.rectangle([0,0,29,29], outline = (0,0,0,255), fill = (0,0,0,0))
		# for y in range(1,lines+1): #1-lines
		# 	draw.line([1,y,30,y],fill = (0,0,0,255))

		for y in range(1,lines+1): #1-lines - 
			self.draw.line([1,max_line - y,30,max_line - y],fill = (0,0,0,255))
		#if full:

		self.image.save("test.tiff", 'TIFF')


