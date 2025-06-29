con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="payroll"
    )
    d = con.cursor()
    def load_table(self,r):
        layout = AnchorLayout()
        self.button_box = MDBoxLayout(
            pos_hint={"center_x": 0.5},
            adaptive_size=True,
            padding="24dp",
            spacing="24dp",
        )

        for self.button_text in ["Add Employee", "Update Employee","Refresh", "Delete","Back"]:
            self.button_box.add_widget(
                MDRaisedButton(
                    text=self.button_text, on_release=self.on_button_press
                )
            )
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.8, 0.9),
            padding=50,
            use_pagination=True,
            check=True,
            #column_height=52,
            #column_padding=56,
            rows_num=8,
            elevation=20,
            background_color_header="#65275d",
            background_color_selected_cell="e4514f",
            column_data=[
                ("Emp ID", dp(30)),
                ("Emp Code", dp(30)),
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Dept ID", dp(30)),
                ("POS ID", dp(30)),
                ("Salary", dp(30)),
                 ],
             )
        for x in r:
            self.data_tables.add_row(x)
        self.add_widget(self.data_tables)
        self.add_widget(self.button_box)
        return layout
        self.d.close()
        self.con.close()

    def on_enter(self):
        query = "select emp_id, emp_code,emp_firstname, emp_lastname, dept_id, pos_id, emp_salary from employee"
        self.d.execute(query)
        self.r = self.d.fetchall()
        self.load_table(self.r)
    def on_button_press(self, instance_button: MDRaisedButton) -> None:
        '''Called when a control button is clicked.'''

        try:
            {
                "Add Employee": self.add_employee,
                "Update Employee": self.update_employee,
                "Refresh":self.refresh,
                "Delete":self.delete,
                "Back":self.back,
            }[instance_button.text]()
        except KeyError:
            pass

    def add_employee(self):
        self.manager.current="Add_Employee"
    def update_employee(self):
        self.manager.current="Update_Employee"
    def refresh(self):
        query = "select * from employee order by emp_id asc"
        self.d.execute(query)
        self.r = self.d.fetchall()
        self.load_table(self.r)
    def delete(self):
        pass
    def back(self):
        self.manager.current="Payroll"