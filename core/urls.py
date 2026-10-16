from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "register/",
        views.register_farmer,
        name="register_farmer"
    ),

    path(
        "register/land/<int:farmer_id>/",
        views.register_land,
        name="register_land"
    ),

    path(
        "farmer-login/",
        views.farmer_login,
        name="farmer_login"
    ),

    path(
        "farmer-dashboard/",
        views.farmer_dashboard,
        name="farmer_dashboard"
    ),
    
path(
    "add-crop/<int:land_id>/",
    views.add_crop,
    name="add_crop"
),
path(
    "register/crop/<int:land_id>/",
    views.register_crop,
    name="register_crop"
),
path(
    "investor-register/",
    views.investor_register,
    name="investor_register"
),
path(
    "investor-login/",
    views.investor_login,
    name="investor_login"
),
path(
    "investor-dashboard/",
    views.investor_dashboard,
    name="investor_dashboard"
),
path(
    "investment-opportunity/<int:crop_id>/",
    views.investment_opportunity,
    name="investment_opportunity"
),
path(
    "send-investment-request/<int:crop_id>/",
    views.send_investment_request,
    name="send_investment_request"
),
path(
    "farmer/investment-requests/",
    views.farmer_investment_requests,
    name="farmer_investment_requests"
),

path(
    "farmer/investment-request/<int:request_id>/<str:action>/",
    views.update_investment_request,
    name="update_investment_request"
),
path(
    "logout/",
    views.user_logout,
    name="user_logout"
),
]