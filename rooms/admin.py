from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address","price")}
        ),
        (
            "Times",
            {"classes":("collapse",),"fields": ("check_in","check_out","instant_book")}
        ),
        (
            "Spaces",
            {"classes":("collapse",),
             "fields": (
                "guests",
                "beds",
                "bedrooms",
                "baths",
            )}
        ),
        (
            "More About the Space",
            {"classes":("collapse",),"fields": ("amenties","facilities","house_rules",)}
        ),
        (
            "Last Details",
            {"classes":("collapse",),"fields": ("host",)}
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book"
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenties",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("^city","^host__username",)

    filter_horizontal = (
        "amenties",
        "facilities",
        "house_rules",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
