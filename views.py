from django.shortcuts import render
from django.views import View

class BearingListView(View):
    def get(self, request):
        # Logic for listing bearings
        return render(request, 'bearings/bearing_list.html')

class BearingDetailView(View):
    def get(self, request, pk):
        # Logic for displaying bearing details
        return render(request, 'bearings/bearing_detail.html')
