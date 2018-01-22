class QuickField:
    name = ""
    type = ""
    id = ""
    field = ""
    label = ""
    classes = []
    maxlength = ""
    placeholder = ""
    style = ""

    def __init__(self, name, label="", classes=[], size=3, type="text", id="", maxlength=155,
                 multiple=False, placeholder="", style=""):
        self.name = str(name)
        self.placeholder = str(placeholder)
        self.style = str(style)
        self.id = str(id)
        self.type = str(type)
        self.label = str(label)
        self.classes = classes
        self.maxlength = maxlength
        self.size = str(size)
        if not label:
            self.label = name
        if not id:
            self.id = name

    def build_field(self):
        self.field = self.get_label() + self.get_input()

        return self.get_col()

    def get_col(self):
        return "<div class=\"col-md-" + self.size + "\">\n\t<div class=\"form-group\">\n" + str(
            self.field) + "\t</div>\n</div>"

    def get_input(self, type="text"):
        attrs = self.get_field_attrs()

        return "\t\t<input maxlength=\"" + str(self.maxlength) + "\" type=\"" + type + "\" " + attrs + ">\n"

    def get_select(self):
        attrs = self.get_field_attrs()
        options = self.get_select_options()

        return "\t\t<select " + attrs + ">" + options + "</select>\n"

    def get_textarea(self):
        attrs = self.get_field_attrs()

        return "\t\t<textarea " + attrs + "></textarea>\n"

    def get_select_options(self):
        return "<option ></option>"

    def get_field_attrs(self):
        is_required = False
        placeholder = ""
        if self.placeholder:
            placeholder = "placeholder=\"" + self.placeholder + "\" "

        style = ""
        if self.style:
            style = "style=\"" + self.style + "\" "

        return style + placeholder + "class=\"form-control " + " ".join(self.classes) + "\"" + (
            "required" if is_required else "") + \
               " id=\"" + self.id + "\" name=\"" + self.name + "\""

    def get_label(self):
        return "\t\t<label for=\"" + self.id + "\" class=\"control-label\">" + self.label + "</label>\n"

    def get(self):
        return self.build_field()

    def __str__(self):
        return self.get()


C = QuickField("NomePaciente", "Nome", style="x")
print(C)
