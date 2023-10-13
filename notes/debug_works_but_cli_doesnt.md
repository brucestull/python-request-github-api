# Debug Works but CLI Doesn't

## CLI

```powershell
(python-request-github-api) PS C:\Users\FlynntKnapp\Programming\python-request-github-api> python .\retrieve_private_repo.py
Status: 404
Status: 404
.gitignore not found or unable to fetch.
config/urls.py not found or unable to fetch.
(python-request-github-api) PS C:\Users\FlynntKnapp\Programming\python-request-github-api>
```

## Debug

```powershell
Status: 200

Contents of config/urls.py:
 """
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="boops/")),
    path('admin/', admin.site.urls),
    path('boops/', include('boops.urls'), name='boops'),
]
```
