from .models import News, Sponsors, Categories, Matches, Players
from django.http import JsonResponse, HttpRequest
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
    
date_after_month = datetime.today()+ relativedelta(months=1)
print('Today: ',datetime.today().strftime('%d/%m/%Y'))
print('After Month:', date_after_month.strftime('%d/%m/%Y'))

AMOUNT_OF_LATEST_NEWS = 3
    

def get_home_information():
    """ Initialize home with particular information """
    ...
    

def get_latest_news():
    return list(News.objects.all().order_by('id')[:AMOUNT_OF_LATEST_NEWS])


def get_all_news():
    return list(News.objects.values())


def get_new_by_id(id):
    try:
        return News.objects.get(id=id)._to_json()
    except:
       return None
 
 
def get_categories():
    categories = list(Categories.objects.all())
    print(categories)
    return list(map(lambda category: category._to_json(), categories))


def get_category_by_id(id):
    try:
        return Categories.objects.get(id=id)._to_json()
    except:
        return None

def get_sponsors():
    return list(map(lambda sponsor: sponsor._to_json(), Sponsors.objects.all()))


def get_matches_by_category_id(id):
    return list(map(lambda sponsor: sponsor._to_json(), Matches.objects.filter(category_id=id).order_by("match_date")))


def get_next_matches():
    start_date = datetime.today()
    end_date = datetime.today() + relativedelta(months=1)
    # return [ match._to_json() for match in Matches.objects.filter(match_date__range=(start_date, end_date)) ]
    return [ match._to_json() for match in Matches.objects.all() ]


def get_players_by_category_id(id):
    return list(map(lambda sponsor: sponsor._to_json(), Players.objects.filter(category_id=id, is_active=True)))


# REQUESTS

def news(request):
    res = JsonResponse(
        {
            "ok": True,
            "news": get_all_news()
        }
    )
    
    return res 

def new_by_id(request, id):
    new = get_new_by_id(id)
    print(id, new)
    response = JsonResponse(data={
            "ok": True,
            "data": new,
    }) if new else JsonResponse({
        "ok": False,
        "msg": "New couldn't be found",
    })
    
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    
    return response


def sponsors(request: HttpRequest):
    sponsors = get_sponsors()
    return JsonResponse({
        "ok": True,
        "data": sponsors,
    })


def home(request):
    latest_news = [new._to_json() for new in get_latest_news()]
    sponsors = get_sponsors()
    categories = get_categories()
    time.sleep(5)
    return JsonResponse(data={"ok": True, "data":
        {
            "news": latest_news,
            "sponsors": sponsors,
            "categories": categories
        }
    })
    
def categories(request):
    return JsonResponse({"ok": True, "categories": get_categories()})
    
    
def category_by_id(request, id):
    category = get_category_by_id(id)
    print(category)
    if not category:
        return JsonResponse({
            "ok": False,
            "msg": "Category couldn't be found"
        })

    matches = get_matches_by_category_id(id)
    
    players = get_players_by_category_id(id)

    return JsonResponse({
            "ok": True,
            "data": {
                "category": category,
                "matches": matches,
                "team": {
                    "staff": {
                        "trainer": category.get("trainer") | {"title": "trainer"},
                        "delegate": category.get("delegate") | {"title": "delegate"}
                    },
                    "players": players
                } 
            }
        })


def next_matches(request):
    return JsonResponse({"ok": True, "data": get_next_matches()})


def latest_news(request):
    latest_news = [new._to_json() for new in get_latest_news()]
    
    return JsonResponse({"ok": True, "data": latest_news})


# def insert_new(request):
#     new = News(title='title2', subtitle='2', date='dat2e2')
#     new.save()
#     return JsonResponse({"msg": "New has been inserted successfuly."})


# def insert_tag(request, id):
#     new = News.objects.get(id=id)
#     if not new:
#         return JsonResponse({"ok": False, "msg": "New could not be found"})

#     return JsonResponse({
#         "ok": True,
#         "msg": "Tag has been inserted successfuly.",
#     })

