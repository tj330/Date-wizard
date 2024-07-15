import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%d/%m/%Y")
    month = now.strftime("%B")
    text = month_description(month)

    return render(request, "date/index.html", {"date":date,"time":time, "month":month, "text":text})

def month_description(month):
    match month:
        case "January":
            para = "January marks the beginning of the year and is often associated with new beginnings and resolutions. In the Northern Hemisphere, it is typically the coldest month, featuring winter weather, snow, and long nights."
            return para

        case "February":
            para = "February is the shortest month of the year, with 28 or 29 days. It's known for Valentine's Day on the 14th, celebrating love and affection. In the Northern Hemisphere, it remains cold, with winter continuing."
            return para
        
        case "March":
            para = "March heralds the arrival of spring in the Northern Hemisphere, with warmer weather and blossoming flowers. It includes St. Patrick's Day on the 17th and marks the beginning of the vernal equinox."
            return para
        
        case "April":
            para = "April is characterized by spring showers and blooming flowers. It's a month of renewal and growth, with celebrations like Easter and Earth Day promoting environmental awareness."
            return para
        
        case "May":
            para = "May brings warmer weather and longer days in the Northern Hemisphere. It is often associated with blooming flowers, Mother's Day, and the start of many outdoor activities and festivals."
            return para
        
        case "June":
            para = "June marks the beginning of summer in the Northern Hemisphere, with the longest day of the year occurring during the summer solstice. It's a time for vacations, outdoor activities, and celebrations like Father's Day."
            return para
        
        case "July":
            para = "July is typically the warmest month of the year in the Northern Hemisphere, featuring Independence Day celebrations in the USA on the 4th. It's a popular month for travel, beach outings, and barbecues."
            return para
        
        case "August":
            para = "August continues the summer season, with hot weather and long days. It's a time for vacations, outdoor events, and enjoying the last full month of summer before the onset of autumn."
            return para
        
        case "September":
            para = "September marks the transition from summer to autumn in the Northern Hemisphere, with cooler temperatures and changing foliage. It includes the start of the school year and Labor Day celebrations in the USA."
            return para
        
        case "October":
            para = "October is known for its autumn colors, cooler weather, and harvest festivals. Halloween on the 31st is a major highlight, with costumes, trick-or-treating, and spooky decorations."
            return para
        
        case "November":
            para = "November brings colder weather and the onset of winter in many regions. It includes significant holidays like Thanksgiving in the USA, emphasizing gratitude and family gatherings."
            return para
        
        case "December":
            para = "December is associated with winter holidays, including Christmas, Hanukkah, and New Year's Eve. It's a festive month with celebrations, decorations, and a focus on family, giving, and reflection on the past year."
            return para
        
def day(request):
    if request.method == 'POST': 
        input_date = request.POST['input_date']
        date = datetime.datetime.strptime(input_date, "%d/%m/%Y")
        date_day = date.weekday()

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = days[date_day]
        data = {"input_date":input_date,"day": day }
    else:
        data = {}
    return render(request,"date/day.html", data)

def goal(request):
    if request.method == 'POST': 
        input_goal = request.POST["input_goal"]
        input_deadline = request.POST["input_deadline"]

        deadline_date = datetime.datetime.strptime(input_deadline, "%d/%m/%Y")
        today_date = datetime.datetime.today()
        time_till = (deadline_date - today_date).days

        data = {
            "input_goal":input_goal, "remaining_days": time_till
        }
    else:
        data = {}
    return render(request, "date/goal.html", data)