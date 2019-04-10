from openpyxl import load_workbook

# read only file. Create a class to read a file
class SkillMigrationFileReader:

    def __init__(self, file_name_and_path):
        self.workbook = load_workbook(file_name_and_path, read_only=True)
        self.worksheet = self.workbook.active

    def return_cell_value(self, cell_reference):
        return self.worksheet[cell_reference].value

    def print_worksheet(self):
        for item in self.worksheet:
            print(item)

    def print_all_cell_data(self):
        list = []
        for row in self.worksheet.values:
            list.append(row)
        return list

    def print_all_data_cells_coordinates(self):
        for row in self.worksheet.rows:
            for p in row:
                print(p.coordinate)


reader = SkillMigrationFileReader("skill_migration.xlsx")
entire_table = reader.print_all_cell_data()


