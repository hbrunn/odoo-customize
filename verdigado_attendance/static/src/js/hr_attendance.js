/* Copyright 2023 Hunki Enterprises BV
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define("verdigado_attendance.hr_attendance", function (require) {
    "use strict";

    var myAttendances = require("hr_attendance.my_attendances");

    myAttendances.include({
        willStart: function () {
            var self = this;
            var promise = this._rpc({
                model: "res.users",
                method: "get_effective_holiday_overtime_factor",
            }).then(function (data) {
                self.effective_holiday_overtime_factor = data;
            });
            return Promise.all([this._super.apply(this, arguments), promise]);
        },
        _rpc: function (params) {
            if (
                params &&
                params.model === "hr.employee" &&
                params.method === "attendance_manual"
            ) {
                params.context.default_apply_holiday_overtime_factor = this.$(
                    "#apply_holiday_overtime"
                ).is(":checked");
            }
            return this._super.apply(this, arguments);
        },
    });
});