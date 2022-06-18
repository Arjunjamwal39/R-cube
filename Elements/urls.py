from unicodedata import name
from Elements import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as accounting
from .forms import Changedapassword, LogindaUser, EnterdaUser, Forgotpass, ForgotpassConfirm

urlpatterns = [
    #path('', homey),
    #path('homey/', homey),
    path('', views.Homeyview.as_view(), name='homey'),
    path('homey/', views.Homeyview.as_view(), name='homey'),
    path('practice/', views.Practiceview.as_view(), name='practice'),              
    path('item-detail/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'), #required
    path('allproduct/', views.Productdisplay, name='allproduct'),                      #required
    path('allproduct/<slug:data>', views.Productdisplay, name='allproductdata'),        #required
    path('sinup/', views.EnterdaUserplz, name = 'sinup'),
    path('accounts/login/', accounting.LoginView.as_view(template_name = 'entry.html',authentication_form=LogindaUser), name='login'),
    path('profile/', views.profile,name='profile'),  
    path('exit/', accounting.LogoutView.as_view(next_page='login'),name='exit'),
    
    path('passchange/', accounting.PasswordChangeView.as_view(template_name='passchange.html', form_class=Changedapassword,success_url='/afterpasschange/'),name='passchange'),
    
    path('afterpasschange/', accounting.PasswordChangeDoneView.as_view(template_name ='afterpasschange.html'),name='afterpasschange'),
    #forgot pass starts
    path('forgotpass/', accounting.PasswordResetView.as_view(template_name='forgotpass.html',form_class=Forgotpass),name='password_reset'),

    path('forgotpass/done/', accounting.PasswordResetDoneView.as_view(template_name='forgotpass_done.html'),name='password_reset_done'),

    path('forgotpass-confirm/<uidb64>/<token>/', accounting.PasswordResetConfirmView.as_view(template_name='forgotpass_confirm.html',form_class = ForgotpassConfirm),name='password_reset_confirm'),
    path('forgotpass-complete', accounting.PasswordResetCompleteView.as_view(template_name='forgotpass_complete.html'),name='password_reset_complete'),
    #forgot pass ends
    path('profileadd/', view=views.Profileadd.as_view(), name='profileadd'),
    path('showaddd/', views.showaddress,name='showaddd'),
    path('add-to-cart/',views.showcart, name = 'add-to-cart'),
    path('cart/',views.displaycart, name = 'cart'),
    path('cartadd/', views.cart_add),
    path('cartsubtract/', views.cart_subtract),
    path('cartremove/', views.removecart),
    path('checkout/',views.checkout, name = 'checkout'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),
    path('oredrs/', views.orders, name='orders'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)