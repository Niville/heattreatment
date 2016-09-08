# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "heat_treatment"
app_title = "Heat Treatment"
app_publisher = "Ragav"
app_description = "About process involved in ht"
app_icon = "octicon octicon-flame"
app_color = "#202020"
app_email = "sragav95@gmail.com"
app_license = "GNU"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/heat_treatment/css/heat_treatment.css"
# app_include_js = "/assets/heat_treatment/js/heat_treatment.js"

# include js, css files in header of web template
# web_include_css = "/assets/heat_treatment/css/heat_treatment.css"
# web_include_js = "/assets/heat_treatment/js/heat_treatment.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "heat_treatment.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "heat_treatment.install.before_install"
# after_install = "heat_treatment.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "heat_treatment.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"heat_treatment.tasks.all"
# 	],
# 	"daily": [
# 		"heat_treatment.tasks.daily"
# 	],
# 	"hourly": [
# 		"heat_treatment.tasks.hourly"
# 	],
# 	"weekly": [
# 		"heat_treatment.tasks.weekly"
# 	]
# 	"monthly": [
# 		"heat_treatment.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "heat_treatment.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "heat_treatment.event.get_events"
# }

