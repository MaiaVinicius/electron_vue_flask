module.exports = function (fieldType, fieldName, label, width, fieldValue, sqlOrClass, columnToShow, additionalTags) {
    this.buildField = function () {
        if (typeof fieldType === "string") {
            for (let f in this.fieldsModel) {
                if (this.fieldsModel[f].name === fieldType) {
                    fieldType = f;
                }
            }
        }

        let field = this.getFieldByType(fieldType);

        this.field = setCol(field, width);
    };

    this.fieldsModel = {
        1: {
            name: "text",
            getHtml: function () {
                return getLabel() + getInput();
            }
        },
        2: {
            name: "memo",
            getHtml: function () {
                return getLabel() + "<textarea class='form-control'></textarea>";
            }
        },
        3: {
            name: "simpleSelect",
            getHtml: function () {
                return getLabel() + getSelect();
            }
        },
        4: {
            name: "Radio/grava texto",
            getHtml: function () {
                return getLabel() + getInput();
            }
        },
        5: {
            name: "Checkboxes/grava texto",
            getHtml: function () {
                return getLabel() + getInput();
            }
        },
        6: {
            name: "currency",
            getHtml: function () {
                return getLabel() + getInput("currency");
            }
        },
        7: {
            name: "number",
            getHtml: function () {
                return getLabel() + getInput(false, "number");
            }
        },
        8: {
            name: "CPF",
            getHtml: function () {
                return getLabel() + getInput("cpf");
            }
        },
        9: {
            name: "CNPJ",
            getHtml: function () {
                return getLabel() + getInput("cnpj");
            }
        },
        10: {
            name: "datepicker",
            getHtml: function () {
                return getLabel() + getInput("datepicker");
            }
        },
        11: {
            name: "Hora",
            getHtml: function () {
                return getLabel() + getInput("time");
            }
        },
        12: {
            name: "Data e Hora",
            getHtml: function () {
                return getLabel() + getInput("datetime");
            }
        },
        13: {
            name: "Data Máscara",
            getHtml: function () {
                return getLabel() + getInput("date");
            }
        },
        14: {
            name: "phone",
            getHtml: function () {
                return getLabel() + getInput("phone");
            }
        },
        15: {
            name: "mobile",
            getHtml: function () {
                return getLabel() + getInput("phone");
            }
        },
        16: {
            name: "Cep",
            getHtml: function () {
                return getLabel() + getInput("cep");
            }
        },
        17: {
            name: "Imagem Única",
            getHtml: function () {
                return getLabel() + getInput();
            }
        },
        18: {
            name: "Múltiplo com Termos/grava texto",
            getHtml: function () {
                return getLabel() + getInput();
            }
        },
        19: {
            name: "Colorpicker Simples",
            getHtml: function () {
                return getLabel() + getInput();
            }
        },
        20: {
            name: "Colorpicker Médio",
            getHtml: function () {
                return getLabel() + getInput();
            }
        },
        21: {
            name: "editor",
            getHtml: function () {
                return getLabel() + getInput();
            }
        },
        22: {
            name: "email",
            getHtml: function () {
                return getLabel() + getInput(false, "email");
            }
        },
        23: {
            name: "contratado",
            getHtml: function () {
                return getLabel() + getInput();
            }
        },
        24: {
            name: "empresa",
            getHtml: function () {
                return getLabel() + getInput();
            }
        },
    };

    const setCol = function (field, size) {
        return "<div class='col-md-" + size + "'>" + field + "</div>";
    };

    function getInput(classes, type) {
        const isRequired = false;
        // const isRequired = obj.required === 1;
        const typeVal = typeof type !== "undefined" ? type : "text";
        return "<input type='" + typeVal + "' " + (isRequired ? "required" : "") + " " +
            "class='form-control " + (typeof classes !== "undefined" && classes ? classes : "") + "' name='" + fieldName + "'>";
    }

    function getSelect() {
        const isRequired = false;
        // const isRequired = obj.required === 1;

        return "<select " +
            "class='form-control' name='" + fieldName + "'></select>";
    }

    function getLabel() {
        return "<label class='control-label'>" + label + "</label>";
    }

    this.getFieldByType = function (fieldType) {
        // const fieldType = obj.fieldTypeID;

        let field = this.fieldsModel[fieldType].getHtml();
        return "<div class='form-group'>" + field + "</div>";
    };

    this.getField = function () {
        this.buildField();
        return this.field;
    };
};