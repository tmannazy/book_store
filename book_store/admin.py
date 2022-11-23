from django.contrib import admin

class BookStoreAdminSite(admin.AdminSite):
	site_header = "Book store site"
	site_title = "Book store"
	index_title = "Book store admin interface"