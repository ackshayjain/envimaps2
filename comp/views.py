from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import requests
# Create your views here
from .models import Complaint
from .forms import AddForm


def index(request):
    if request.method == 'POST':
        # create a form instance and popuslate it with data from the request:
        form = AddForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            title = request.POST.get('title', '')
            desc = request.POST.get('desc', '')
            location = request.POST.get('location', '')
            r = requests.get(
                "https://maps.googleapis.com/maps/api/geocode/json?address=" + location + "&key=AIzaSyCIXeZdC33t1bfnjdPKGmoVg5ebtT4ddNY")
            json = r.json()
            results = json['results']
            latLng = {'lat': 25.2234975, 'lng': 73.7477857}
            if(len(results) > 0):
                latLng = results[0]['geometry']['location']
            # {'lat': 25.2234975, 'lng': 73.7477857}
            pic = request.FILES.get('pic', '')
            comp_obj = Complaint(lat=latLng['lat'], lon=latLng['lng'], title=title, desc=desc, location=location,
                                 pic=pic)
            comp_obj.save()
            return HttpResponseRedirect(reverse('home:thanks'))
            # return render(request, 'ES/index2.html', context)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = AddForm()
        comp_list = Complaint.objects.all().order_by('-date_published')
        count = Complaint.objects.count()

        k = 0
        list_one = []
        list_rest = []
        for i in comp_list:
            if (k == 0):
                list_one.append(i)
            else:
                list_rest.append(i)
            k = k + 1

        # count_3 = count//3
        # if(count%3!=0):
        #   count_3 +=1

        # k=0
        # comp_sub_list=[]
        # comp_sub_list_one=[]

        # loc_list=[]

        # # print(count_3)
        # for i in comp_list:
        #   loc_list.append(str(i.location))

        # for i in range(0,count_3):
        #   comp_sub=[]

        #   if(i==count_3-1 and count%3!=0):
        #     r = range(0,count%3)

        #   else:
        #     r = range(0,3)
        #   # print(r)
        #   for j in r:
        #     comp_sub.append(comp_list[k])
        #     k=k+1
        #     # print(k)

        #   if(i==0):
        #     comp_sub_list_one = comp_sub
        #   else:
        #     comp_sub_list.append(comp_sub)

        # count_range = range(1,count_3)
        count_range = range(1, count)

        # context = {'comp':comp_list, 'sub_list':comp_sub_list, 'list_one':comp_sub_list_one,'r':count_range, 'form':form, 'loc':loc_list}
        context = {'comp': comp_list, 'r': count_range, 'one': list_one, 'rest': list_rest, 'form': form}

        # count_3 = count//3
        # if(count%3!=0):
        #   count_3 +=1

        # k=0
        # comp_sub_list=[]
        # comp_sub_list_one=[]

        # loc_list=[]
        # lat_list=[]
        # lon_list=[]
        # # print(count_3)
        # for i in comp_list:
        #   loc_list.append(str(i.location))
        #   lat_list.append(i.lat)
        #   lon_list.append(i.lon)

        # for i in range(0,count_3):
        #   comp_sub=[]

        #   if(i==count_3-1 and count%3!=0):
        #     r = range(0,count%3)

        #   else:
        #     r = range(0,3)
        #   # print(r)
        #   for j in r:
        #     comp_sub.append(comp_list[k])
        #     k=k+1
        #     # print(k)

        #   if(i==0):
        #     comp_sub_list_one = comp_sub
        #   else:
        #     comp_sub_list.append(comp_sub)

        # count_range = range(1,count_3)
        # context = {'comp':comp_list, 'sub_list':comp_sub_list, 'list_one':comp_sub_list_one,'r':count_range, 'form':form, 'loc':loc_list, 'lat':lat_list, 'lon':lon_list}

    return render(request, 'ES/index.html', context)


# def add_comp(request):

#     if request.method == 'POST':
#         # create a form instance and popuslate it with data from the request:
#         form = AddForm(request.POST, request.FILES)
#         # check whether it's valid:
#         if form.is_valid():

#            title = request.POST.get('title','')
#            desc = request.POST.get('desc','')
#            location = request.POST.get('location','')
#            pic = request.FILES.get('pic','')
#            comp_obj = Complaint(title = title,desc = desc, location=location, pic = pic)
#            comp_obj.save()
#            return HttpResponseRedirect(reverse('home:index'))


#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = AddForm()

#     return render(request, 'ES/index.html', {'form': form})


def thanks(request):
    return render(request, 'ES/thanks.html')


def hmap(request):
    comp_list = Complaint.objects.all()
    # [ [l,l], [l,l] ]
    latLng = []
    for i in comp_list:
        sub_list=[]
        sub_list.append(i.lat)
        sub_list.append(i.lon)
        latLng.append(sub_list)
    context = {'latLng':latLng}
    return render(request, 'ES/heatmap.html', context)
