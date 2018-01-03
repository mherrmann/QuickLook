from fman import DirectoryPaneCommand
from fman.url import as_human_readable
from subprocess import Popen

class QuickLook(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor:
			Popen(['qlmanage', '-p', as_human_readable(file_under_cursor)])