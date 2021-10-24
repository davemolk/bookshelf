from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404
)

from .models import Record



