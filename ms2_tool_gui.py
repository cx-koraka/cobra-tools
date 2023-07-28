import sys
import time
import logging
# Check Python version, setup logging
from ovl_util.setup import ms2_tool_setup # pyright: ignore
# Import widgets before everything except Python built-ins and ovl_util.setup!
from ovl_util import widgets, interaction
from ovl_util.widgets import get_icon
from generated.formats.ms2 import Ms2File
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(widgets.MainWindow):

	def __init__(self):
		widgets.MainWindow.__init__(self, "MS2 Editor", )
		self.resize(600, 600)
		self.setAcceptDrops(True)

		self.ms2_file = Ms2File()

		self.filter = "Supported files (*ms2)"

		self.file_widget = self.make_file_widget(ftype="MS2")

		header_names = ["Name", "File Type", "LODs", "Objects", "Meshes", "Materials"]

		# create the table
		self.files_container = widgets.SortableTable(header_names, (), ignore_drop_type="MS2")
		# connect the interaction functions
		self.files_container.table.table_model.member_renamed.connect(self.rename_handle)
		self.files_container.table.hideColumn(1)

		# Configure table button row
		self.btn_duplicate = widgets.SelectedItemsButton(self, icon=get_icon("duplicate_mesh"))
		self.btn_duplicate.clicked.connect(self.duplicate)
		self.btn_duplicate.setToolTip("Duplicate Selected Meshes")
		self.btn_delete = widgets.SelectedItemsButton(self, icon=get_icon("delete_mesh"))
		self.btn_delete.clicked.connect(self.remove)
		self.btn_delete.setToolTip("Delete Selected Meshes")
		# Add buttons to table
		self.files_container.add_button(self.btn_duplicate)
		self.files_container.add_button(self.btn_delete)

		self.qgrid = QtWidgets.QGridLayout()
		self.qgrid.addWidget(self.file_widget, 0, 0)
		self.qgrid.addWidget(self.files_container, 1, 0)
		self.qgrid.addWidget(self.p_action, 2, 0)
		self.central_widget.setLayout(self.qgrid)

		main_menu = self.menu_bar
		file_menu = main_menu.addMenu('File')
		edit_menu = main_menu.addMenu('Edit')
		button_data = (
			(file_menu, "Open", self.file_widget.ask_open, "CTRL+O", "dir"),
			(file_menu, "Append", self.append, "", "append"),
			(file_menu, "Save", self.file_widget.ask_save, "CTRL+S", "save"),
			(file_menu, "Save As", self.file_widget.ask_save_as, "CTRL+SHIFT+S", "save"),
			(file_menu, "Exit", self.close, "", "exit"),
			(edit_menu, "Duplicate Selected", self.duplicate, "SHIFT+D", "duplicate_mesh"),
			(edit_menu, "Remove Selected", self.remove, "DEL", "delete_mesh"),
		)
		self.add_to_menu(button_data)

	def rename_handle(self, old_name, new_name):
		"""this manages the renaming of a single entry"""
		# force new name to be lowercase
		new_name = new_name.lower()
		try:
			if self.ms2_file.name_used(new_name):
				self.showwarning(f"Model {new_name} already exists in ms2!")
			# new name is new
			else:
				self.ms2_file.rename_file(old_name, new_name)
				self.set_file_modified(True)
		except:
			self.handle_error("Renaming failed, see log!")
		self.update_gui_table()

	def remove(self):
		selected_file_names = self.files_container.table.get_selected_files()
		if selected_file_names:
			try:
				self.ms2_file.remove(selected_file_names)
				self.set_file_modified(True)
			except:
				self.handle_error("Removing file failed, see log!")
			self.update_gui_table()

	def duplicate(self):
		selected_file_names = self.files_container.table.get_selected_files()
		if selected_file_names:
			try:
				self.ms2_file.duplicate(selected_file_names)
				self.set_file_modified(True)
			except:
				self.handle_error("Duplicating file failed, see log!")
			self.update_gui_table()

	def open(self, filepath):
		if filepath:
			self.set_file_modified(False)
			try:
				self.ms2_file.load(filepath, read_editable=True)
			except:
				self.handle_error("Loading failed, see log!")
			self.update_gui_table()

	def append(self):
		if self.file_widget.is_open():
			append_path = QtWidgets.QFileDialog.getOpenFileName(
				self, f'Append MS2', self.cfg.get(f"dir_ms2s_in", "C://"), self.file_widget.files_filter_str)[0]
			if append_path:
				try:
					other_ms2_file = Ms2File()
					other_ms2_file.load(append_path, read_editable=True)
					# ensure that there are no name collisions
					for model in other_ms2_file.model_infos:
						self.ms2_file.make_name_unique(model)
						self.ms2_file.model_infos.append(model)
					self.set_file_modified(True)
				except:
					self.handle_error("Appending failed, see log!")
				self.update_gui_table()

	def update_gui_table(self, ):
		start_time = time.time()
		try:
			logging.info(f"Loading {len(self.ms2_file.mdl_2_names)} files into gui")
			self.files_container.set_data([[m.name, ".mdl2", m.num_lods, m.num_objects, m.num_meshes, m.num_materials] for m in self.ms2_file.model_infos])
			logging.info(f"Loaded GUI in {time.time() - start_time:.2f} seconds")
			self.set_msg_temporarily("Operation completed!")
		except:
			self.handle_error("GUI update failed, see log!")

	def save(self, filepath) -> None:
		try:
			self.ms2_file.save(filepath)
			self.set_file_modified(False)
			self.set_msg_temporarily(f"Saved {self.ms2_file.name}")
		except:
			self.handle_error("Saving MS2 failed, see log!")


if __name__ == '__main__':
	widgets.startup(MainWindow)
