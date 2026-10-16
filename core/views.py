

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import FarmerForm, LandForm, CropForm, InvestorForm

from .models import Farmer, Land, Crop, Investor, InvestmentRequest, Notification

# --------------------------------------------------

# HOME

# --------------------------------------------------

def home(request):

    return render(request, "core/home.html")

# --------------------------------------------------

# FARMER REGISTRATION

# --------------------------------------------------

def register_farmer(request):

    if request.method == "POST":

        form = FarmerForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            password = form.cleaned_data["password"]

            if User.objects.filter(username=username).exists():

                form.add_error(

                    "username",

                    "This username is already taken."

                )

            else:

                user = User.objects.create_user(

                    username=username,

                    password=password

                )

                farmer = form.save(commit=False)

                farmer.user = user

                farmer.save()

                # Log in the newly registered farmer.

                login(request, user)

                # Continue with land registration.

                return redirect(

                    "register_land",

                    farmer_id=farmer.id

                )

    else:

        form = FarmerForm()

    return render(

        request,

        "core/register.html",

        {"form": form}

    )

# --------------------------------------------------

# LAND REGISTRATION

# --------------------------------------------------

def register_land(request, farmer_id):

    farmer = get_object_or_404(

        Farmer,

        id=farmer_id

    )

    # Only the owner of this profile can register land.

    if (

        not request.user.is_authenticated

        or farmer.user_id != request.user.id

    ):

        return redirect("farmer_login")

    if request.method == "POST":

        form = LandForm(request.POST, request.FILES)

        if form.is_valid():

            land = form.save(commit=False)

            land.farmer = farmer

            land.save()

            return redirect(

                "register_crop",

                land_id=land.id

            )

    else:

        form = LandForm()

    return render(

        request,

        "core/register_land.html",

        {

            "form": form,

            "farmer": farmer

        }

    )

# --------------------------------------------------

# ADD CROP

# Keep this function if your URLs use "add_crop".

# --------------------------------------------------

@login_required

def add_crop(request, land_id):

    farmer = Farmer.objects.filter(

        user=request.user

    ).first()

    if farmer is None:

        return render(

            request,

            "core/farmer_login.html",

            {

                "error": (

                    "This account is not linked to a farmer profile."

                )

            }

        )

    land = get_object_or_404(

        Land,

        id=land_id,

        farmer=farmer

    )

    if request.method == "POST":

        form = CropForm(request.POST)

        if form.is_valid():

            crop = form.save(commit=False)

            crop.land = land

            crop.save()

            return redirect("farmer_dashboard")

    else:

        form = CropForm()

    return render(

        request,

        "core/add_crop.html",

        {

            "form": form,

            "land": land

        }

    )

# --------------------------------------------------

# CROP REGISTRATION

# --------------------------------------------------

@login_required

def register_crop(request, land_id):

    farmer = Farmer.objects.filter(

        user=request.user

    ).first()

    if farmer is None:

        return render(

            request,

            "core/farmer_login.html",

            {

                "error": (

                    "This account is not linked to a farmer profile."

                )

            }

        )

    land = get_object_or_404(

        Land,

        id=land_id,

        farmer=farmer

    )

    if request.method == "POST":

        form = CropForm(request.POST)

        if form.is_valid():

            crop = form.save(commit=False)

            crop.land = land

            crop.save()

            return redirect("farmer_dashboard")

    else:

        form = CropForm()

    return render(

        request,

        "core/register_crop.html",

        {

            "form": form,

            "land": land

        }

    )

# --------------------------------------------------

# FARMER LOGIN

# Only one farmer_login function should exist.

# --------------------------------------------------

def farmer_login(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is None:

            return render(

                request,

                "core/farmer_login.html",

                {

                    "error": "Invalid username or password."

                }

            )

        farmer = Farmer.objects.filter(

            user=user

        ).first()

        if farmer is None:

            return render(

                request,

                "core/farmer_login.html",

                {

                    "error": (

                        "This account is not linked to a farmer profile."

                    )

                }

            )

        login(request, user)

        # Maintain compatibility with any existing code

        # that reads farmer_id from the session.

        request.session["farmer_id"] = farmer.id

        return redirect("farmer_dashboard")

    return render(

        request,

        "core/farmer_login.html"

    )

# --------------------------------------------------

# FARMER DASHBOARD

# Only one farmer_dashboard function should exist.

# --------------------------------------------------

@login_required

def farmer_dashboard(request):

    farmer = Farmer.objects.filter(

        user=request.user

    ).first()

    if farmer is None:

        return render(

            request,

            "core/farmer_login.html",

            {

                "error": (

                    "This account is not linked to a farmer profile."

                )

            }

        )

    return render(

        request,

        "core/farmer_dashboard.html",

        {"farmer": farmer}

    )

# --------------------------------------------------

# INVESTOR REGISTRATION

# --------------------------------------------------

def investor_register(request):

    if request.method == "POST":

        form = InvestorForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            password = form.cleaned_data["password"]

            if User.objects.filter(username=username).exists():

                form.add_error(

                    "username",

                    "This username is already taken."

                )

            else:

                user = User.objects.create_user(

                    username=username,

                    password=password,

                    email=form.cleaned_data["email"]

                )

                investor = form.save(commit=False)

                investor.user = user

                investor.save()

                return redirect("investor_login")

    else:

        form = InvestorForm()

    return render(

        request,

        "core/investor_register.html",

        {"form": form}

    )

# --------------------------------------------------

# INVESTOR LOGIN

# --------------------------------------------------

def investor_login(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is None:

            return render(

                request,

                "core/investor_login.html",

                {

                    "error": "Invalid username or password."

                }

            )

        investor = Investor.objects.filter(

            user=user

        ).first()

        if investor is None:

            return render(

                request,

                "core/investor_login.html",

                {

                    "error": (

                        "This account is not registered as an investor."

                    )

                }

            )

        login(request, user)

        request.session["investor_id"] = investor.id

        return redirect("investor_dashboard")

    return render(

        request,

        "core/investor_login.html"

    )

# --------------------------------------------------

# INVESTOR DASHBOARD

# --------------------------------------------------

@login_required

def investor_dashboard(request):

    investor = Investor.objects.filter(

        user=request.user

    ).first()

    if investor is None:

        return render(

            request,

            "core/investor_login.html",

            {

                "error": (

                    "This account is not registered as an investor."

                )

            }

        )

    crops = Crop.objects.select_related(

        "land",

        "land__farmer"

    ).all()

    return render(

        request,

        "core/investor_dashboard.html",

        {"crops": crops}

    )

# --------------------------------------------------

# INVESTMENT OPPORTUNITY DETAILS

# --------------------------------------------------

def investment_opportunity(request, crop_id):

    crop = get_object_or_404(

        Crop.objects.select_related(

            "land",

            "land__farmer"

        ),

        id=crop_id

    )

    return render(

        request,

        "core/investment_opportunity.html",

        {"crop": crop}

    )

# --------------------------------------------------

# INVESTOR SENDS AN INVESTMENT REQUEST

# --------------------------------------------------

@login_required

def send_investment_request(request, crop_id):

    if request.method != "POST":

        return redirect("investor_dashboard")

    investor = Investor.objects.filter(

        user=request.user

    ).first()

    if investor is None:

        return redirect("investor_login")

    crop = get_object_or_404(

        Crop,

        id=crop_id

    )

    # Prevent a second pending request for the same crop.

    existing_request = InvestmentRequest.objects.filter(

        investor=investor,

        crop=crop,

        status="pending"

    ).exists()

    if existing_request:

        messages.info(

            request,

            "You already have a pending request for this crop."

        )

        return redirect("investor_dashboard")

    investment_request = InvestmentRequest.objects.create(
        investor=investor,
        crop=crop,
        message=request.POST.get("message", "").strip()
    )

    # Dummy SMS-style notification for the farmer.
    farmer = crop.land.farmer
    if farmer.user_id:
        Notification.objects.create(
            recipient=farmer.user,
            investment_request=investment_request,
            title="New investment request",
            message=(
                f"Hi {farmer.name}, you have received a new investment "
                f"request from {investor.name} for {crop.crop_name}. "
                "Log in to Sempulam to view the details."
            )
        )

    messages.success(

        request,

        "Your investment request was sent successfully."

    )

    return redirect("investor_dashboard")

# --------------------------------------------------

# FARMER VIEWS INVESTMENT REQUESTS

# --------------------------------------------------

@login_required

def farmer_investment_requests(request):

    farmer = Farmer.objects.filter(

        user=request.user

    ).first()

    if farmer is None:

        return render(

            request,

            "core/farmer_login.html",

            {

                "error": (

                    "This account is not linked to a farmer profile."

                )

            }

        )

    investment_requests = InvestmentRequest.objects.filter(

        crop__land__farmer=farmer

    ).select_related(

        "investor",

        "crop",

        "crop__land"

    ).order_by("-created_at")

    return render(

        request,

        "core/farmer_investment_requests.html",

        {

            "farmer": farmer,

            "investment_requests": investment_requests

        }

    )

# --------------------------------------------------

# FARMER ACCEPTS OR DECLINES A REQUEST

# --------------------------------------------------

@login_required

def update_investment_request(request, request_id, action):

    if request.method != "POST":

        return redirect("farmer_investment_requests")

    farmer = Farmer.objects.filter(

        user=request.user

    ).first()

    if farmer is None:

        return redirect("farmer_login")

    # Ensure this request belongs to a crop owned by this farmer.

    investment_request = get_object_or_404(

        InvestmentRequest,

        id=request_id,

        crop__land__farmer=farmer

    )

    # Only pending requests can be updated.

    if investment_request.status != "pending":

        messages.info(

            request,

            "This request has already been processed."

        )

        return redirect("farmer_investment_requests")

    if action == "accept":

        investment_request.status = "accepted"

    elif action == "reject":

        investment_request.status = "rejected"

    else:

        return redirect("farmer_investment_requests")

    investment_request.save()

    # Dummy SMS-style notification for the investor.
    if action == "accept":
        notification_title = "Investment request accepted"
        notification_message = (
            f"Hi {investment_request.investor.name}, your investment "
            f"request for {investment_request.crop.crop_name} has been "
            "accepted by the farmer. Log in to Sempulam to view the next steps."
        )
    else:
        notification_title = "Investment request rejected"
        notification_message = (
            f"Hi {investment_request.investor.name}, your investment "
            f"request for {investment_request.crop.crop_name} has been "
            "rejected by the farmer. Log in to Sempulam to view your requests."
        )

    if investment_request.investor.user_id:
        Notification.objects.create(
            recipient=investment_request.investor.user,
            investment_request=investment_request,
            title=notification_title,
            message=notification_message
        )

    messages.success(

        request,

        f"Investment request {investment_request.get_status_display().lower()}."

    )

    return redirect("farmer_investment_requests")

# --------------------------------------------------

# LOGOUT

# --------------------------------------------------

@login_required

def user_logout(request):

    logout(request)

    return redirect("home")
