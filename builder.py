class CodeBuilder:
    def __init__(self, class_name):
        self.class_name = class_name
        self.fields = []

    def add_field(self, name, age=None):
        self.fields.append((name, age))
        return self  # võimaldab chaining

    def __str__(self):
        lines = [f'class {self.class_name}:', '', '  def __init__(self):']
        for name, age in self.fields:
            lines.append(f'    self.{name} = {age}')
        return '\n'.join(lines)


        

    





cb = CodeBuilder('Person').add_field('name', '""') .add_field('age', '0')
print(cb) 
