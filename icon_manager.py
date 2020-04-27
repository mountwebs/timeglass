import os, sys

class Icon_manager():
	def __init__(self, initial_seconds):
		self.cli = False
		self.icon_steps = 88 # 1-89
		self.icon_counter = 1
		self.active = False
		self.icon_interval = initial_seconds / self.icon_steps
		self.path = "Icons/"
		self.icon_path = self.get_icon_path()
		self.inverted = False
		
	def set_icon_interval(self,seconds):
		self.icon_interval = seconds / self.icon_steps

	def reset(self):
		self.active = False
		self.icon_counter = 1

	def resource_path(self,relative_path):
	    """ Get absolute path to resource, works for dev and for PyInstaller """
	    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
	    return os.path.join(base_path, relative_path)

	def invert(self):
		if self.inverted:
			filename = os.path.join(self.path,"timeglass.png")
			self.inverted = False
		else:
			filename = os.path.join(self.path,"timeglass_inverted.png")
			self.inverted = True

		if not self.cli:
			return os.path.join(self.resource_path(filename))
		else:
			return filename

	def get_icon_path(self):
		if self.active:
			filename = os.path.join(self.path,f"timeglass{self.icon_counter}.png")
		else:
			filename = os.path.join(self.path,"timeglass.png")
		if not self.cli:
			icon_path = os.path.join(self.resource_path(filename))
		else:
			icon_path = filename
		return icon_path


