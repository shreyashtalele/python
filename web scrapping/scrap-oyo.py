import requests
import requests
from bs4 import Beautifulsoup
import pandas
import argparse
import connect

parser=agrparse.argumentparser()
parser.add_argument("--page-nym-max",help="enter the number of pages to parse",type=int)
parser.add_argument("--dbname",help="enter the name of db ",type=str)
args=parser.parse_args()

oyo_url="https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX=args.page_num_MAX
scraped_info_list=[]
connect.req.(args.dbname)
 for page_num in range(1,page_num_MAX):
   print("GET Request for:"+url)
   req = requests.get(url)
   content= req.content


soup=Beautifulsoup(content."html.parser")

all_hotels=soup.find_all("div",{"class":"hotelcardlisting"})
scraped_info_list=[]

for hotel in all_hotels:
    hotel_dict={}
    hotel_dict["name"]=hotel.find("h3",{"class":"listingallhoteldescription_hotelname"}).text
    hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
    hotel_dict["price"]=hotel.find("span",{"class":"listingprice_finalprice"}).text
    try:
    hotel_dict["rating"]=hotel.find("span",{"class":"hotelrating_ratingsummary"}).text
    except AttributeError:
        hotel_dict["rating"]=none
    
    parent_amenities_element=hotel.find("div",{"class": "amenitywrapper"})
    
    amenities_list= []
    for amenity in parent_amenities_element.find("div",{"class": "amenitywrapper"})    
       amenities_list.append(amenity.find("span",{"class":"d-body-smd-textEllipsis"}).text)
       
       hotel_dict["amenities"]=', '.join(amenities_list[:-1])
       
       scraped_info_list.append(hotel_dict)
    
    print(hotel_name,hotel_address,hotel_price,hotel_rating,amenities_list)
    
dataframe = pandas.dataframe( scraped_info_list)
print("creating CSV file")
dataframe.to_csv("oyo.csv")
connect.get_hotel_info(args.dbname)
