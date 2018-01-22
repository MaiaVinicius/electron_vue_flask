const QuickField = require('./quickField');

module.exports = function () {

    /*let rows = [];
     const setInRow = function (rowId, field) {
     if (typeof rows[rowId] === "undefined") {
     rows[rowId] = [];
     }
     rows[rowId].push(field);
     };

     const getRows = function () {
     let rowsHtml = "";
     rows.forEach(function (entry) {
     rowsHtml += "<div class='row'>" + entry.join("") + "</div>";
     });
     return rowsHtml;
     };
     */
    this.form = "";

    this.buildForm = function () {
        for (let fieldKey in this.data) {
            let obj = this.data[fieldKey];

            if (obj.showInForm) {
                let field = new QuickField(obj.fieldTypeID, obj.columnName, obj.label, obj.size, obj.defaultValue, '', '', '');
                this.form += field.getField();
            }
        }
    };

    this.getForm = function () {
        this.buildForm();
        return this.form;
    };
};