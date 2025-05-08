from django.contrib import admin
from .models import User, Product, Order

# Registering the User model with custom display fields
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'date_joined')  # Customize as needed
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

# Registering the Product model
class OrderInline(admin.TabularInline):
    model = Order
    extra = 0  # This will avoid displaying empty forms for new orders
    fields = ('buyer', 'quantity', 'total_price', 'status')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock_quantity', 'seller')
    list_filter = ('category',)
    search_fields = ('name', 'category')
    ordering = ('name',)
    inlines = [OrderInline]  # Display related orders inline within the product view

# Registering the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'product', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('buyer__username', 'product__name')
    ordering = ('-created_at',)
    exclude = ('created_at',)  # Exclude 'created_at' field from the form
    # Explicitly define which fields should be shown in the form (excluding 'created_at')
    fields = ('buyer', 'product', 'quantity', 'total_price', 'status')
