from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserUpdateForm
from django.views.generic import FormView, View
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages



class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'accounts/user_registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # print(form.cleaned_data)
        user=form.save()
        login(self.request, user)
        # print(user)

        messages.success(self.request, f'Account Successfully Created')
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        messages.success(self.request ,'Logged in Successfully')
        return reverse_lazy('home')

class UserLogoutView(View):
    # def get_success_url(self):
    #     if self.request.user.is_authenticated:
    #         logout(self.request)
    #     return reverse_lazy('home')

    def get(self, request):
        logout(request)
        messages.success(self.request ,'Logged Out Successfully')
        return redirect('home')
    
    # def get_next_page(self):
    #     return redirect('home')


class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(self.request ,'Profile Successfully Updated')
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
