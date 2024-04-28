# from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('', views.dispHome),
    path('home/', views.dispHome, name="Home"),
    path('university/', views.dispUniversity),
    path('Universities/IIS-Bangalore/', views.dispIIS, name="IIS"),
    path('Universities/Jawaharlal-Nehru-University/', views.dispJnu, name="JNU"),
    path('Universities/Jamia-Millia-Islamia-University/', views.dispJmiu, name="JMIU"),
    path('Universities/Jadavpur-University/', views.dispJadavpur, name="JDP"),
    path('Universities/Jadavpur-University/Engineering-&-Technology/', views.dispJDPEngTech),
    path('Universities/Jadavpur-University/Science/', views.dispJDPSci),
    path('Universities/Jadavpur-University/ISLM/', views.dispJDPISLM),
    # path('Universities/Jadavpur-University/Arts/', include("CalendarHome.urls")),
    # path('Universities/Jadavpur-University/Engineering-&-Technology/', include("CalendarHome.urls")),
    # path('Universities/Jadavpur-University/Science/', include("CalendarHome.urls")),
    # path('Universities/Jadavpur-University/ISLM/', include("CalendarHome.urls")),
    path('Universities/Amrita-Vishwa-Vidyapeetham/', views.dispAVV, name="AVV"),
    path('Universities/VIT/', views.dispVIT, name="VIT"),
    path('Universities/BHU/', views.dispBHU, name="BHU"),
    path('Universities/DUpost/', views.dispDUpost, name="DUP"),
    path('Universities/DUunder/', views.dispDUunder, name="DUU"),
    path('Universities/University-Of-Hyderabad/', views.dispUOH, name="UOH"),
    path('Universities/Amity/', views.dispAmity, name="AMY"),
    path('Universities/Bharathiar-University/', views.dispBU, name="BU"),
    path('Universities/Panjab-University/', views.dispPU, name="PU"),
    path('Universities/Mysore-University/', views.dispMysore, name="MYU"),
    path('Universities/Chandigarh-University/', views.dispCU, name="CHU"),
    path('Universities/Andhra-University/', views.dispAU, name="ANU"),
    path('Universities/Guru-Nanak-Dev-University/', views.dispGNDU, name="GNDU"),
    path('Universities/University-Of-Kashmir/', views.dispKashmir, name="UOK"),
    path('Universities/University-Of-Jammu/', views.dispJammu, name="UOJ"),
    path('Universities/Pondicherry-University/', views.dispPondicherry, name="POU"),
    path('Universities/Tezpur-University/', views.dispTezpur, name="TZU"),
    path('Universities/Gauhati-University/', views.dispGauhati, name="UOG"),
    path('aboutUs/', views.dispAboutUs, name="About"),
    path('termsAndConditions/', views.dispTermsAndConditions, name="TnC"),
    path('filter-by-date/', views.dispFilter, name="filter"),
    path('filter-by-date/<str:date>/', views.filter_by_date, name='filter_by_date'),
    path('chatbot/', views.dispChatbot),
    path('logout/', views.dispLogout, name='logout'),
    path('signUp/', views.dispSignUp, name='signUp'),
    path('login', views.dispLogin, name='login'),
    path('profile/', views.dispProfile),
]