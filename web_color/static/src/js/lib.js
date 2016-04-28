/* © 2012 Étienne Beaudry Auger - Savoir-faire Linux
   © 2016 Alex Comba - Agile Business Group sagl
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

openerp.web_color = function(instance) {
    
    widget_name = 'color';
    //Add in the widgets list
    instance.web.form.widgets.add(widget_name, 'openerp.web_color'); 
    //Add object in the column list
    instance.web.list.columns.add('field.color', 'instance.web.list.Color'); 
    //instance of the widget itself
    instance.web.list.Color = instance.web.list.Column.extend({
        /**
         * Return a formatted div colored and display the hexa color code
         * from row_data
         *
         * @private
         */
        _format: function (row_data, options) {
            return _.template(
                '<div class="colorviewer" style="background-color: <%-colorCode%>"></div>\
                <label style="padding-left: 5px"><%-colorCode%></label>', {
                    colorCode: row_data[this.id].value
                });

        }
    });
}
