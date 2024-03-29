###
# @format
# -----
# Project: @eventiva/eventiva
# File: hooks.py
# Path: \projects\modules\grand_theft_auto\grand_theft_auto\hooks.py
# Created Date: Sunday, January 14th 2024
# Author: Jonathan Stevens, jonathan@resnovas.com
# Github: https://github.com/TGTGamer
# -----
# Contributing: Please read through our contributing guidelines.
# Included are directions for opening issues, coding standards,
# and notes on development. These can be found at
# https://github.com/eventiva/eventiva/blob/develop/CONTRIBUTING.md
# -----
# Code of Conduct: This project abides by the Contributor Covenant, v2.0
# Please interact in ways that contribute to an open, welcoming, diverse,
# inclusive, and healthy community. Our Code of Conduct can be found at
# https://github.com/eventiva/eventiva/blob/develop/CODE_OF_CONDUCT.md
# -----
# Copyright (c) 2024 Resnovas - All Rights Reserved
# LICENSE: GNU General Public License v2.0 or later (GPL-2.0-or-later)
# -----
# This program has been provided under confidence of the copyright holder and
# is licensed for copying, distribution and modification under the terms
# of the GNU General Public License v2.0 or later (GPL-2.0-or-later) published as the License,
# or (at your option) any later version of this license.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License v2.0 or later for more details.
# You should have received a copy of the GNU General Public License v2.0 or later
# along with this program. If not, please write to: jonathan@resnovas.com,
# or see https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# -----
# This project abides by the GPL Cooperation Commitment.
# Before filing or continuing to prosecute any legal proceeding or claim
# (other than a Defensive Action) arising from termination of a Covered
# License, we commit to extend to the person or entity ('you') accused
# of violating the Covered License the following provisions regarding
# cure and reinstatement, taken from GPL version 3.
# For further details on the GPL Cooperation Commitment please visit
# the official website: https://gplcc.github.io/gplcc/
# -----
# DELETING THIS NOTICE AUTOMATICALLY VOIDS YOUR LICENSE
###



app_name = "grand_theft_auto"
app_title = "Grand Theft Auto"
app_publisher = "Eventiva"
app_description = "Integrate Grand Theft Auto specific endpoints into Eventiva Gaming"
app_email = "gta.gaming.application@eventiva.co.uk"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/grand_theft_auto/css/grand_theft_auto.css"
# app_include_js = "/assets/grand_theft_auto/js/grand_theft_auto.js"

# include js, css files in header of web template
# web_include_css = "/assets/grand_theft_auto/css/grand_theft_auto.css"
# web_include_js = "/assets/grand_theft_auto/js/grand_theft_auto.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "grand_theft_auto/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "grand_theft_auto/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "grand_theft_auto.utils.jinja_methods",
# 	"filters": "grand_theft_auto.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "grand_theft_auto.install.before_install"
after_install = "grand_theft_auto.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "grand_theft_auto.uninstall.before_uninstall"
# after_uninstall = "grand_theft_auto.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "grand_theft_auto.utils.before_app_install"
# after_app_install = "grand_theft_auto.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "grand_theft_auto.utils.before_app_uninstall"
# after_app_uninstall = "grand_theft_auto.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "grand_theft_auto.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"grand_theft_auto.tasks.all"
# 	],
# 	"daily": [
# 		"grand_theft_auto.tasks.daily"
# 	],
# 	"hourly": [
# 		"grand_theft_auto.tasks.hourly"
# 	],
# 	"weekly": [
# 		"grand_theft_auto.tasks.weekly"
# 	],
# 	"monthly": [
# 		"grand_theft_auto.tasks.monthly"
# 	],
# }

# Testing
# -------

before_tests = "grand_theft_auto.install_test"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "grand_theft_auto.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "grand_theft_auto.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["grand_theft_auto.utils.before_request"]
# after_request = ["grand_theft_auto.utils.after_request"]

# Job Events
# ----------
# before_job = ["grand_theft_auto.utils.before_job"]
# after_job = ["grand_theft_auto.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"grand_theft_auto.auth.validate"
# ]
