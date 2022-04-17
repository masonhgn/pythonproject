#this program uses modules to get data  to do
#all sorts of plots.  Many programs might have
#code that does a similar thing.
#This particular program makes a plot for
#non EV sales of a chosen dealer versus  the
#average of all dealers.

from EvStudySomeListsandConstants import *
import sys #contains system commands such as exit program

from EvConstantsAboutValDatabase import *

#we load up these variables to write out as plots and such
import EvReturnsInfoForReportsAndPlots

DataBaseMonth, DataBaseYear, DaysInMonth,ValDataBase,DealerInfo = \
  EvReturnsInfoForReportsAndPlots.GivesUsValsToDoPlotsAndReports()
ValsThomasvilleDealer = []
ValsQuitmanDealer = []

XValues = []
for i in range(0,DaysInMonth):
    ValsThomasvilleDealer.append(0)
    ValsQuitmanDealer.append(0)
    XValues.append(i+1) #would be the day number in month

      
WhereInValDataBase = 0
while (WhereInValDataBase < len(ValDataBase)):
    ThisLine = ValDataBase[WhereInValDataBase]
    ThisDay = int(ThisLine[DayInsideDataBase])
    ThisDealer = int(ThisLine[DealerNumInsideDataBase])
    ThisBolt_EVI = int(ThisLine[CHEVY_BOLT_EVInsideDataBase])
    ThisBolt_EUV = int(ThisLine[CHEVY_BOLT_EUVInsideDataBase])
    ThisCADILLAC_LYRIQ = int(ThisLine[CADILLAC_LYRIQInsideDataBase])
    ThisGM_NON_EV = int(ThisLine[GM_NON_EVInsideDataBase])
    #some of the above might not be needed for every plot but we leave it
    #to make a useful template for creating other similar programs

    if ("Thomasville" in DealerInfo[ThisDealer][DEALER_NAME]):
      ValsThomasvilleDealer[ThisDay-1]=ValsThomasvilleDealer[ThisDay-1] + ThisBolt_EVI + ThisBolt_EUV + ThisCADILLAC_LYRIQ

    if ("Quitman" in DealerInfo[ThisDealer][DEALER_NAME]):
      ValsQuitmanDealer[ThisDay-1]=ValsQuitmanDealer[ThisDay-1] + ThisBolt_EVI + ThisBolt_EUV + ThisCADILLAC_LYRIQ


    WhereInValDataBase = WhereInValDataBase + 1

NumberOfDealers = len(DealerInfo)




#o.k. now we have the data to do our plot
import matplotlib.pyplot

matplotlib.pyplot.plot(XValues,ValsThomasvilleDealer,label="Thomasville")
matplotlib.pyplot.plot(XValues,ValsQuitmanDealer,label="Quitman")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
