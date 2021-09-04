import sys, inspect
import os
sys.path.append(SRC_PATH)
from api_wrapper import api_wrapper as api
from asset_list import Products
import time

ignoredFunctions = ["imag", "bit_length", "capitalize", "casefold", "center", "count", "encode", "expandtabs", "find", "format", "index", "isdigit", "lower", "startswith", "endswith", "encode", "isalnum", "isalpha", "isdecimal"]

#DATA Content:
#anno7
#onlineManager
#__spec__
#__package__
#subprocess
#console
#utils
#__loader__
#sys
#rdgs::SessionTime
#prober
#Prober
#scenes
#rdsdk::CRDString
#rdgs::BuildingGUID
#gameevents
#system
#rdgs::BuildingOrCraftableGUID
#rdgs::CorporationTime
#uiclasses
#TextSources
#debug
#ui
#rdgs::ProductAmount
#rdmath
#__doc__
#os
#__name__
#render
#net
#logger
#rdgs::CraftableGUID
#session
#rdgs::ProductGUID
#__builtins__
#game

maxdepth = 6

def main():
	wood_id = 120008
	
	popIDs = {
                'farmers': 15000000,
                'workers': 15000001,
                'artisans': 15000002,
                'engineers': 15000003,
                'investors': 15000004
                }
	start = time.time()

	#data = DATA['session']
	#scanFunctions(data, 0)
	#log('\n')
	#logline(time.time() - start)

	data = DATA['session'].jumpToSelection()
	logline(data)

	#logline(dir(data))
	#logline(len(data))
	#logline('\n')

def scanFunctions(dat, depth):
	global maxdepth
	if depth <= maxdepth:
		attributes = dir(dat)
		for attrib in attributes:
			for known in ignoredFunctions:
				if attrib.lower == known.lower:
					return	
			if not attrib.startswith("__"):
				for i in range(0, depth):
					log("\t")
				log(attrib)
				log("\n")
				#if not (atType == type("string") or atType == type(1) or atType == type(1.2)):
				try:
					scanFunctions(getattr(dat, attrib), depth + 1)
				except:
					# eat cake
					pass
					


def tryPopulation(dat):
	log(dat.GetAreaPopulation)

def log(text):
	with open(LOG_FILE, 'a') as log_file:
		log_file.write(str(text))

def logline(text):
	with open(LOG_FILE, 'a') as log_file:
		log_file.write(str(text)+'\r\n')

def getListofHistoricPop(modules, popIDs):
        for poptype, popID in popIDs.items():
                popvalues = []
                popvalues.append(getHistoricPop(modules, 0, popID))
                i=1
                while getHistoricPop(modules, i, popID) > 0:
                        popvalues.append(getHistoricPop(modules, i, popID))
                        i=i+1
                log(poptype+'\n'+''.join(str(popvalues))+'\n'+'---')
		
def getHistoricPop(modules, snapshotIndex, popID):
        return modules['TextSources'].TextSourceRoots.EconomyStatistic.History.GetPopulationAmount(snapshotIndex,popID)

def openConsole(modules):
	modules['console'].toggleVisibility()
	
def getTradeRoutes(modules):
	return scenes(modules).SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData
	
def getTradeRouteIDs(modules):
	routeData = getTradeRoutes(modules)
	return [route.RouteID for route in iter(routeData)]

def getAreasForRoute(modules, route):
	pass

def getAreaFromId(modules, areaID):
	return TextSourceRoots(modules).GetArea().GetAreaFromID(areaID)

def getStationsForTradeRoute(tradeRouteID):
	pass
	
def TextSourceRoots(modules):
	return modules['TextSources'].TextSourceRoots


def scenes(modules):
	return modules['scenes']
	
def iter(self):
	for i in range(len(self)):
		yield self[i]


def listener():
	scenes(DATA).SessionTradeRouteOverview.TradeRouteOverviewObject.RouteDat    
# Notes
def openCharterRoute(modules):
	modules['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.TransferData[1].RouteButtonClicked()
def openRoute(modules, index):
	modules['scenes'].SessionTradeRouteOverview.TradeRouteOverviewObject.RouteData[index].EditRouteClicked()
def getCargoForLAstSelectedShip():
	DATA['scenes'].ObjectMenuShip.ShipObject.CargoSlotData[0].ItemData.ButtonBehaviour.RefGUID
def openCreateRouteMenu():
	scenes(DATA).SessionTradeRouteOverview.TradeRouteOverviewObject.TradeRouteSelect
def islandCoordinates():
	scenes(DATA).StrategicMap.Data.IslandMarker[0].Position.x
main()

