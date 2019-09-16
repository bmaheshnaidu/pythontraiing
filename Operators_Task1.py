str_Language = "Telugu1"
int_TicketsCount = 7
int_TicketsAvialableCount=6
int_TicketRate = 150
if (str_Language =="English") & (int_TicketsCount<= int_TicketsAvialableCount) :
    print ("{0} tickets have been booked for {1} movie".format(int_TicketsCount , str_Language))
else:
    if (str_Language=="Telugu") & (int_TicketRate==150) & (int_TicketsCount<= int_TicketsAvialableCount):
        print("{0} tickets have been booked for {1} movie with rate {2} ".format (int_TicketsCount,str_Language,int_TicketRate))
    else:
        if int_TicketsAvialableCount >= int_TicketsCount :
            print("{0} tickets have been booked for {1} movie with rate {2} ".format(int_TicketsCount, str_Language,
                                                                                     int_TicketRate))
        else :
            print("No Tickets available")






