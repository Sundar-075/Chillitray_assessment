from django.urls import path
from .views import GetPages, Login, Signin, Signup, TaskAddView, TaskGetView, Taskaddfun, UserSignup, index, logout, signup_code

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', UserSignup.as_view(), name="signup"),
    path('sign-up/', Signup, name="sign-up"),
    path('sign-up-urls/', signup_code, name="signCode"),
    path('', index, name="index"),
    path('login/', Login, name="login"),
    path('signin/', Signin, name="signin"),
    path('logout/', logout, name="logout"),

    path('task-create/', TaskAddView.as_view(), name="taskCreate"),
    path('taskfun', Taskaddfun, name="taskFun"),
    path('get-task', TaskGetView.as_view(), name="getTask"),
    path('getpage', GetPages, name="pages")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
