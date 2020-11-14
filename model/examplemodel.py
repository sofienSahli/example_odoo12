from .... import models, fields


class ExampleClass(models.Model):
    _name = "example.class"
    _description = "exmaple description"
    name = fields.Char(string="Name")
    roll_no = fields.Integer(string="roll_number")
    division = fields.Char('Div')
