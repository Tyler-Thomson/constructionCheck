# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from . models import User, House, Section, Checklist, Check
#
# # class UserModel(admin.ModelAdmin):
# #     list_display = ["first_name", "last_name", "email", "password",
# #                                         "updated_at", "created_at"]
# #     list_display_links = ["first_name"]
# #     list_filter = ["first_name"]
# #     list_editable = ["last_name", "email", "password"]
# #     search_fields = ["user_name"]
# #
# #     class Meta:
# #         model = User
# #
# # admin.site.register(User, UserAdmin)
#
#
# class HouseModel(admin.ModelAdmin):
#     list_display = ["address", "city", "user", "checklist",
#                                         "updated_at", "created_at"]
#     list_display_links = ["address"]
#     list_filter = ["address"]
#     list_editable = ["address", "city", "user", "checklist"]
#     search_fields = ["address"]
#
#     class Meta:
#         model = House
#
# admin.site.register(House)
#
#
# class ChecklistModel(admin.ModelAdmin):
#     list_display = ["updated_at", "created_at"]
#     list_filter = ["created_at"]
#     search_fields = ["created_at"]
#
#     class Meta:
#         model = Checklist
#
# admin.site.register(Checklist)
#
#
# class SectionModel(admin.ModelAdmin):
#     list_display = ["name", "updated_at", "created_at"]
#     list_display_links = ["name"]
#     list_filter = ["name"]
#     list_editable = ["name"]
#     search_fields = ["name"]
#
#     class Meta:
#         model = Section
#
# admin.site.register(Section)
#
#
# class CheckModel(admin.ModelAdmin):
#     list_display = ["title", "checklist", "section",
#                             "updated_at", "created_at"]
#     list_filter = ["title"]
#     list_editable = ["title", "checklist", "section"]
#     search_fields = ["title"]
#
#     class Meta:
#         model = Check
#
# admin.site.register(Check)
